"""Test script to verify all modules can be imported."""
import sys

print("Testing module imports...")

try:
    print("✓ Importing google.generativeai...", end=" ")
    import google.generativeai as genai
    print("OK")
except ImportError as e:
    print(f"FAILED: {e}")
    sys.exit(1)

try:
    print("✓ Importing apify_client...", end=" ")
    from apify_client import ApifyClient
    print("OK")
except ImportError as e:
    print(f"FAILED: {e}")
    sys.exit(1)

try:
    print("✓ Importing dotenv...", end=" ")
    from dotenv import load_dotenv
    print("OK")
except ImportError as e:
    print(f"FAILED: {e}")
    sys.exit(1)

try:
    print("✓ Importing rich...", end=" ")
    from rich.console import Console
    from rich.prompt import Prompt
    print("OK")
except ImportError as e:
    print(f"FAILED: {e}")
    sys.exit(1)

print("\n" + "="*50)
print("All dependencies imported successfully!")
print("="*50)
