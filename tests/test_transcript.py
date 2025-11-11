"""Quick test script for the new transcript scraper."""
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from youtube_scraper import YouTubeScraper

print("🧪 Testing YouTube Transcript Scraper")
print("=" * 80)
print("ℹ️  This test uses YouTube's FREE transcript API - no Apify needed!\n")

# Test with a single video
test_video_url = "https://www.youtube.com/watch?v=89CQRxq0YSg"
print(f"Testing with video: {test_video_url}\n")

scraper = YouTubeScraper()

# Test single video scraping
print("Step 1: Testing single video transcript extraction...")
print("-" * 80)

video_data = scraper._scrape_single_video(test_video_url)

if video_data:
    print("\n✅ SUCCESS! Transcript fetched:")
    print(f"   - Video ID: {video_data['video_id']}")
    print(f"   - Title: {video_data['title']}")
    print(f"   - URL: {video_data['url']}")
    print(f"   - Transcript length: {len(video_data['transcript'])} characters")
    print("\n   First 500 characters of transcript:")
    print("   " + "-" * 76)
    print(f"   {video_data['transcript'][:500]}...")
    print("   " + "-" * 76)
else:
    print("\n❌ FAILED: No transcript found")
    print("This video might not have subtitles/captions available.")
    print("Try a different video URL.")

print(f"\n{'=' * 80}")
print("\n🎯 Next steps:")
print("1. If test passed: Install youtube-transcript-api with:")
print("   pip install youtube-transcript-api")
print("2. For channel scraping, you still need APIFY_API_TOKEN in .env")
print("3. Run main.py to scrape a full channel")
print(f"\n{'=' * 80}")
