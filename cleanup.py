"""Cleanup utility to remove old transcripts."""
import os
import glob
from rich.console import Console
from rich.prompt import Confirm

console = Console()


def main():
    """Clean up transcript files."""
    console.print("[bold cyan]YouTube RAG Cleanup Tool[/bold cyan]\n")

    # Find transcript files
    transcript_files = glob.glob("transcripts/*.txt")

    if not transcript_files:
        console.print("[yellow]No transcript files found.[/yellow]")
        return

    console.print(f"Found {len(transcript_files)} transcript file(s):\n")

    for i, file_path in enumerate(transcript_files, 1):
        file_size = os.path.getsize(file_path)
        console.print(f"  {i}. {os.path.basename(file_path)} ({file_size:,} bytes)")

    console.print()

    # Ask for confirmation
    if Confirm.ask("Do you want to delete all transcript files?", default=False):
        for file_path in transcript_files:
            try:
                os.remove(file_path)
                console.print(f"✅ Deleted: {os.path.basename(file_path)}")
            except Exception as e:
                console.print(f"❌ Error deleting {file_path}: {e}")

        console.print(f"\n[green]Deleted {len(transcript_files)} file(s)[/green]")
    else:
        console.print("[yellow]Cleanup cancelled[/yellow]")


if __name__ == "__main__":
    main()
