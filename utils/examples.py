"""Example queries and usage patterns for the YouTube RAG tool."""
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

console = Console()


def show_examples():
    """Display example usage and queries."""
    console.print(Panel.fit(
        "[bold cyan]YouTube Channel RAG - Example Queries[/bold cyan]",
        border_style="cyan"
    ))

    examples = """
# Example YouTube Channels to Try

- **Educational**: https://www.youtube.com/@veritasium
- **Tech Reviews**: https://www.youtube.com/@mkbhd
- **Science**: https://www.youtube.com/@kurzgesagt
- **Coding**: https://www.youtube.com/@fireship
- **Business**: https://www.youtube.com/@lexfridman

# Example Questions to Ask

## General Queries
- "What are the main topics covered in these videos?"
- "Summarize all the videos in bullet points"
- "What are the key takeaways from this channel?"

## Specific Topic Search
- "Which videos discuss artificial intelligence?"
- "Find all mentions of Python programming"
- "What did the creator say about climate change?"

## Comparison & Analysis
- "Compare the different approaches mentioned across videos"
- "What are the pros and cons discussed about [topic]?"
- "How has the creator's opinion on [topic] evolved?"

## Content Discovery
- "Which video would be best for learning about [topic]?"
- "Find the most recent video about [subject]"
- "What technical concepts are explained?"

## Quotes & References
- "Find quotes about [keyword]"
- "What sources or studies were mentioned?"
- "List all the tools/products recommended"

# Tips for Better Results

1. **Be Specific**: Instead of "Tell me about the videos", ask "What specific techniques for [topic] are demonstrated?"

2. **Request Citations**: Ask "Which video discusses this?" to get specific references

3. **Follow Up**: Ask follow-up questions to dig deeper into topics

4. **Combine Queries**: "Summarize the main points about [topic] and list any tools mentioned"

# Sample Workflow

```
1. Scrape 10 videos from a tech channel
2. Ask: "What are the main topics?"
3. Pick an interesting topic
4. Ask: "Tell me more about [topic] from the videos"
5. Ask: "Which video covers this in the most detail?"
6. Go watch that specific video with context!
```

# Advanced Usage

## Multiple Sessions
- Keep transcripts in the `transcripts/` folder
- Run `python3 chat.py` to query anytime without re-scraping
- Delete old transcripts with `python3 utils/cleanup.py` before scraping a new channel

## Batch Processing
- Scrape multiple channels (one at a time)
- Compare content across different creators
- Build a knowledge base of your favorite channels

## Integration Ideas
- Use for research: Find expert opinions on topics
- Content creation: Get ideas from successful videos
- Learning: Create study guides from educational channels
"""

    console.print(Markdown(examples))


if __name__ == "__main__":
    show_examples()
