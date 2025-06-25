---
description: "Utility for remembering how to call VAN QA rules"
applyTo: "van-qa-utils/rule-calling-help.instructions.md"
---

# VAN QA: HOW TO CALL RULES

> **TL;DR:** This file provides examples and reminders on how to properly call VAN QA rules using the fetch_rules tool.

## 🚨 RULE CALLING SYNTAX

Always use the `fetch_rules` tool with the correct syntax:

```
<function_calls>
<invoke name="fetch_rules">
<parameter name="rule_names">["isolation_rules/visual-maps/rule-name"]
</invoke>
</function_calls>