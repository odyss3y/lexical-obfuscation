# Obfuscator Project Instructions

## Project posture
This repository contains obfuscation-related tooling. Treat correctness, reversibility, and auditability as more important than clever transformations or broad rewrites.

Do not make opportunistic refactors. Do not rename public interfaces, CLI flags, config keys, output formats, or file layouts unless explicitly asked.

## Security and ethics boundaries
Assume the intended use is defensive, research, testing, compatibility, or controlled transformation work.

Do not add stealth, persistence, credential theft, evasion of security products, unauthorized access, malware deployment, or anti-forensics behavior.

If a requested change could make the tool meaningfully more useful for abuse, pause and explain the concern. Prefer safer alternatives such as test fixtures, toy examples, static analysis, reversible transforms, or documentation.

## Workflow
Before editing, inspect:
- repository layout
- README / docs
- config files
- build/test commands
- current Git status
- relevant source files

Prefer small, reviewable patches. Show the intended diff before applying broad changes.

After any edit, report:
- files changed
- reason for each change
- commands run
- test results
- remaining risks
- rollback instructions

## Testing
Prefer existing tests and project-native tooling. Do not invent a new test framework unless explicitly asked.

If tests are absent, identify the smallest useful validation path before changing code.

For obfuscation logic, preserve before/after examples where practical.

## Git behavior
Never commit, push, rebase, reset, stash, discard changes, or rewrite history unless explicitly asked.

Always preserve user changes. If the working tree is dirty, identify existing changes before making new ones.

## Style
Keep changes minimal and local. Match the existing code style.

Avoid large dependency changes, formatting-only diffs, or generated-file churn unless the task explicitly requires it.
