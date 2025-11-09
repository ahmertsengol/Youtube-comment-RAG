# Quick Start Guide

Get started with the YouTube Channel RAG Tool in 3 simple steps!

## Step 1: Get Your API Keys

### Gemini API Key
1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click "Create API Key"
3. Copy the key

### Apify API Token
1. Go to [Apify Console](https://console.apify.com/account/integrations)
2. Sign up or log in
3. Find your API token in the Integrations section
4. Copy the token

## Step 2: Run Setup

```bash
# Run the setup script
./setup.sh

# Or manually:
pip3 install -r requirements.txt
cp .env.example .env
```

## Step 3: Configure Your API Keys

Edit the `.env` file:

```bash
nano .env
```

Replace the placeholder values:

```
GEMINI_API_KEY=your_actual_gemini_api_key
APIFY_API_TOKEN=your_actual_apify_token
```

Save and exit (Ctrl+X, then Y, then Enter in nano).

## Step 4: Run the Tool!

```bash
python3 main.py
```

You'll be asked:
1. **YouTube Channel URL** - Example: `https://www.youtube.com/@veritasium`
2. **Number of videos** - Example: `10`

Then wait for:
- Videos to be scraped (1-2 minutes)
- Transcripts to be uploaded to Gemini (1-2 minutes)
- Chat interface to start

## Example Usage

```
$ python3 main.py

YouTube Channel RAG Tool
Scrape YouTube videos and chat with transcripts using AI

Step 1: YouTube Channel Information
Enter YouTube channel URL: https://www.youtube.com/@veritasium
How many videos to scrape (newest to oldest) [10]: 5

Step 2: Scraping Videos
🔍 Scraping 5 videos from channel...
⏳ Running Apify YouTube scraper...
📥 Fetching results...
✅ Successfully scraped 5 videos

Step 3: Saving Transcripts
💾 Saved: transcripts/abc123.txt
💾 Saved: transcripts/def456.txt
...

Step 4: Setting up RAG with Gemini API
📤 Uploading 5 files to Gemini API...
⏳ Processing files...
✅ All files ready

Chat Interface
Type your questions about the videos. Type 'quit' or 'exit' to end.

You: What are the main topics in these videos?
AI Assistant: Based on the transcripts, the main topics covered are...
```

## Tips

- Start with 5-10 videos to test
- The free tier of both APIs is sufficient for testing
- Transcripts are saved locally in `transcripts/` folder
- You can re-run chat.py to query existing transcripts without re-scraping

## Troubleshooting

### "APIFY_API_TOKEN not found"
- Make sure you created the `.env` file
- Check that there are no spaces around the `=` sign
- Ensure you saved the file

### "No videos found"
- Check the YouTube channel URL is correct
- Try a different channel
- Make sure the channel has public videos

### "Error uploading files"
- Check your Gemini API key is valid
- You might have hit rate limits - wait a few minutes
- Check your API quota

## Next Steps

- Ask questions about the video content
- Try different channels
- Adjust the number of videos
- Read the full [README.md](README.md) for more details

## Example Questions to Ask

Once your transcripts are loaded, try asking:

- "Summarize all the videos"
- "What did [creator] say about [topic]?"
- "Which video discusses [keyword]?"
- "Compare the different approaches mentioned"
- "What are the key takeaways?"
- "Find all mentions of [term]"

Enjoy exploring YouTube content with AI! 🎉
