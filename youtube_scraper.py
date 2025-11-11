"""YouTube video transcript scraper using YouTube Transcript API."""
import os
import re
from typing import List, Dict, Optional
from apify_client import ApifyClient
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    TranscriptsDisabled,
    NoTranscriptFound,
    VideoUnplayable,
    VideoUnavailable,
)
from dotenv import load_dotenv

load_dotenv()

# pylint: disable=redefined-outer-name


class YouTubeScraper:
    """Scraper for YouTube video transcripts."""

    def __init__(self):
        """Initialize the scraper."""
        # Apify is only used for getting video URLs from channels
        api_token = os.getenv("APIFY_API_TOKEN")
        self.apify_client = ApifyClient(api_token) if api_token else None

    def _get_channel_video_urls(self, channel_url: str, max_videos: int) -> List[Dict]:
        """
        Get video URLs and metadata from a YouTube channel.

        Args:
            channel_url: YouTube channel URL
            max_videos: Maximum number of videos to fetch

        Returns:
            List of dictionaries with video metadata
        """
        if not self.apify_client:
            raise ValueError("APIFY_API_TOKEN required for channel scraping. Set it in .env file")

        print(f"🔍 Fetching video list from channel: {channel_url}")

        # Use streamers/youtube-scraper to get video metadata
        run_input = {
            "startUrls": [{"url": channel_url}],
            "maxResults": max_videos,
            "scrapeSubtitles": False,
            "scrapeChannelInfo": False,
            "scrapeComments": False,
            "scrapeDescriptions": False,
        }

        run = self.apify_client.actor("streamers/youtube-scraper").call(run_input=run_input)

        videos = []
        for item in self.apify_client.dataset(run["defaultDatasetId"]).iterate_items():
            video_info = {
                "url": item.get("url"),
                "title": item.get("title", "Unknown Title"),
                "video_id": item.get("id"),
            }
            if video_info["url"]:
                videos.append(video_info)

        print(f"✅ Found {len(videos)} videos")
        return videos

    def scrape_channel(self, channel_url: str, max_videos: int = 10) -> List[Dict]:
        """
        Scrape video transcripts from a YouTube channel.

        Args:
            channel_url: YouTube channel URL
            max_videos: Maximum number of videos to scrape (newest first)

        Returns:
            List of video data dictionaries with transcripts
        """
        # Step 1: Get video URLs from channel
        video_infos = self._get_channel_video_urls(channel_url, max_videos)

        if not video_infos:
            print("❌ No videos found in channel")
            return []

        # Step 2: Get transcripts for each video
        print(f"\n📝 Fetching transcripts for {len(video_infos)} videos...")
        videos = []

        for i, video_info in enumerate(video_infos, 1):
            video_url = video_info["url"]
            print(f"\n[{i}/{len(video_infos)}] Processing: {video_info['title']}")

            try:
                video_data = self._scrape_single_video(video_url)
                if video_data:
                    # Update title from Apify metadata
                    video_data['title'] = video_info['title']
                    videos.append(video_data)
                    print(f"✅ Transcript fetched ({len(video_data['transcript'])} chars)")
                else:
                    print("⚠️  No transcript available")
            except (ValueError, KeyError, TypeError) as e:
                print(f"❌ Error processing video: {e}")
                continue
            except (ConnectionError, TimeoutError, OSError) as e:
                # Network-related errors
                print(f"❌ Network error: {e}")
                continue
            except Exception as e:  # noqa: BLE001
                # Catch any other unexpected errors (API changes, etc.)
                print(f"❌ Unexpected error: {e}")
                continue

        print(f"\n✅ Successfully scraped {len(videos)} videos with transcripts")
        return videos

    def _scrape_single_video(self, video_url: str) -> Optional[Dict]:
        """
        Scrape transcript from a single YouTube video using YouTube Transcript API.

        Args:
            video_url: YouTube video URL

        Returns:
            Video data dictionary with transcript, or None if no transcript available
        """
        # Extract video ID from URL
        video_id = self._extract_video_id(video_url)
        if not video_id:
            print(f"❌ Could not extract video ID from URL: {video_url}")
            return None

        try:
            # Try multiple language options with fallback
            # Priority: English > Turkish > any available language
            transcript_data = None
            api = YouTubeTranscriptApi()

            # Try English first (most common)
            try:
                fetched = api.fetch(video_id, languages=['en'])
                transcript_data = fetched.to_raw_data()
            except (TranscriptsDisabled, NoTranscriptFound):
                pass

            # Try Turkish
            if not transcript_data:
                try:
                    fetched = api.fetch(video_id, languages=['tr'])
                    transcript_data = fetched.to_raw_data()
                except (TranscriptsDisabled, NoTranscriptFound):
                    pass

            # Try any available language (auto-generated or manual)
            if not transcript_data:
                try:
                    # This will get the first available transcript
                    fetched = api.fetch(video_id)
                    transcript_data = fetched.to_raw_data()
                except (TranscriptsDisabled, NoTranscriptFound):
                    pass

            if not transcript_data:
                return None

            # Combine all text segments into one string
            full_text = " ".join([entry['text'] for entry in transcript_data])

            if not full_text.strip():
                return None

            video_data = {
                "video_id": video_id,
                "title": "Unknown Title",  # Title will be set from Apify data in scrape_channel
                "url": video_url,
                "transcript": full_text,
            }
            return video_data

        except TranscriptsDisabled:
            print("⚠️  Transcripts disabled for this video")
            return None
        except NoTranscriptFound:
            print("⚠️  No transcript found for this video")
            return None
        except VideoUnplayable as e:
            # Handle members-only or restricted videos
            error_msg = str(e)
            if "members-only" in error_msg.lower() or "member" in error_msg.lower():
                print("🔒 Members-only video (transcript not available)")
            else:
                print(f"⚠️  Video unplayable: {error_msg[:100]}")
            return None
        except VideoUnavailable:
            print("⚠️  Video unavailable")
            return None
        except (ValueError, TypeError, KeyError) as e:
            print(f"❌ Error processing transcript: {e}")
            return None
        except (ConnectionError, TimeoutError, OSError) as e:
            # Network-related errors
            print(f"❌ Network error: {e}")
            return None
        except Exception as e:  # noqa: BLE001
            # Catch any other unexpected errors (API changes, etc.)
            error_msg = str(e)
            # Check if it's a members-only error in the message
            if "members-only" in error_msg.lower() or "member" in error_msg.lower():
                print("🔒 Members-only video (transcript not available)")
            else:
                print(f"❌ Unexpected error: {error_msg[:150]}")
            return None

    @staticmethod
    def _extract_video_id(video_url: str) -> Optional[str]:
        """
        Extract video ID from YouTube URL.

        Args:
            video_url: YouTube video URL

        Returns:
            Video ID or None if not found
        """
        patterns = [
            r'(?:v=|\/)([\w-]{11})',  # Standard watch URL
            r'youtu\.be\/([\w-]{11})',  # Short URL
            r'embed\/([\w-]{11})',  # Embed URL
        ]

        for pattern in patterns:
            match = re.search(pattern, video_url)
            if match:
                return match.group(1)

        return None

    def save_transcripts(self, videos: List[Dict], output_dir: str = "transcripts") -> List[str]:
        """
        Save video transcripts to individual files.

        Args:
            videos: List of video data dictionaries
            output_dir: Directory to save transcript files

        Returns:
            List of file paths
        """
        os.makedirs(output_dir, exist_ok=True)
        file_paths = []

        for video in videos:
            video_id = video["video_id"]
            title = video["title"]
            transcript = video["transcript"]

            # Create filename from video ID
            filename = f"{output_dir}/{video_id}.txt"

            # Write transcript with minimal metadata
            with open(filename, "w", encoding="utf-8") as f:
                f.write(f"Title: {title}\n")
                f.write(f"URL: {video['url']}\n")
                f.write(f"\n{'='*80}\n\n")
                f.write(f"Transcript:\n{transcript}\n")

            file_paths.append(filename)
            print(f"💾 Saved: {filename}")

        return file_paths


if __name__ == "__main__":
    # Test the scraper
    scraper = YouTubeScraper()
    channel_url = input("Enter YouTube channel URL: ")
    max_videos = int(input("How many videos to scrape? "))

    videos = scraper.scrape_channel(channel_url, max_videos)
    file_paths = scraper.save_transcripts(videos)

    print(f"\n✅ Saved {len(file_paths)} transcripts")
