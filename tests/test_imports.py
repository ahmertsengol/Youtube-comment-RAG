"""Test script to verify all modules can be imported."""
import sys

print("Testing module imports...")

try:
    print("✓ Importing google.generativeai...", end=" ")
    import google.generativeai as genai  # noqa: F401
    print("OK")
except ImportError as e:
    print(f"FAILED: {e}")
    sys.exit(1)

try:
    print("✓ Importing apify_client...", end=" ")
    from apify_client import ApifyClient  # noqa: F401
    print("OK")
except ImportError as e:
    print(f"FAILED: {e}")
    sys.exit(1)

try:
    print("✓ Importing dotenv...", end=" ")
    from dotenv import load_dotenv  # noqa: F401
    print("OK")
except ImportError as e:
    print(f"FAILED: {e}")
    sys.exit(1)

try:
    print("✓ Importing rich...", end=" ")
    from rich.console import Console  # noqa: F401
    from rich.prompt import Prompt  # noqa: F401
    print("OK")
except ImportError as e:
    print(f"FAILED: {e}")
    sys.exit(1)

print("\n" + "="*50)
print("All dependencies imported successfully!")
print("="*50)
