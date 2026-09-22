---
name: hot100-recall
description: Create interview-focused active-recall questions, grading, and weakness reviews from Hot 100 notes.
---

# Hot100 Recall

Use this skill when a user wants to practice, review, grade, or convert an algorithm note into an interview-style recall drill.

## Workflow

1. Identify the topic, question number, and requested mode: quiz, code completion, grading, or weakness review.
2. Read only the requested note and the relevant reference under references/.
3. Build questions around the invariant, state definition, boundary cases, and complexity rather than memorized wording.
4. For grading, separate correctness, reasoning, implementation risk, and interview communication.
5. End with one concrete next-review trigger.

## Output

- Keep each question focused on one decision.
- State the expected invariant or key point separately from the prompt.
- When grading, explain the smallest correction that makes the answer reliable.
- Use the structure in references/review-format.md.

## Scope

- This skill is for technical interview preparation, not a general course generator.
- Do not invent progress, submissions, or personal mistakes that are not present in the supplied material.
- Do not copy external problem statements or official solutions into the result.

## Supporting resources

- Read references/review-format.md when producing a full review.
- Read references/mistake-taxonomy.md when classifying a weakness.
- Use templates/question.md for a reusable question card.
- Use examples/binary-tree-recall.md as a format example only.
