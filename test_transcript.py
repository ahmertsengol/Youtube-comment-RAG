"""Quick test script for the new transcript scraper."""
import os
from youtube_scraper import YouTubeScraper
from dotenv import load_dotenv

load_dotenv()

# Check if API token exists
if not os.getenv("APIFY_API_TOKEN"):
    print("❌ APIFY_API_TOKEN not found in .env file")
    print("Please create a .env file with your Apify API token:")
    print("APIFY_API_TOKEN=your_token_here")
    exit(1)

print("🧪 Testing YouTube Transcript Scraper\n")
print("=" * 80)

# Test with a single video
test_video_url = "https://www.youtube.com/watch?v=89CQRxq0YSg"
print(f"Testing with video: {test_video_url}\n")

scraper = YouTubeScraper()

# Test single video scraping
print("Step 1: Testing single video transcript extraction...")
print("-" * 80)

video_data = scraper._scrape_single_video(test_video_url)

if video_data:
    print(f"\n✅ SUCCESS! Transcript fetched:")
    print(f"   - Video ID: {video_data['video_id']}")
    print(f"   - Title: {video_data['title']}")
    print(f"   - URL: {video_data['url']}")
    print(f"   - Transcript length: {len(video_data['transcript'])} characters")
    print(f"\n   First 500 characters of transcript:")
    print(f"   {'-' * 76}")
    print(f"   {video_data['transcript'][:500]}...")
    print(f"   {'-' * 76}")
else:
    print("\n❌ FAILED: No transcript found")
    print("This video might not have subtitles/captions available.")

print(f"\n{'=' * 80}")
print("\n🎯 Next steps:")
print("1. If test passed: Run main.py to scrape a full channel")
print("2. If test failed: Check your APIFY_API_TOKEN and try a different video")
print(f"\n{'=' * 80}")
