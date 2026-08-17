# Dumbify

An agent skill that rewrites competent workplace writing into terse, lowercase, fragment-heavy engineering communication.

Dumbify is designed for GitHub PR descriptions and review comments, Asana tasks, Slack / Teams, incident notes, and similar internal work communication.

The core idea:

> dumbify does not make the thinking dumber. it makes the writing look dumber.

The target is not fake Gen-Z slang. It is compressed engineering communication: fewer words, less punctuation, lowercase, fragments, direct statements, preserved technical precision.

## Installation

### Claude Code plugin

If this repository is added as a Claude Code marketplace, install it with:

```text
/plugin marketplace add smartwatermelon/dumbify
```

The runtime artifact is `SKILL.md`.

### Claude Code, project-local

```bash
mkdir -p .claude/skills/dumbify
cp SKILL.md .claude/skills/dumbify/
```

### Claude Code, global

```bash
mkdir -p ~/.claude/skills/dumbify
cp SKILL.md ~/.claude/skills/dumbify/
```

### Any other harness

Copy `SKILL.md` into the location used by the target tool for Markdown-based skills, or provide its contents as system/developer instructions.

## Usage

Ask for it directly:

```text
Dumbify this: [paste text]
```

Or point it at a file when the harness supports file-aware skills.

## Examples

**Input**

> I think we should probably update the Terraform module before merging this because the current version has a race condition during deployment.

**Output**

> update terraform module before merge. current version races during deploy

**Input**

> Thanks for catching this. I agree that the caller already validates the input, so I don't think we need to handle this case here.

**Output**

> yep caller already validates this. don't need handle here

**Input**

> Would you mind taking a look at the intermittent deployment failures and checking whether they're related to the recent cache changes?

**Output**

> can you check intermittent deploy failures + cache changes

## Intensity

Default is level 2. The skill supports levels 1–4, with higher levels producing increasingly compressed output.

Level 3 or 4 should be explicitly requested.

## Watermarks

Dumbify is not advertised as a watermark-removal mechanism. Any change to watermark detectability is an empirical property of the watermarking system and must be tested rather than assumed.

## License

MIT. See [LICENSE](LICENSE).
