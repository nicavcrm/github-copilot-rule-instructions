# /fg - Fix Grammar Command

## Purpose
Correct grammar, spelling, punctuation; remove obvious filler (uh, um, like, you know) that adds no meaning.

## Usage
Type `/fg` followed by your raw transcription text in Copilot Chat.

## Command Contract
- Input: Raw transcription text with grammatical errors, spelling mistakes, and filler words
- Output: ONLY the corrected text. No preface, no suffix.
- Note: Use the copy button in Copilot Chat or select and copy (Ctrl/Cmd+C) to copy the output to clipboard

## Rules
- Keep domain-specific terms unchanged unless clearly misspelled
- Remove obvious filler words: uh, um, like, you know (only when they add no meaning)
- Correct grammar, spelling, and punctuation
- Preserve original intent and meaning
- Do not add explanations or commentary
- Replace sensitive tokens with [REDACTED] if present

## Example
Input: `/fg this is teh systm taht shoud handel paymnt, um, for our users`
Output: `This is the system that should handle payment for our users.`