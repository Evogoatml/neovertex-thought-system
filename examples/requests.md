# Example control panels

Append one of these control sets to a task, or use the CLI flags to generate a full prompt.

## Quick bug fix

```text
MODE: quick
HARDENING: 1
OUTPUT: minimal

Fix this bug and show the corrected code: ...
```

## Adversarial review

```text
MODE: adversarial
HARDENING: 3
OUTPUT: full

Review this API design for abuse cases and failure modes: ...
```

## System design

```text
MODE: system_design
HARDENING: 2
OUTPUT: structured
THINK_DEPTH: 4

Design a job processing service for ...
```
