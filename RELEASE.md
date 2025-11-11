# Release Guide

This guide explains how to create a new release for this project.

## Pre-Release Checklist

- [ ] All tests pass
- [ ] Documentation is up to date
- [ ] CHANGELOG.md is updated with new version
- [ ] VERSION file is updated
- [ ] README.md version badge is updated
- [ ] No sensitive data in code (API keys, tokens, etc.)
- [ ] All dependencies are up to date
- [ ] License information is complete

## Creating a Release

### Step 1: Update Version

1. Update `VERSION` file with new version number (e.g., `1.0.0`)
2. Update `CHANGELOG.md` with new release notes
3. Update version badge in `README.md` if needed

### Step 2: Commit Changes

```bash
git add VERSION CHANGELOG.md README.md
git commit -m "chore: bump version to 1.0.0"
```

### Step 3: Create Git Tag

```bash
# Create annotated tag
git tag -a v1.0.0 -m "Release version 1.0.0"

# Or create tag with release notes from CHANGELOG
git tag -a v1.0.0 -F CHANGELOG.md
```

### Step 4: Push to Remote

```bash
# Push commits
git push origin main

# Push tags
git push origin v1.0.0
```

### Step 5: Create GitHub Release

1. Go to your GitHub repository
2. Click on "Releases" → "Draft a new release"
3. Select the tag you just created (e.g., `v1.0.0`)
4. Set release title: `v1.0.0` or `Release v1.0.0`
5. Copy release notes from `CHANGELOG.md` for this version
6. Optionally attach release assets (if any)
7. Click "Publish release"

## Release Notes Template

When creating a GitHub release, use this template:

```markdown
## What's New in v1.0.0

### ✨ Features
- Feature 1
- Feature 2

### 🐛 Bug Fixes
- Fix 1
- Fix 2

### 📚 Documentation
- Documentation updates

### 🔧 Improvements
- Improvement 1

---

**Full Changelog**: https://github.com/yourusername/repo/compare/v0.9.0...v1.0.0
```

## Semantic Versioning

This project follows [Semantic Versioning](https://semver.org/):

- **MAJOR** version (1.0.0): Incompatible API changes
- **MINOR** version (0.1.0): New functionality in a backwards compatible manner
- **PATCH** version (0.0.1): Backwards compatible bug fixes

## Automated Release (Optional)

For automated releases, you can use GitHub Actions. Create `.github/workflows/release.yml`:

```yaml
name: Release

on:
  push:
    tags:
      - 'v*'

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Create Release
        uses: actions/create-release@v1
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          tag_name: ${{ github.ref }}
          release_name: Release ${{ github.ref }}
          body_path: CHANGELOG.md
          draft: false
          prerelease: false
```

## Post-Release

After creating a release:

- [ ] Verify release appears on GitHub
- [ ] Check that tag is correct
- [ ] Test installation from release (if applicable)
- [ ] Announce release (social media, blog, etc.)
- [ ] Monitor for issues or feedback

## Current Release: v1.0.0

**Release Date**: 2025-01-11

**Status**: Initial release

See [CHANGELOG.md](CHANGELOG.md) for detailed changes.

