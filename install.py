#!/usr/bin/env python3
"""
GitHub Copilot Voice Transcription Commands Installer
Usage: python install.py
Or: curl -s https://raw.githubusercontent.com/nicavcrm/github-copilot-rule-instructions/main/install.py | python3
"""

import os
import sys
import urllib.request
import urllib.error
from pathlib import Path

REPO_URL = "https://raw.githubusercontent.com/nicavcrm/github-copilot-rule-instructions/main"
INSTRUCTIONS_DIR = ".github/instructions"
COMMANDS = ["fg", "fr", "fc", "fe", "fs"]

def main():
    print("🎯 Installing GitHub Copilot Voice Transcription Commands...")
    
    # Check if we're in a git repository
    if not Path(".git").exists():
        print("⚠️  Warning: Not in a git repository. Installing anyway...")
    
    # Create instructions directory
    instructions_path = Path(INSTRUCTIONS_DIR)
    print(f"📁 Creating {INSTRUCTIONS_DIR} directory...")
    instructions_path.mkdir(parents=True, exist_ok=True)
    
    # Download command files
    success_count = 0
    
    for cmd in COMMANDS:
        print(f"⬇️  Downloading /{cmd} command...")
        
        try:
            url = f"{REPO_URL}/.github/instructions/{cmd}.md"
            file_path = instructions_path / f"{cmd}.md"
            
            with urllib.request.urlopen(url) as response:
                content = response.read().decode('utf-8')
                
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
                
            print(f"✅ /{cmd} command installed")
            success_count += 1
            
        except urllib.error.URLError as e:
            print(f"❌ Failed to download /{cmd} command: {e}")
        except IOError as e:
            print(f"❌ Failed to write /{cmd} command file: {e}")
    
    if success_count == len(COMMANDS):
        print_success_message()
    else:
        print(f"⚠️  Installation completed with errors. {success_count}/{len(COMMANDS)} commands installed.")
        sys.exit(1)

def print_success_message():
    print("""
🎉 Installation complete!

Available commands in GitHub Copilot Chat:
  /fg  - Fix Grammar (correct spelling, grammar, remove filler)
  /fr  - Fix Requirements (convert transcript to structured requirements)
  /fc  - Fix Cleanup (minimal cleanup, preserve original phrasing)
  /fe  - Fix Expand (expand terse lists into detailed specifications)
  /fs  - Fix Summary (create executive summary, ≤120 words)

Usage: Type any command in Copilot Chat followed by your text.
Example: /fg this is teh rough transcripshun with erors

📝 Files installed in: {INSTRUCTIONS_DIR}/
🔧 Customize the instructions by editing the files in that directory.
""")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n❌ Installation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)