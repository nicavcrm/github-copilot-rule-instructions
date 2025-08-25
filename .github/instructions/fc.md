# /fc - Fix Cleanup Command

## Purpose
Minimal cleanup (remove filler + obvious misrecognitions) while keeping original phrasing mostly intact.

## Usage
Type `/fc` followed by your raw transcription in Copilot Chat.

## Command Contract
- Input: Raw transcription text
- Output: Cleaned transcript with minimal changes
- Note: Use the copy button in Copilot Chat or select and copy (Ctrl/Cmd+C) to copy the output to clipboard

## Rules
- Remove filler words: uh, um, like, you know (only obvious ones)
- Fix obvious speech recognition errors
- Keep original phrasing and structure mostly intact
- Preserve informal tone and speaking style
- Keep domain-specific terms unchanged unless clearly misspelled
- Do not restructure sentences significantly
- Do not add explanations or commentary
- Replace sensitive tokens with [REDACTED] if present

## What NOT to do
- Do not make major grammatical improvements
- Do not change informal language to formal
- Do not restructure content organization
- Do not add missing information

## Example
Input: `/fc so um we need this system, you know, that can handel the, uh, payment processing for users`
Output: `So we need this system that can handle the payment processing for users`