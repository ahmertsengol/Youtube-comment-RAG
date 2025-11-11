# Third-Party Licenses

This project uses the following third-party libraries and their respective licenses:

## Direct Dependencies

### google-generativeai (>=0.8.0)
- **License**: Apache License 2.0
- **Repository**: https://github.com/google/generative-ai-python
- **Copyright**: Copyright 2023 Google LLC
- **License Text**: See [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)

### apify-client (>=1.7.0)
- **License**: Apache License 2.0
- **Repository**: https://github.com/apify/apify-client-python
- **Copyright**: Copyright 2023 Apify Technologies s.r.o.
- **License Text**: See [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)

### python-dotenv (>=1.0.0)
- **License**: BSD-3-Clause
- **Repository**: https://github.com/theskumar/python-dotenv
- **Copyright**: Copyright (c) 2013-2023, Saurabh Kumar
- **License Text**: See [BSD-3-Clause License](https://opensource.org/licenses/BSD-3-Clause)

### rich (>=13.7.0)
- **License**: MIT License
- **Repository**: https://github.com/Textualize/rich
- **Copyright**: Copyright (c) 2020 Will McGugan
- **License Text**: See [MIT License](https://opensource.org/licenses/MIT)

### cffi (>=1.15.0)
- **License**: MIT License
- **Repository**: https://github.com/python-cffi/cffi
- **Copyright**: Copyright (c) 2013-2023, Armin Rigo, Maciej Fijalkowski
- **License Text**: See [MIT License](https://opensource.org/licenses/MIT)

### youtube-transcript-api (>=0.6.0)
- **License**: MIT License
- **Repository**: https://github.com/jdepoix/youtube-transcript-api
- **Copyright**: Copyright (c) 2020 Jonas Depoix
- **License Text**: See [MIT License](https://opensource.org/licenses/MIT)

## License Compatibility

All dependencies use permissive licenses (MIT, Apache 2.0, BSD-3-Clause) that are compatible with this project's MIT License.

## How to Verify Licenses

To check licenses of installed packages:

```bash
pip install pip-licenses
pip-licenses --with-urls --with-description
```

Or manually check each package:

```bash
pip show <package-name>
```

## License Summary

- **MIT License**: Most permissive, allows commercial use, modification, distribution, private use, and patent use. Requires license and copyright notice.
- **Apache License 2.0**: Similar to MIT but also provides an express grant of patent rights and requires state changes.
- **BSD-3-Clause**: Similar to MIT but includes a non-endorsement clause.

All licenses used in this project are open source and allow commercial use.

