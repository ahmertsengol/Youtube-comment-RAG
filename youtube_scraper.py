"""YouTube video scraper using Apify."""
import os
import time
from typing import List, Dict
from apify_client import ApifyClient
from dotenv import load_dotenv

load_dotenv()


class YouTubeScraper:
    """Scraper for YouTube channel videos using Apify."""

    def __init__(self):
        """Initialize the Apify client."""
        api_token = os.getenv("APIFY_API_TOKEN")
        if not api_token:
            raise ValueError("APIFY_API_TOKEN not found in environment variables")
        self.client = ApifyClient(api_token)

    def scrape_channel(self, channel_url: str, max_videos: int = 10) -> List[Dict]:
        """
        Scrape videos from a YouTube channel.

        Args:
            channel_url: YouTube channel URL
            max_videos: Maximum number of videos to scrape (newest first)

        Returns:
            List of video data dictionaries
        """
        print(f"🔍 Scraping {max_videos} videos from channel: {channel_url}")

        # Prepare the Actor input
        run_input = {
            "startUrls": [{"url": channel_url}],
            "maxResults": max_videos,
            "scrapeSubtitles": True,  # Get video transcripts
            "scrapeChannelInfo": False,
            "scrapeComments": False,
            "scrapeDescriptions": True,
        }

        # Run the Actor and wait for it to finish
        print("⏳ Running Apify YouTube scraper...")
        run = self.client.actor("streamers/youtube-scraper").call(run_input=run_input)

        # Fetch Actor results from the run's dataset
        videos = []
        print("📥 Fetching results...")
        for item in self.client.dataset(run["defaultDatasetId"]).iterate_items():
            video_data = {
                "video_id": item.get("id"),
                "title": item.get("title"),
                "description": item.get("description", ""),
                "url": item.get("url"),
                "published_at": item.get("publishedAt"),
                "duration": item.get("duration"),
                "view_count": item.get("viewCount"),
                "subtitles": item.get("subtitles", ""),
            }
            videos.append(video_data)

        print(f"✅ Successfully scraped {len(videos)} videos")
        return videos

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
            subtitles = video["subtitles"]

            # Create filename from video ID
            filename = f"{output_dir}/{video_id}.txt"

            # Write transcript with metadata
            with open(filename, "w", encoding="utf-8") as f:
                f.write(f"Title: {title}\n")
                f.write(f"URL: {video['url']}\n")
                f.write(f"Published: {video.get('published_at', 'Unknown')}\n")
                f.write(f"Duration: {video.get('duration', 'Unknown')}\n")
                f.write(f"Views: {video.get('view_count', 'Unknown')}\n")
                f.write(f"\n{'='*80}\n\n")
                f.write(f"Description:\n{video['description']}\n\n")
                f.write(f"{'='*80}\n\n")
                f.write(f"Transcript:\n{subtitles}\n")

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
