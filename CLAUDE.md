# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Dumbify is a single-artifact agent skill: a prompt, not a program. There is no
build, no test suite, no lint step, no dependencies, and no executable code.
The entire runtime artifact is `SKILL.md`; everything else is packaging.

- `SKILL.md` — the skill. YAML frontmatter (`name`, `version`, `description`,
  `license`) followed by the instruction body. Consumed verbatim by Claude Code
  and any other Markdown-skill harness.
- `README.md` — human-facing install/usage docs.
- `.claude/` — this repo's own Claude Code config, unrelated to the skill's content.

Verification is by reading and by trying the skill on sample text, not by
running anything.

## Editing SKILL.md

The frontmatter `description` is what the harness matches against to decide
whether to load the skill, so it is load-bearing prose, not a summary — changing
it changes when Dumbify fires.

The body is organized as layered constraints, and the ordering matters to how
the model resolves conflicts:

1. **Core principle** — "makes the writing look dumber, not the thinking."
2. **Non-negotiable constraints** — preserve meaning, preserve real uncertainty,
   genuinely rewrite rather than word-substitute. These override everything below.
3. **Process** (10 steps) and the **stupidity audit** (a self-check list run
   before output).
4. **Register rules** (10 numbered rules: lowercase, fragments, articles,
   subjects, auxiliaries, connectives, social cushioning, disagreement,
   punctuation, markdown).
5. **Mode sections** — GitHub PR, PR review comments, Asana/task, Slack, incident.
   These specialize the register rules per surface.
6. **Intensity levels 1–4**, default 2; 3–4 only on explicit request.
7. **Failure modes** — the negative space, defining what Dumbify must not become.

When adding a rule, put it at the layer that matches its precedence and follow
the existing shape: a short imperative, then before/after examples in blockquotes
(`> normal` / `→` / `> dumbified`). Examples carry more weight than explanation
here — prefer adding one over adding a paragraph.

Two invariants that most proposed edits threaten:

- **Compression is linguistic, never semantic.** Any rule that could drop a fact,
  number, identifier, caveat, or genuine hedge is wrong regardless of how much
  shorter it makes the output.
- **The target register is a busy engineer, not a teenager.** Slang, emoji,
  deliberate misspellings, and acronym soup are explicitly enumerated failure
  modes. Do not soften those prohibitions.

Keep `README.md`'s examples and the intensity-level description consistent with
`SKILL.md` when either changes.

## Watermarks

The repo takes a deliberate, non-negotiable position: Dumbify is not a
watermark-removal tool, and no claim may be made that it defeats or evades any
detector. Both `SKILL.md` and `README.md` state this. Do not weaken, hedge, or
remove that framing.
