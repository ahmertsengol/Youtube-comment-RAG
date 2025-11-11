# License and Legal Information

This file contains all license and legal information for the project.

## Project License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for the full license text.

### Copyright

Copyright (c) 2025 YouTube Channel RAG Tool Contributors

All rights reserved.

---

## Third-Party Libraries and Licenses

This project uses the following third-party libraries:

### Direct Dependencies

#### google-generativeai (>=0.8.0)
- **License**: Apache License 2.0
- **Purpose**: Google Gemini API integration
- **Repository**: https://github.com/google/generative-ai-python
- **Copyright**: Copyright 2023 Google LLC
- **License Text**: [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)

#### apify-client (>=1.7.0)
- **License**: Apache License 2.0
- **Purpose**: YouTube channel scraping via Apify platform
- **Repository**: https://github.com/apify/apify-client-python
- **Copyright**: Copyright 2023 Apify Technologies s.r.o.
- **License Text**: [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)

#### python-dotenv (>=1.0.0)
- **License**: BSD-3-Clause
- **Purpose**: Environment variable management
- **Repository**: https://github.com/theskumar/python-dotenv
- **Copyright**: Copyright (c) 2013-2023, Saurabh Kumar
- **License Text**: [BSD-3-Clause License](https://opensource.org/licenses/BSD-3-Clause)

#### rich (>=13.7.0)
- **License**: MIT License
- **Purpose**: Beautiful terminal UI and formatting
- **Repository**: https://github.com/Textualize/rich
- **Copyright**: Copyright (c) 2020 Will McGugan
- **License Text**: [MIT License](https://opensource.org/licenses/MIT)

#### cffi (>=1.15.0)
- **License**: MIT License
- **Purpose**: C Foreign Function Interface (dependency)
- **Repository**: https://github.com/python-cffi/cffi
- **Copyright**: Copyright (c) 2013-2023, Armin Rigo, Maciej Fijalkowski
- **License Text**: [MIT License](https://opensource.org/licenses/MIT)

#### youtube-transcript-api (>=0.6.0)
- **License**: MIT License
- **Purpose**: Free YouTube transcript extraction
- **Repository**: https://github.com/jdepoix/youtube-transcript-api
- **Copyright**: Copyright (c) 2020 Jonas Depoix
- **License Text**: [MIT License](https://opensource.org/licenses/MIT)

### License Compatibility

All dependencies use permissive licenses (MIT, Apache 2.0, BSD-3-Clause) that are compatible with this project's MIT License.

### License Summary

- **MIT License**: Most permissive, allows commercial use, modification, distribution, private use, and patent use. Requires license and copyright notice.
- **Apache License 2.0**: Similar to MIT but also provides an express grant of patent rights and requires state changes.
- **BSD-3-Clause**: Similar to MIT but includes a non-endorsement clause.

All licenses used in this project are open source and allow commercial use.

### Verifying Licenses

To check licenses of installed packages:

```bash
pip install pip-licenses
pip-licenses --with-urls --with-description
```

Or manually check each package:

```bash
pip show <package-name>
```

---

## Service Terms of Use

### YouTube API Usage

This tool uses YouTube's public transcript endpoints. Users must comply with:
- [YouTube Terms of Service](https://www.youtube.com/static?template=terms)
- [YouTube API Services Terms of Service](https://developers.google.com/youtube/terms/api-services-terms-of-service)

**Important**: This tool is not affiliated with, endorsed by, or connected to YouTube or Google.

### Google Gemini API Usage

Users must comply with:
- [Google AI Terms of Service](https://ai.google.dev/terms)
- [Google Privacy Policy](https://policies.google.com/privacy)

### Apify Platform Usage

Users must comply with:
- [Apify Terms of Service](https://apify.com/terms)
- [Apify Privacy Policy](https://apify.com/privacy)

---

## Disclaimer

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.

The authors and contributors are not responsible for:
- Any misuse of this software
- Violations of third-party terms of service
- Data accuracy or completeness
- Service availability or API rate limits
- Any damages resulting from the use of this software

---

## Data Privacy

- This tool processes publicly available YouTube video transcripts
- No personal data is collected or stored
- API keys are stored locally in `.env` file and never shared
- Transcripts are stored locally in `transcripts/` directory
- Data is transmitted to the following third parties:
  - YouTube (for transcript retrieval)
  - Google Gemini API (for AI processing)
  - Apify (for channel scraping)

---

## User Responsibilities

Users are responsible for:
- Ensuring compliance with all applicable terms of service
- Obtaining necessary API keys and tokens
- Respecting rate limits and quotas
- Using the tool in accordance with applicable laws
- Not using the tool for illegal or unauthorized purposes

---

## Intellectual Property

- **Project code**: MIT License (see LICENSE file)
- **Third-party libraries**: See section above
- **YouTube content**: Copyright of respective content creators
- **Google Gemini API**: Subject to Google's terms

---

## Attribution and Acknowledgments

This project uses the following services and APIs:

- **Google Gemini API**: For AI-powered content search and chat
  - Terms: https://ai.google.dev/terms
  - Privacy: https://policies.google.com/privacy

- **Apify Platform**: For YouTube channel scraping
  - Terms: https://apify.com/terms
  - Privacy: https://apify.com/privacy

- **YouTube Transcript API**: Free transcript extraction
  - No official API, uses public YouTube endpoints
  - Respects YouTube's Terms of Service

Special thanks to:
- **youtube-transcript-api** developers for providing a free transcript extraction solution
- **Google Gemini** team for the powerful AI API
- **Apify** for the YouTube scraping infrastructure
- **Rich** library developers for beautiful terminal UI
- All open-source contributors whose work made this project possible

---

## Contact

For legal questions or concerns:
- Open an issue in the repository
- Contact the project maintainers

---

## Changes to Legal Terms

This legal information may be updated. Users should review this document periodically.

Last updated: 2025-01-11
