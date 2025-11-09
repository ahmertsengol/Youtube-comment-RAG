# YouTube Channel RAG Tool

A powerful RAG (Retrieval Augmented Generation) tool that scrapes YouTube channel videos, extracts transcripts, and enables AI-powered chat interactions with the content using Google's Gemini API.

## Features

- 🎥 Scrape videos from any YouTube channel using Apify
- 📝 Extract video transcripts, titles, and metadata
- 🤖 AI-powered chat interface using Gemini API with file search
- 💾 Persistent transcript storage
- 🔍 Intelligent search across all video content
- 💬 Interactive chat interface to query video content

## Prerequisites

- Python 3.8+
- Gemini API key ([Get one here](https://aistudio.google.com/app/apikey))
- Apify API token ([Get one here](https://console.apify.com/account/integrations))

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd Youtube-comment-RAG
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
```

4. Edit `.env` and add your API keys:
```env
GEMINI_API_KEY=your_gemini_api_key_here
APIFY_API_TOKEN=your_apify_api_token_here
```

## Usage

### Option 1: Complete Workflow (Scrape + Chat)

Run the main script to scrape videos and immediately start chatting:

```bash
python main.py
```

You'll be prompted to:
1. Enter the YouTube channel URL
2. Specify how many videos to scrape (newest to oldest)
3. Wait for scraping and indexing to complete
4. Start chatting with the transcripts!

Example:
```
Enter YouTube channel URL: https://www.youtube.com/@channelname
How many videos to scrape: 20
```

### Option 2: Chat with Existing Transcripts

If you've already scraped videos and want to chat again:

```bash
python chat.py
```

This will load existing transcripts from the `transcripts/` directory and start the chat interface.

## Project Structure

```
Youtube-comment-RAG/
├── main.py              # Main orchestration script
├── chat.py              # Standalone chat interface
├── youtube_scraper.py   # Apify YouTube scraper module
├── gemini_rag.py        # Gemini API RAG implementation
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variables template
├── .gitignore          # Git ignore file
├── transcripts/        # Saved video transcripts (auto-created)
└── README.md           # This file
```

## How It Works

1. **Scraping**: Uses Apify's YouTube scraper to fetch video metadata and transcripts
2. **Storage**: Saves each video's transcript with metadata to individual text files
3. **Indexing**: Uploads transcripts to Gemini API for AI-powered search
4. **Chat**: Provides an interactive interface to ask questions about the video content

## Example Questions

Once your transcripts are indexed, you can ask questions like:

- "What are the main topics covered in these videos?"
- "Summarize the video about [specific topic]"
- "What did the creator say about [topic]?"
- "Find all mentions of [keyword]"
- "Compare the approaches discussed in different videos"

## API Documentation

- **Apify YouTube Scraper**: [https://apify.com/streamers/youtube-scraper](https://apify.com/streamers/youtube-scraper)
- **Gemini API File Search**: [https://ai.google.dev/gemini-api/docs/file-search](https://ai.google.dev/gemini-api/docs/file-search)
- **Apify API Docs**: [https://docs.apify.com/](https://docs.apify.com/)

## Modules

### youtube_scraper.py
- `YouTubeScraper`: Main class for scraping YouTube channels
- `scrape_channel()`: Scrapes videos from a channel
- `save_transcripts()`: Saves transcripts to files

### gemini_rag.py
- `GeminiRAG`: RAG implementation using Gemini API
- `upload_files()`: Uploads transcripts to Gemini
- `chat()`: Query the RAG system
- `delete_all_files()`: Clean up uploaded files

### main.py
Main orchestration script that:
1. Prompts for channel URL and video count
2. Scrapes videos using Apify
3. Saves transcripts locally
4. Uploads to Gemini API
5. Starts interactive chat

### chat.py
Standalone chat interface for querying existing transcripts.

## Troubleshooting

### "APIFY_API_TOKEN not found"
Make sure you've created a `.env` file with your API token.

### "No transcript files found"
Run `main.py` first to scrape videos, or check that the `transcripts/` directory exists.

### "Error uploading files"
Check that your Gemini API key is valid and has sufficient quota.

### Rate Limits
Both APIs have rate limits. If you encounter errors:
- For Apify: Check your plan limits
- For Gemini: Wait a few minutes or check your quota

## Cost Considerations

- **Apify**: Free tier includes limited compute units. Check [pricing](https://apify.com/pricing)
- **Gemini API**: Free tier available with rate limits. Check [pricing](https://ai.google.dev/pricing)

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues or questions:
- Check the [Apify documentation](https://docs.apify.com/)
- Check the [Gemini API documentation](https://ai.google.dev/docs)
- Open an issue in this repository
