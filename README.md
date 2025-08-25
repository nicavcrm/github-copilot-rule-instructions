# GitHub Copilot Voice Transcription Commands

A collection of custom GitHub Copilot instructions for refining voice transcriptions into clean, structured content. Perfect for developers who use voice-to-text tools and need to quickly clean up and format their dictated content.

## 🚀 Quick Install

### One-liner installation (recommended)
```bash
curl -s https://raw.githubusercontent.com/nicavcrm/github-copilot-rule-instructions/main/install.sh | bash
```

### Alternative installations
```bash
# Using Python
curl -s https://raw.githubusercontent.com/nicavcrm/github-copilot-rule-instructions/main/install.py | python3

# Manual download
git clone https://github.com/nicavcrm/github-copilot-rule-instructions.git
cd github-copilot-rule-instructions
./install.sh
```

## 📋 Available Commands

| Command | Purpose | Output |
|---------|---------|--------|
| `/fg` | **Fix Grammar** | Clean text with corrected spelling, grammar, and removed filler words |
| `/fr` | **Fix Requirements** | Structured requirements document with user stories and technical specs |
| `/fc` | **Fix Cleanup** | Minimal cleanup preserving original phrasing and informal tone |
| `/fe` | **Fix Expand** | Expanded specifications from terse lists or shorthand notes |
| `/fs` | **Fix Summary** | Executive summary (≤120 words) focusing on purpose, scope, and risks |

## 💡 Usage Examples

### `/fg` - Fix Grammar
**Input:** `/fg this is teh systm taht shoud handel paymnt, um, for our users`  
**Output:** `This is the system that should handle payment for our users.`

### `/fr` - Fix Requirements  
**Input:** `/fr we need voice input cleanup system that can fix transcripts`  
**Output:**
```markdown
## Title
Voice Input Cleanup System

## Context
Need automated transcription refinement for voice-to-text workflows

## User Story
As a developer I want automated transcript cleanup so that I can quickly convert voice input into professional documentation.

## Functional Requirements
- Process raw voice transcripts
- Remove filler words and correct grammar
- Generate structured output formats
- Support multiple cleanup modes

...
```

### `/fc` - Fix Cleanup
**Input:** `/fc so um we need this system, you know, that can handel the, uh, payment processing`  
**Output:** `So we need this system that can handle the payment processing`

### `/fe` - Fix Expand
**Input:** 
```
/fe 
- Auth system
- Payment flow  
- User dashboard
```
**Output:**
```
- Authentication system that handles user login, registration, and session management with secure token-based authentication
- Payment processing flow that integrates with payment gateways to handle transactions, refunds, and payment method management
- User dashboard interface that displays account information, transaction history, and provides access to core application features
```

### `/fs` - Fix Summary
**Input:** `/fs [long technical specification]`  
**Output:** `System implements real-time payment processing with fraud detection for e-commerce platform. Scope includes user authentication, transaction management, and third-party gateway integration. Key risks: PCI compliance requirements and high-availability demands. Technical complexity centers on distributed transaction handling and real-time fraud analysis algorithms.`

## 🔧 How It Works

1. **Install** the command files in your repository's `.github/instructions/` directory
2. **Open** GitHub Copilot Chat in VS Code
3. **Type** any command (`/fg`, `/fr`, `/fc`, `/fe`, `/fs`) followed by your content
4. **Get** instant, formatted output following the command's specific rules

## 📁 What Gets Installed

```
.github/
└── instructions/
    ├── fg.md    # Fix Grammar command
    ├── fr.md    # Fix Requirements command  
    ├── fc.md    # Fix Cleanup command
    ├── fe.md    # Fix Expand command
    └── fs.md    # Fix Summary command
```

## 🎯 Perfect For

- **Voice-driven development** workflows
- **Meeting transcription** cleanup
- **Requirements gathering** from recorded sessions  
- **Documentation** generation from rough notes
- **Spec writing** from brainstorming sessions

## 🔒 Security & Privacy

- Commands replace sensitive tokens with `[REDACTED]` automatically
- No data is sent to external servers beyond GitHub Copilot's normal operation
- All processing happens locally through GitHub Copilot

## 🛠 Customization

After installation, you can customize any command by editing the files in `.github/instructions/`. Each file contains:
- Purpose and usage instructions
- Command contract specifications  
- Processing rules and examples
- Error handling guidelines

## 📚 Technical Details

Based on [GitHub Copilot's custom instructions feature](https://code.visualstudio.com/docs/copilot/copilot-customization), these commands work by providing structured prompts that guide Copilot's behavior for specific tasks.

### Requirements
- VS Code with GitHub Copilot extension
- GitHub Copilot subscription
- Repository with `.github/instructions/` support

### Command Structure
Each command file includes:
- Clear purpose statement
- Usage instructions
- Input/output contracts
- Processing rules
- Example transformations

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-command`)
3. Commit your changes (`git commit -m 'Add amazing command'`)
4. Push to the branch (`git push origin feature/amazing-command`)
5. Open a Pull Request

## 📄 License

MIT License - feel free to use, modify, and distribute.

## 🙋‍♀️ Support

- **Issues**: [GitHub Issues](https://github.com/nicavcrm/github-copilot-rule-instructions/issues)
- **Discussions**: [GitHub Discussions](https://github.com/nicavcrm/github-copilot-rule-instructions/discussions)

---

**Made with ❤️ for developers who think faster than they type**
