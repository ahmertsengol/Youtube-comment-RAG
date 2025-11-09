"""Gemini API integration for RAG with file search."""
import os
import time
from typing import List
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()


class GeminiRAG:
    """RAG system using Gemini API with file search."""

    def __init__(self):
        """Initialize Gemini API."""
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")

        genai.configure(api_key=api_key)
        self.model = None
        self.uploaded_files = []

    def upload_files(self, file_paths: List[str]) -> List:
        """
        Upload files to Gemini API.

        Args:
            file_paths: List of file paths to upload

        Returns:
            List of uploaded file objects
        """
        print(f"\n📤 Uploading {len(file_paths)} files to Gemini API...")
        uploaded_files = []

        for file_path in file_paths:
            print(f"⬆️  Uploading: {os.path.basename(file_path)}")
            try:
                uploaded_file = genai.upload_file(
                    path=file_path,
                    display_name=os.path.basename(file_path)
                )
                uploaded_files.append(uploaded_file)
            except Exception as e:
                print(f"❌ Error uploading {file_path}: {e}")

        # Wait for files to be processed
        print("\n⏳ Processing files...")
        for file in uploaded_files:
            while file.state.name == "PROCESSING":
                time.sleep(2)
                file = genai.get_file(file.name)

            if file.state.name == "FAILED":
                print(f"❌ File {file.display_name} failed to process")
            else:
                print(f"✅ {file.display_name} ready")

        self.uploaded_files = uploaded_files
        print(f"\n✅ Successfully uploaded and processed {len(uploaded_files)} files")
        return uploaded_files

    def initialize_model(self):
        """Initialize the Gemini model with file search capabilities."""
        print("\n🤖 Initializing Gemini model with file search...")

        # Create model with files for context
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config={
                "temperature": 0.7,
                "top_p": 0.95,
                "top_k": 40,
                "max_output_tokens": 8192,
            }
        )
        print("✅ Model initialized")

    def chat(self, query: str) -> str:
        """
        Query the RAG system.

        Args:
            query: User question

        Returns:
            Model response
        """
        if not self.model:
            self.initialize_model()

        if not self.uploaded_files:
            return "No files have been uploaded yet. Please upload transcript files first."

        print(f"\n💭 Query: {query}")
        print("🔍 Searching through transcripts...")

        try:
            # Create a prompt that instructs the model to search through the files
            full_prompt = f"""You are a helpful assistant with access to YouTube video transcripts.
Answer the user's question based on the information in the uploaded transcript files.
If the information is not in the transcripts, say so clearly.
Always cite which video(s) you're referencing when possible.

User question: {query}"""

            # Send query with uploaded files as context
            response = self.model.generate_content([full_prompt] + self.uploaded_files)

            return response.text

        except Exception as e:
            return f"❌ Error processing query: {str(e)}"

    def list_files(self) -> List:
        """List all uploaded files."""
        return self.uploaded_files

    def delete_all_files(self):
        """Delete all uploaded files from Gemini API."""
        print("\n🗑️  Deleting uploaded files...")
        for file in self.uploaded_files:
            try:
                genai.delete_file(file.name)
                print(f"✅ Deleted: {file.display_name}")
            except Exception as e:
                print(f"❌ Error deleting {file.display_name}: {e}")

        self.uploaded_files = []
        print("✅ All files deleted")


if __name__ == "__main__":
    # Test the RAG system
    rag = GeminiRAG()

    # Example: upload some files
    import glob
    transcript_files = glob.glob("transcripts/*.txt")

    if transcript_files:
        rag.upload_files(transcript_files)
        rag.initialize_model()

        # Test query
        response = rag.chat("What topics are covered in these videos?")
        print(f"\n💬 Response:\n{response}")
    else:
        print("No transcript files found in transcripts/ directory")
