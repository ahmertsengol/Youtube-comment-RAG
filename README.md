# YouTube Channel RAG Tool

A RAG (Retrieval Augmented Generation) tool that scrapes YouTube channel videos, extracts transcripts, and enables AI-powered chat interactions using Google's Gemini API.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Gemini API](https://img.shields.io/badge/Gemini-API-orange.svg)](https://ai.google.dev/)

## Features

- Extract video lists from YouTube channels using Apify
- Automatically fetch transcripts using free YouTube Transcript API
- AI-powered content search with Gemini API
- Interactive terminal chat interface with markdown support
- Local transcript storage

## Quick Start

### Prerequisites

- Python 3.8+
- [Gemini API key](https://aistudio.google.com/app/apikey)
- [Apify API token](https://console.apify.com/account/integrations) (only for channel scraping)

### Installation

```bash
# Clone repository
git clone <repo-url>
cd Youtube-comment-RAG

# Install dependencies
pip install -r requirements.txt

# Configure API keys
cp .env.example .env
# Edit .env and add your API keys
```

### Usage

**Scrape videos and chat:**
```bash
python main.py
```

**Chat with existing transcripts:**
```bash
python chat.py
```

**Test single video (no Apify needed):**
```bash
python -m tests.test_transcript
```

## Example Questions

- "What are the main topics covered in these videos?"
- "What did the creator say about [topic]?"
- "Which videos mention [keyword]?"
- "Compare approaches discussed in different videos"

## Project Structure

```
├── main.py              # Main orchestration script
├── chat.py              # Standalone chat interface
├── youtube_scraper.py  # Transcript extraction
├── gemini_rag.py       # Gemini API integration
├── tests/              # Test files
├── utils/              # Utility scripts
└── docs/               # Documentation
```

## License

MIT License - see [LICENSE](LICENSE) file for details.

For complete license and legal information including third-party licenses, see [LICENSE_INFO.md](LICENSE_INFO.md).

## Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Support

- [Documentation](docs/)
- [Report Issues](https://github.com/yourusername/repo/issues)
- [Apify Docs](https://docs.apify.com/)
- [Gemini API Docs](https://ai.google.dev/docs)
