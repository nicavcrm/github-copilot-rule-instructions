# /fs - Fix Summary Command

## Purpose
Create an executive summary of the provided content.

## Usage
Type `/fs` followed by your content in Copilot Chat. Optionally add "limit: <N>" to specify word count.

## Command Contract
- Input: Content to be summarized
- Output: Executive summary ≤ 120 words (unless user specifies different limit)

## Rules
- Default limit: 120 words
- Custom limit: Use "limit: <N>" syntax (e.g., "/fs limit: 200")
- Focus on: Purpose, scope, key risks/complexity
- Keep domain-specific terms unchanged
- Preserve critical technical details
- Do not add explanations or commentary about the summary process
- Replace sensitive tokens with [REDACTED] if present

## Content Focus Areas
1. **Purpose**: What is being built/achieved
2. **Scope**: What's included and excluded
3. **Key Risks**: Major technical or business risks
4. **Complexity**: Notable technical challenges or dependencies

## Style Guidelines
- Concise, executive-level language
- No marketing fluff
- Clear, actionable insights
- Highlight critical decision points
- Maintain technical accuracy

## Example
Input: `/fs [long technical specification document]`
Output: `System will implement real-time payment processing with fraud detection for e-commerce platform. Scope includes user authentication, transaction management, and third-party gateway integration. Key risks: PCI compliance requirements and high-availability demands during peak traffic. Technical complexity centers on distributed transaction handling and real-time fraud analysis algorithms.`