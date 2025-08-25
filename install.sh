#!/bin/bash

# GitHub Copilot Voice Transcription Commands Installer
# Usage: curl -s https://raw.githubusercontent.com/nicavcrm/github-copilot-rule-instructions/main/install.sh | bash
# Or: ./install.sh

set -e

REPO_URL="https://raw.githubusercontent.com/nicavcrm/github-copilot-rule-instructions/main"
INSTRUCTIONS_DIR=".github/instructions"

echo "🎯 Installing GitHub Copilot Voice Transcription Commands..."

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    echo "⚠️  Warning: Not in a git repository. Installing anyway..."
fi

# Create instructions directory
echo "📁 Creating ${INSTRUCTIONS_DIR} directory..."
mkdir -p "${INSTRUCTIONS_DIR}"

# Download command files
commands=("fg" "fr" "fc" "fe" "fs")

for cmd in "${commands[@]}"; do
    echo "⬇️  Downloading /${cmd} command..."
    if command -v curl &> /dev/null; then
        curl -s -o "${INSTRUCTIONS_DIR}/${cmd}.md" "${REPO_URL}/.github/instructions/${cmd}.md"
    elif command -v wget &> /dev/null; then
        wget -q -O "${INSTRUCTIONS_DIR}/${cmd}.md" "${REPO_URL}/.github/instructions/${cmd}.md"
    else
        echo "❌ Error: Neither curl nor wget is available. Please install one of them."
        exit 1
    fi
    
    if [ -f "${INSTRUCTIONS_DIR}/${cmd}.md" ]; then
        echo "✅ /${cmd} command installed"
    else
        echo "❌ Failed to install /${cmd} command"
        exit 1
    fi
done

echo ""
echo "🎉 Installation complete!"
echo ""
echo "Available commands in GitHub Copilot Chat:"
echo "  /fg  - Fix Grammar (correct spelling, grammar, remove filler)"
echo "  /fr  - Fix Requirements (convert transcript to structured requirements)"
echo "  /fc  - Fix Cleanup (minimal cleanup, preserve original phrasing)"
echo "  /fe  - Fix Expand (expand terse lists into detailed specifications)"
echo "  /fs  - Fix Summary (create executive summary, ≤120 words)"
echo ""
echo "Usage: Type any command in Copilot Chat followed by your text."
echo "Example: /fg this is teh rough transcripshun with erors"
echo ""
echo "📝 Files installed in: ${INSTRUCTIONS_DIR}/"
echo "🔧 Customize the instructions by editing the files in that directory."