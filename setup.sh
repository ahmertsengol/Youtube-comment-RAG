#!/bin/bash

# YouTube Channel RAG Tool Setup Script

echo "=========================================="
echo "YouTube Channel RAG Tool - Setup"
echo "=========================================="
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"
echo ""

# Check if pip3 is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip3."
    exit 1
fi

echo "✅ pip3 found"
echo ""

# Install dependencies
echo "📦 Installing Python dependencies..."
pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo ""
echo "✅ Dependencies installed successfully"
echo ""

# Check for .env file
if [ ! -f ".env" ]; then
    echo "⚠️  .env file not found!"
    echo ""
    echo "Creating .env file from template..."
    cp .env.example .env

    echo "✅ .env file created!"
    echo ""
    echo "⚠️  IMPORTANT: You need to edit the .env file and add your API keys:"
    echo ""
    echo "   1. Get your Gemini API key from:"
    echo "      https://aistudio.google.com/app/apikey"
    echo ""
    echo "   2. Get your Apify API token from:"
    echo "      https://console.apify.com/account/integrations"
    echo ""
    echo "   3. Edit .env file and replace the placeholder values:"
    echo "      nano .env   (or use your favorite editor)"
    echo ""
else
    echo "✅ .env file exists"
    echo ""

    # Check if API keys are set
    if grep -q "your_gemini_api_key_here" .env || grep -q "your_apify_api_token_here" .env; then
        echo "⚠️  WARNING: Your .env file still contains placeholder values!"
        echo "   Please edit .env and add your actual API keys."
        echo ""
    else
        echo "✅ API keys appear to be configured"
        echo ""
    fi
fi

# Create transcripts directory
if [ ! -d "transcripts" ]; then
    mkdir transcripts
    echo "✅ Created transcripts/ directory"
    echo ""
fi

echo "=========================================="
echo "Setup Complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo ""
echo "1. Make sure your API keys are set in .env file"
echo ""
echo "2. Run the tool:"
echo "   python3 main.py"
echo ""
echo "   Or chat with existing transcripts:"
echo "   python3 chat.py"
echo ""
echo "For help, see README.md"
echo ""
