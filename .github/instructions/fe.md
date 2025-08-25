# /fe - Fix Expand Command

## Purpose
Expand terse list or shorthand into fuller specification paragraphs/bullets.

## Usage
Type `/fe` followed by your terse list or shorthand notes in Copilot Chat.

## Command Contract
- Input: Terse list, shorthand notes, or brief specifications
- Output: Expanded content with fuller descriptions

## Rules
- Preserve original ordering
- Expand each item into fuller paragraphs or detailed bullets
- Include "Original:" line if rewriting a bullet substantially
- Maintain original intent and scope
- Do not add new features or requirements beyond hints in original
- Keep domain-specific terms unchanged
- Preserve hierarchical structure if present
- Do not add explanations or commentary about the expansion process

## Expansion Guidelines
- Turn keywords into complete sentences
- Add context where implied but not explicit
- Expand abbreviations and shorthand
- Provide more detailed descriptions while staying within scope
- Maintain technical accuracy

## Example
Input: 
```
/fe 
- Auth system
- Payment flow
- User dashboard
```

Output:
```
- Authentication system that handles user login, registration, and session management with secure token-based authentication
- Payment processing flow that integrates with payment gateways to handle transactions, refunds, and payment method management
- User dashboard interface that displays account information, transaction history, and provides access to core application features
```