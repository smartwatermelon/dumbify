# Claude Code Infrastructure - Project-Specific

This directory was automatically created by Git template when you initialized or cloned this repository.

## What is this?

The `.claude/` directory provides project-specific configuration for Claude Code CLI (CCCLI) collaboration. It integrates with global infrastructure at `~/.claude/` to provide:

- Project-specific configuration (Node version, required tools, deployment secrets)
- Project-local documentation and patterns

## Directory Structure

```text
.claude/
├── README.md                  # This file
└── config.sh.template         # Template for project configuration
```

## Quick Start

### Option 1: No Additional Configuration Needed

If your project doesn't need special validation, required secrets, or version constraints, **you're done**! Your project already benefits from global infrastructure:

- Global git hooks (pre-commit, pre-push)
- Code review automation
- Branch protection
- Standard workflows

### Option 2: Add Project Configuration

If you need project-specific settings:

1. Copy the template:

   ```bash
   cp .claude/config.sh.template .claude/config.sh
   ```

2. Edit `.claude/config.sh` to define:
   - Required Node version
   - Required tools (EAS, Maestro, jq, etc.)
   - Deployment secrets
   - Custom pre/post build hooks

3. Update your build/deploy scripts to source the config:

   ```bash
   # In build scripts
   source "${HOME}/.claude/lib/build-commons.sh"
   [[ -f ".claude/config.sh" ]] && source ".claude/config.sh"
   run_preflight_checks

   # In deploy scripts
   source "${HOME}/.claude/lib/deploy-commons.sh"
   source ".claude/config.sh"
   verify_cloudflare_secrets "${DEPLOYMENT_REQUIRED_SECRETS[@]}"
   ```

### Option 3: Add Custom Hook Extensions

Project-specific git hook extensions do **not** live in `.claude/`. They live in
`.project-hooks/` at the repository root:

- `.project-hooks/pre-commit` — runs after the global lint pass, before the AI review
- `.project-hooks/pre-push` — same seam for push-time checks

Both must be executable (`chmod +x`). The trust model is the same as any build
tooling: if you cloned the repo and are committing to it, you trust its scripts.

```bash
touch .project-hooks/pre-commit
chmod +x .project-hooks/pre-commit
```

The contract is exit 0 to allow the git operation, exit 1 to block it.

## Common Patterns

### Node.js Project with Version Requirement

```bash
# .claude/config.sh
export REQUIRED_NODE_VERSION="20"
```

### Project with Deployment Secrets

```bash
# .claude/config.sh
export DEPLOYMENT_REQUIRED_SECRETS=(
  "API_KEY"
  "DATABASE_URL"
  "JWT_SECRET"
)
```

### Custom Security Check

```bash
# .project-hooks/pre-commit
#!/usr/bin/env bash

# Block commits with hardcoded API keys
if git diff --cached | grep -iE 'API_KEY.*=.*"[A-Za-z0-9]{32}"'; then
  echo "ERROR: Hardcoded API key detected"
  exit 1
fi

exit 0
```

## Integration with Global Infrastructure

Global hooks at `~/.config/git/hooks/` run the project-local extensions in
`.project-hooks/`. Nothing executes files inside `.claude/` — that directory is
configuration and documentation only.

**Global Infrastructure Documentation**: `~/.claude/docs/INFRASTRUCTURE.md`

## Files Included

### config.sh.template

Template for project configuration. Copy to `config.sh` and customize with your project's requirements.

## Next Steps

1. **Review your needs**: Do you need project-specific configuration or validation?
2. **If yes**: Follow Quick Start Option 2 or 3 above
3. **If no**: You're done! Just start working

## Documentation

- **Global Infrastructure**: `~/.claude/docs/INFRASTRUCTURE.md`
- **Build Patterns**: `~/.claude/docs/BUILD_PATTERNS.md` (if exists)
- **Deployment Patterns**: `~/.claude/docs/DEPLOYMENT_PATTERNS.md` (if exists)
- **Hook System**: `~/.claude/docs/HOOKS.md` (if exists)

## Troubleshooting

### Extensions not running?

```bash
# Check the extension exists at the right path and is executable
ls -la .project-hooks/

# Make executable if needed
chmod +x .project-hooks/pre-commit .project-hooks/pre-push
```

### Config not being used?

```bash
# Verify config exists and is sourced
ls -la .claude/config.sh

# Check your build/deploy scripts source it
grep -r "source.*config.sh" scripts/
```

### Need help?

See global infrastructure documentation at `~/.claude/docs/INFRASTRUCTURE.md` for complete reference.
