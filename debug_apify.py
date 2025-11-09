"""Debug script to see what Apify returns."""
import os
import json
from apify_client import ApifyClient
from dotenv import load_dotenv

load_dotenv()

# Initialize client
api_token = os.getenv("APIFY_API_TOKEN")
client = ApifyClient(api_token)

# Test with one video
channel_url = input("Enter YouTube channel URL: ")

run_input = {
    "startUrls": [{"url": channel_url}],
    "maxResults": 1,  # Just get 1 video for testing
    "scrapeSubtitles": True,
    "scrapeChannelInfo": False,
    "scrapeComments": False,
    "scrapeDescriptions": True,
}

print("⏳ Running Apify YouTube scraper...")
run = client.actor("streamers/youtube-scraper").call(run_input=run_input)

print("\n📥 Fetching results...")
print("="*80)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print("\n🔍 RAW DATA FROM APIFY:")
    print("="*80)
    print(json.dumps(item, indent=2, ensure_ascii=False))
    print("="*80)

    print("\n📋 AVAILABLE FIELDS:")
    for key in item.keys():
        value_preview = str(item[key])[:100] if item[key] else "None"
        print(f"  - {key}: {value_preview}")

    print("\n"+"="*80)
    break  # Only show first video
