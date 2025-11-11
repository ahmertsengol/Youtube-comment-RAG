# Contributing to YouTube Channel RAG Tool

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on constructive feedback
- Respect different viewpoints and experiences

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in [Issues](https://github.com/yourusername/repo/issues)
2. If not, create a new issue using the bug report template
3. Include:
   - Clear description of the bug
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (OS, Python version, etc.)
   - Error messages or logs

### Suggesting Features

1. Check if the feature has already been suggested
2. Create a new issue using the feature request template
3. Describe:
   - The problem the feature would solve
   - Proposed solution
   - Alternative solutions considered
   - Additional context

### Submitting Code Changes

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/repo.git
   cd repo
   ```

2. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

3. **Make your changes**
   - Follow the code style (PEP 8 for Python)
   - Add type hints where appropriate
   - Write docstrings for functions and classes
   - Add comments for complex logic
   - Update documentation if needed

4. **Test your changes**
   ```bash
   python -m tests.test_imports
   python -m tests.test_transcript
   ```

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: Add new feature description"
   # or
   git commit -m "fix: Fix bug description"
   ```

   Use conventional commit messages:
   - `feat:` for new features
   - `fix:` for bug fixes
   - `docs:` for documentation changes
   - `style:` for code style changes
   - `refactor:` for code refactoring
   - `test:` for adding tests
   - `chore:` for maintenance tasks

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Go to the original repository on GitHub
   - Click "New Pull Request"
   - Select your branch
   - Fill out the PR template
   - Wait for review

## Code Style Guidelines

### Python

- Follow PEP 8 style guide
- Use type hints for function parameters and return types
- Maximum line length: 120 characters
- Use descriptive variable and function names
- Write docstrings for all public functions and classes

### Example

```python
def scrape_channel(self, channel_url: str, max_videos: int = 10) -> List[Dict]:
    """
    Scrape video transcripts from a YouTube channel.

    Args:
        channel_url: YouTube channel URL
        max_videos: Maximum number of videos to scrape (newest first)

    Returns:
        List of video data dictionaries with transcripts
    """
    # Implementation
```

## Testing

- Write tests for new features
- Ensure all existing tests pass
- Test edge cases and error conditions
- Update tests when fixing bugs

## Documentation

- Update README.md if adding new features
- Add docstrings to new functions/classes
- Update examples if behavior changes
- Keep CHANGELOG.md updated (if exists)

## Review Process

1. All PRs require at least one approval
2. CI checks must pass
3. Code must follow style guidelines
4. Documentation must be updated
5. Tests must pass

## Questions?

- Open an issue for questions
- Check existing documentation
- Review closed issues/PRs for similar questions

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

Thank you for contributing! 🎉

