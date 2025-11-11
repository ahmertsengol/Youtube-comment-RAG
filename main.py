"""Main script to orchestrate YouTube scraping and RAG setup."""
import os
import sys
from youtube_scraper import YouTubeScraper
from gemini_rag import GeminiRAG
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.panel import Panel
from rich.markdown import Markdown

console = Console()


def main():
    """Main function to orchestrate the YouTube RAG tool."""
    console.print(Panel.fit(
        "[bold cyan]YouTube Channel RAG Tool[/bold cyan]\n"
        "Scrape YouTube videos and chat with transcripts using AI",
        border_style="cyan"
    ))

    # Check for .env file
    if not os.path.exists(".env"):
        console.print("\n[yellow]⚠️  No .env file found![/yellow]")
        console.print("Please create a .env file with your API keys.")
        console.print("See .env.example for the required format.\n")
        sys.exit(1)

    try:
        # Initialize scraper
        console.print("\n[bold]Step 1: YouTube Channel Information[/bold]")
        channel_url = Prompt.ask("🔗 Enter YouTube channel URL")
        max_videos = IntPrompt.ask(
            "📊 How many videos to scrape (newest to oldest)",
            default=10
        )

        # Scrape videos
        console.print("\n[bold]Step 2: Scraping Videos[/bold]")
        scraper = YouTubeScraper()
        videos = scraper.scrape_channel(channel_url, max_videos)

        if not videos:
            console.print("[red]❌ No videos found or scraping failed[/red]")
            sys.exit(1)

        # Save transcripts
        console.print("\n[bold]Step 3: Saving Transcripts[/bold]")
        file_paths = scraper.save_transcripts(videos)

        # Upload to Gemini
        console.print("\n[bold]Step 4: Setting up RAG with Gemini API[/bold]")
        rag = GeminiRAG()
        rag.upload_files(file_paths)
        rag.initialize_model()

        console.print("\n[bold green]✅ Setup Complete![/bold green]")
        console.print(f"📚 Indexed {len(file_paths)} video transcripts")
        console.print("\n[cyan]You can now chat with the video transcripts![/cyan]")

        # Start chat interface
        console.print("\n" + "="*60)
        console.print("[bold]Chat Interface[/bold]")
        console.print("Type your questions about the videos. Type 'quit' or 'exit' to end.\n")

        while True:
            try:
                query = Prompt.ask("[bold cyan]You[/bold cyan]")

                if query.lower() in ["quit", "exit", "q"]:
                    console.print("\n[yellow]Cleaning up...[/yellow]")
                    # Optionally delete files from Gemini
                    # rag.delete_all_files()
                    console.print("[green]Goodbye! 👋[/green]")
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
            except (ValueError, KeyError, TypeError) as e:
                console.print(f"\n[red]Error: {str(e)}[/red]\n")
            except Exception as e:  # noqa: BLE001
                # Catch any other unexpected errors
                console.print(f"\n[red]Error: {str(e)}[/red]\n")

    except KeyboardInterrupt:
        console.print("\n\n[yellow]Interrupted. Exiting...[/yellow]")
        sys.exit(0)
    except (ValueError, KeyError, TypeError, ConnectionError, TimeoutError) as e:
        console.print(f"\n[red]❌ Error: {str(e)}[/red]")
        sys.exit(1)
    except Exception as e:  # noqa: BLE001
        # Catch any other unexpected errors
        console.print(f"\n[red]❌ Unexpected error: {str(e)}[/red]")
        sys.exit(1)


if __name__ == "__main__":
    main()
