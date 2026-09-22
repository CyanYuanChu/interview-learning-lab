---
name: repository-structure-audit
description: Audit a learning repository for directory boundaries, discoverable entrypoints, and reference metadata.
---

# Repository Structure Audit

Use this skill when a repository needs a structure review, a new file classification, or a consistency check before a refactor.

## Workflow

1. Inventory tracked files and top-level directories.
2. Classify each content file as note, reference, skill, app, docs, or tooling.
3. Check that each directory has the expected README or entrypoint.
4. Check skill frontmatter and reference source metadata.
5. Report findings grouped by severity and suggest the smallest safe change.

## Rules

- Treat existing user files as valuable until their role is understood.
- Do not move, delete, or rewrite files automatically; ask for confirmation before destructive cleanup.
- Do not judge a file only by its extension. Follow links and inspect its actual role.
- Keep generated reports separate from the repository unless the user requests a checked-in report.

## Output

Return:

- a concise structure summary;
- misplaced or ambiguous files;
- missing entrypoints or metadata;
- safe next actions;
- checks that were actually run.
