"""List available Gemini models."""
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# Configure API
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("❌ GEMINI_API_KEY not found in .env")
    exit(1)

genai.configure(api_key=api_key)

print("🔍 Listing all available Gemini models...\n")
print("="*80)

for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(f"\n✅ Model: {model.name}")
        print(f"   Display Name: {model.display_name}")
        print(f"   Description: {model.description}")
        print(f"   Supported Methods: {model.supported_generation_methods}")
        print("-"*80)

print("\n" + "="*80)
print("\nℹ️  Use one of the model names above (e.g., 'models/gemini-pro')")
