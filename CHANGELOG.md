# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-01-11

### Added
- Initial release of YouTube Channel RAG Tool
- YouTube channel video scraping via Apify platform
- Automatic transcript extraction using YouTube Transcript API
- AI-powered content search and chat using Google Gemini API
- Interactive terminal chat interface with markdown support
- Local transcript storage in `transcripts/` directory
- Rich terminal UI with beautiful formatting
- Support for multiple video processing
- Error handling and retry mechanisms
- Comprehensive documentation in Turkish and English
- Test suite for transcript extraction
- Utility scripts for cleanup and debugging
- Environment variable management with `.env` support

### Features
- **Channel Scraping**: Extract video lists from YouTube channels
- **Transcript Extraction**: Automatically fetch transcripts for videos
- **AI Chat**: Interactive chat interface powered by Gemini API
- **RAG System**: Retrieval Augmented Generation for context-aware responses
- **Local Storage**: Transcripts stored locally for offline access
- **Beautiful UI**: Rich terminal interface with colors and formatting

### Documentation
- README.md with quick start guide
- Turkish installation guide (docs/KURULUM.md)
- Quick start guide (docs/QUICKSTART.md)
- Contributing guidelines (CONTRIBUTING.md)
- Comprehensive license information (LICENSE_INFO.md)

### Technical Details
- Python 3.8+ support
- Dependencies: google-generativeai, apify-client, python-dotenv, rich, youtube-transcript-api
- MIT License
- Clean architecture with separated concerns

---

## [Unreleased]

### Planned
- Batch processing improvements
- Export functionality for transcripts
- Enhanced error messages
- Performance optimizations
- Additional AI model support

