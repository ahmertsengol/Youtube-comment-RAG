"""Standalone chat interface for querying existing transcripts."""
import os
import sys
import glob
from gemini_rag import GeminiRAG
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.markdown import Markdown

console = Console()


def main():
    """Run the chat interface with existing transcripts."""
    console.print(Panel.fit(
        "[bold cyan]YouTube Transcript Chat[/bold cyan]\n"
        "Chat with your indexed video transcripts",
        border_style="cyan"
    ))

    # Check for .env file
    if not os.path.exists(".env"):
        console.print("\n[yellow]⚠️  No .env file found![/yellow]")
        console.print("Please create a .env file with your GEMINI_API_KEY.")
        sys.exit(1)

    # Check for transcript files
    transcript_files = glob.glob("transcripts/*.txt")
    if not transcript_files:
        console.print("\n[red]❌ No transcript files found in transcripts/ directory[/red]")
        console.print("Please run main.py first to scrape videos.")
        sys.exit(1)

    console.print(f"\n📚 Found {len(transcript_files)} transcript files")

    try:
        # Initialize RAG
        console.print("\n⏳ Loading transcripts into Gemini API...")
        rag = GeminiRAG()
        rag.upload_files(transcript_files)
        rag.initialize_model()

        console.print("\n[bold green]✅ Ready to chat![/bold green]")
        console.print("\n" + "="*60)
        console.print("[bold]Chat Interface[/bold]")
        console.print("Type your questions about the videos. Type 'quit' or 'exit' to end.\n")

        while True:
            try:
                query = Prompt.ask("[bold cyan]You[/bold cyan]")

                if query.lower() in ["quit", "exit", "q"]:
                    console.print("\n[green]Goodbye! 👋[/green]")
                    break

                if not query.strip():
                    continue

                response = rag.chat(query)
                
                # Display response in a beautiful panel with markdown support
                console.print("\n")
                console.print(Panel(
                    Markdown(response),
                    title="[bold green]🤖 AI Assistant[/bold green]",
                    border_style="green",
                    padding=(1, 2),
                    expand=False
                ))
                console.print()  # Empty line for spacing

            except KeyboardInterrupt:
                console.print("\n\n[yellow]Interrupted. Exiting...[/yellow]")
                break
            except Exception as e:
                console.print(f"\n[red]Error: {str(e)}[/red]\n")

    except KeyboardInterrupt:
        console.print("\n\n[yellow]Interrupted. Exiting...[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n[red]❌ Error: {str(e)}[/red]")
        sys.exit(1)


if __name__ == "__main__":
    main()
