"""YouTube video transcript scraper using Apify."""
import os
import time
import re
from typing import List, Dict
from apify_client import ApifyClient
from dotenv import load_dotenv

load_dotenv()


class YouTubeScraper:
    """Scraper for YouTube video transcripts using Apify."""

    def __init__(self):
        """Initialize the Apify client."""
        api_token = os.getenv("APIFY_API_TOKEN")
        if not api_token:
            raise ValueError("APIFY_API_TOKEN not found in environment variables")
        self.client = ApifyClient(api_token)

    def _get_channel_video_urls(self, channel_url: str, max_videos: int) -> List[str]:
        """
        Get video URLs from a YouTube channel.

        Args:
            channel_url: YouTube channel URL
            max_videos: Maximum number of videos to fetch

        Returns:
            List of video URLs
        """
        print(f"🔍 Fetching video list from channel: {channel_url}")

        # Use streamers/youtube-scraper to get video URLs only
        run_input = {
            "startUrls": [{"url": channel_url}],
            "maxResults": max_videos,
            "scrapeSubtitles": False,  # We don't need subtitles here
            "scrapeChannelInfo": False,
            "scrapeComments": False,
            "scrapeDescriptions": False,
        }

        run = self.client.actor("streamers/youtube-scraper").call(run_input=run_input)

        video_urls = []
        for item in self.client.dataset(run["defaultDatasetId"]).iterate_items():
            url = item.get("url")
            if url:
                video_urls.append(url)

        print(f"✅ Found {len(video_urls)} videos")
        return video_urls

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
        video_urls = self._get_channel_video_urls(channel_url, max_videos)

        if not video_urls:
            print("❌ No videos found in channel")
            return []

        # Step 2: Get transcripts for each video
        print(f"\n📝 Fetching transcripts for {len(video_urls)} videos...")
        videos = []

        for i, video_url in enumerate(video_urls, 1):
            print(f"\n[{i}/{len(video_urls)}] Processing: {video_url}")

            try:
                video_data = self._scrape_single_video(video_url)
                if video_data:
                    videos.append(video_data)
                    print(f"✅ Transcript fetched ({len(video_data['transcript'])} chars)")
                else:
                    print(f"⚠️  No transcript available")
            except Exception as e:
                print(f"❌ Error: {e}")
                continue

            # Small delay to avoid rate limiting
            if i < len(video_urls):
                time.sleep(1)

        print(f"\n✅ Successfully scraped {len(videos)} videos with transcripts")
        return videos

    def _scrape_single_video(self, video_url: str) -> Dict:
        """
        Scrape transcript from a single YouTube video.

        Args:
            video_url: YouTube video URL

        Returns:
            Video data dictionary with transcript
        """
        # Extract video ID from URL
        video_id_match = re.search(r'(?:v=|\/)([\w-]{11})', video_url)
        video_id = video_id_match.group(1) if video_id_match else None

        # Use dedicated transcript scraper
        run_input = {
            "videoUrls": [video_url],
            "language": "en",  # Primary language (will fallback to auto-generated if not available)
        }

        run = self.client.actor("knowbaseai/youtube-transcript-extractor").call(run_input=run_input)

        # Fetch transcript from results
        for item in self.client.dataset(run["defaultDatasetId"]).iterate_items():
            transcript = item.get("transcript", "")

            # Skip if no transcript
            if not transcript or transcript.strip() == "":
                return None

            video_data = {
                "video_id": video_id or item.get("videoId", "unknown"),
                "title": item.get("title", "Unknown Title"),
                "url": video_url,
                "transcript": transcript,
            }
            return video_data

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
