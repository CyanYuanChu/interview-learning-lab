---
name: algorithm-visualizer
description: Design or revise self-contained HTML visualizations for interview algorithms and their invariants.
---

# Algorithm Visualizer

Use this skill when an interview algorithm is easier to understand through visible state changes, such as pointers, windows, recursion, queues, or dynamic-programming tables.

## Workflow

1. State the algorithm invariant and the smallest meaningful input.
2. Decide which state must be visible and which controls the learner needs.
3. Build a self-contained HTML page unless the user explicitly asks for a framework or service.
4. Keep the explanation, code idea, and animation state consistent.
5. Verify the shortest user flow: open, start/reset, change an input, and observe the expected state.

## Required behavior

- Explain what each visual state means.
- Make reset and replay deterministic.
- Keep inputs bounded so the visualization remains readable.
- Include keyboard or focus-visible behavior for interactive controls.
- Document local opening, optional HTTP serving, and known verification limits in the app README.

## Scope

This skill creates learning visualizations; it does not replace the algorithm explanation, add a backend, or imply deployment.

## Supporting resources

- Read references/visualization-checklist.md before finalizing a demo.
- Use templates/demo-spec.md to define the state and controls before writing HTML.
