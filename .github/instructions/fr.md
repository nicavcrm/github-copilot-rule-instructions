# /fr - Fix Requirements Command

## Purpose
Convert noisy transcript (possibly already /fg-ed) into structured requirements.

## Usage
Type `/fr` followed by your transcript or rough requirements in Copilot Chat.

## Command Contract
- Input: Noisy transcript or rough requirements text
- Output: Structured requirements document in exact order (omit empty sections)

## Required Output Sections (exact order)
1. **Title**
2. **Context**
3. **User Story** (As a [role] I want [capability] so that [benefit].)
4. **Functional Requirements** (bulleted; each starts with a verb)
5. **Non-Functional Requirements**
6. **Assumptions**
7. **Edge Cases**
8. **Open Questions** (only real gaps)
9. **Improvements** (optional enhancements clearly labeled)

## Style Guidelines
- Concise, unambiguous, no marketing fluff
- Do not fabricate details
- Mark uncertainty with (UNCLEAR: ...)
- Preserve intent; never introduce new features beyond transcript hints
- Keep domain-specific terms unchanged
- If transcript is too ambiguous, output "Clarification Needed" section instead

## Error Handling
If the transcript is too ambiguous to proceed, output only:
```
## Clarification Needed
[Brief description of what needs clarification]
```