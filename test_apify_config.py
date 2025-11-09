"""Test different Apify configurations to get subtitles."""
import os
from apify_client import ApifyClient
from dotenv import load_dotenv
import json

load_dotenv()

client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Test with MORE subtitle options
print("🧪 Testing Apify with enhanced subtitle configuration...\n")

test_configs = [
    {
        "name": "Config 1: Basic scrapeSubtitles",
        "input": {
            "startUrls": [{"url": "https://www.youtube.com/watch?v=7CYmTLHOUtU"}],
            "maxResults": 1,
            "scrapeSubtitles": True,
        }
    },
    {
        "name": "Config 2: With subtitle languages",
        "input": {
            "startUrls": [{"url": "https://www.youtube.com/watch?v=7CYmTLHOUtU"}],
            "maxResults": 1,
            "scrapeSubtitles": True,
            "subtitleLanguages": ["tr", "en"],  # Turkish and English
        }
    },
    {
        "name": "Config 3: With subtitleFormat",
        "input": {
            "startUrls": [{"url": "https://www.youtube.com/watch?v=7CYmTLHOUtU"}],
            "maxResults": 1,
            "scrapeSubtitles": True,
            "subtitleFormat": "text",
        }
    },
]

for config in test_configs:
    print(f"\n{'='*80}")
    print(f"Testing: {config['name']}")
    print(f"{'='*80}\n")

    try:
        run = client.actor("streamers/youtube-scraper").call(run_input=config['input'])

        for item in client.dataset(run["defaultDatasetId"]).iterate_items():
            print(f"✅ Video: {item.get('title')}")
            print(f"\n📋 Subtitle-related fields:")

            # Check all possible subtitle fields
            subtitle_fields = [
                'subtitles', 'subtitle', 'captions', 'caption',
                'transcript', 'text', 'translatedText'
            ]

            for field in subtitle_fields:
                value = item.get(field)
                if value:
                    preview = str(value)[:200] if value else "None"
                    print(f"  - {field}: {preview}...")

            # Show if text field has content
            if item.get('text'):
                print(f"\n📝 text field (first 300 chars):")
                print(f"  {item.get('text')[:300]}...")

            break  # Only show first video

    except Exception as e:
        print(f"❌ Error: {e}")

print(f"\n{'='*80}")
print("Test complete!")
