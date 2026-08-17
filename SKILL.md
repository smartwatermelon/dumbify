---
name: dumbify
version: 0.1.0
description: Rewrite competent workplace writing into terse, lowercase, fragment-heavy engineering communication. Preserve meaning, facts, technical precision, and real uncertainty while aggressively removing ceremony, hedging, articles, connective tissue, and unnecessary words. Optimized for GitHub PRs/comments, Asana tasks, Slack, and similar internal work communication.
license: MIT
---

# Dumbify

Rewrite normal competent work writing into deliberately compressed workplace engineering sludge.

The target is not fake Gen-Z slang. Do not add "no cap", "bestie", "it's giving", emojis, gamer slang, TikTok vocabulary, or deliberate misspellings.

The target is a technically competent person typing very quickly between meetings:

> fewer words. less punctuation. lowercase. fragments. direct.

## Core principle

**Dumbify does not make the thinking dumber. It makes the writing look dumber.**

Preserve the semantic payload. Destroy unnecessary linguistic ceremony.

A good output should sound like something an experienced engineer would actually type into GitHub, Slack, Asana, or an internal ticket when they have 14 seconds to spare.

A bad output sounds like an AI pretending to be a teenager.

## Primary use cases

Optimize especially for:

- GitHub PR descriptions
- GitHub review comments
- GitHub issue comments
- Asana tasks and task descriptions
- Slack / Teams messages
- internal engineering notes
- incident notes
- commit-adjacent prose

For long-form documents, use a lighter touch unless the user explicitly asks for maximum Dumbify.

## Non-negotiable constraints

### Preserve meaning

Never remove or invent:

- facts
- names
- numbers
- dates
- URLs
- identifiers
- technical details
- dependencies
- requested actions
- consequences
- genuine uncertainty
- important qualifications
- security or operational caveats

Compression is linguistic, not semantic.

### Preserve real uncertainty

Remove unnecessary hedging, but do not turn uncertainty into certainty.

Examples:

> I suspect this is a cache issue

→

> probably cache issue

not:

> cache issue

Similarly:

> This may break under concurrent load

→

> may break under load

not:

> breaks under load

The goal is bluntness, not fabrication.

### Rewrite; do not merely substitute words

The output should be a genuine rewrite.

Do not mechanically replace a few words while preserving the original sentence structure. Rebuild the sentence around its semantic payload.

This also means the output should not look like a lightly edited version of the source.

## Process

1. Extract the semantic payload.
2. Identify the actual action, judgment, result, or request.
3. Delete ceremony and framing.
4. Compress syntax.
5. Compress vocabulary.
6. Reduce punctuation and capitalization.
7. Remove unnecessary hedging while preserving real uncertainty.
8. Make the register internally consistent.
9. Run the stupidity audit.
10. Output only the rewritten text unless the user asks for explanation.

## The stupidity audit

Before finalizing, ask:

- can this be shorter without losing information?
- can any article disappear?
- can the subject disappear because the actor is obvious?
- can a clause become a fragment?
- can two sentences become one?
- can one sentence become two shorter fragments?
- is any word present only to sound polite, careful, professional, or educated?
- does this sound like a real engineer typing, rather than an AI trying to sound casual?
- did compression accidentally change the technical meaning?
- did uncertainty become false certainty?
- did I add slang that nobody actually uses at work?

If the answer to "can this be shorter?" is yes, shorten it.

## Register rules

### 1. lowercase by default

Use lowercase for ordinary prose.

Keep capitalization when it carries technical or semantic meaning:

- AWS
- API
- GitHub
- Terraform
- Kubernetes
- PostgreSQL
- HTTP
- TLS
- names
- product names
- proper nouns
- code identifiers

Do not lowercase code, filenames, URLs, commands, identifiers, or quoted material unless the user explicitly asks.

### 2. fragments are preferred

Complete sentences are not required.

Prefer:

> deploy still broken

> fixed cache issue

> needs followup

> works locally

> probably unrelated

> caller already validates this

over polished sentences.

### 3. articles are optional

Aggressively remove:

- the
- a
- an

when the meaning remains obvious.

Examples:

> the deployment pipeline

→

> deploy pipeline

> a problem with the cache

→

> cache issue

> the service cannot connect to the database

→

> service can't connect db

Do not remove articles when doing so creates genuine ambiguity.

### 4. subjects are optional

If the actor is obvious, omit it.

> I updated the config

→

> updated config

> I checked locally and it works

→

> checked locally. works

> We should merge this

→

> should merge

Do not remove the subject when ownership or responsibility matters.

### 5. auxiliary verbs are optional

Drop unnecessary forms of "is", "are", "was", "were", "will", etc.

> tests are passing

→

> tests pass

> this is blocking deploy

→

> blocking deploy

> the service is still failing

→

> service still failing

### 6. connective tissue is expensive

Delete or compress:

- furthermore
- additionally
- however
- therefore
- that said
- in this case
- for this reason
- as a result
- which means
- for context
- just to give some background
- in order to

Examples:

> This changes the timeout, which means requests can now run longer.

→

> timeout bumped. requests run longer

> For context, this happens because the cache is stale.

→

> happens bc cache is stale

### 7. remove social cushioning

Delete unnecessary:

- thanks for flagging this
- I appreciate you taking the time
- I understand the concern
- I'd be happy to
- just wanted to
- I was wondering if
- would you mind
- please don't hesitate to
- hope this helps
- let me know if you'd like

Examples:

> Thanks for catching this. I agree that this could race under load.

→

> yep this races under load

> Would you mind taking a look when you have a chance?

→

> can you look at this

### 8. direct disagreement

Translate diplomatic workplace language into concise, non-hostile statements.

> I don't necessarily agree that this is the best approach.

→

> don't think this is right

> I'm not sure this is the direction I'd take.

→

> wouldn't do this

> I have some concerns about long-term maintainability.

→

> this is gonna suck to maintain

Do not turn disagreement into insults.

### 9. punctuation budget

Default:

- periods: optional
- commas: rare
- semicolons: almost never
- em dashes: never
- en dashes: never
- parentheses: usually delete
- exclamation marks: almost never
- question marks: only for actual questions

Prefer:

> fixed thing. tests pass

over:

> Fixed the thing; the tests are now passing.

Do not strip punctuation from code, commands, URLs, paths, structured data, or quoted material.

### 10. markdown budget

For GitHub, use Markdown when it carries useful structure.

Do not create ornamental structure.

Avoid turning a two-line PR description into a five-section document.

Good:

```markdown
auto-refresh expired auth tokens

fixes requests failing when token expires
```

Also good for a larger change:

```markdown
### what

auto-refresh expired auth tokens

### why

expired token currently nukes request

### tests

unit + integration
```

Bad:

```markdown
## Summary

This pull request introduces...

## Motivation

The motivation behind this change...

## Implementation Details

...
```

Use the smallest structure that makes the information skimmable.

## Vocabulary compression

Use common engineering shorthand when natural.

| Normal | Dumbify |
|---|---|
| configuration | config |
| development | dev |
| production | prod |
| repository | repo |
| documentation | docs |
| environment | env |
| infrastructure | infra |
| deployment | deploy |
| deployment pipeline | deploy pipeline |
| pull request | PR |
| follow-up | followup |
| with | w/ |
| without | w/o |
| versus | vs |
| plus | + |
| approximately | ~ |
| right now | rn |
| as soon as possible | asap |

Do not use internet-slang abbreviations merely to look young.

Avoid:

- u
- ur
- r
- dis
- dat
- no cap
- fr fr
- bestie
- slay
- fire
- based
- it's giving
- 💀
- 🔥
- 🚀

This is **engineering compression**, not adolescent roleplay.

## Vocabulary rules

Prefer nouns and short verbs.

> perform an analysis of

→

> analyze

> make a determination

→

> decide

> provide clarification

→

> clarify

> implement a fix

→

> fix

> utilize

→

> use

> commence

→

> start

> facilitate

→

> help

> leverage

→

> use

> in the event that

→

> if

> at this point in time

→

> now

## Hedging

Remove stacked hedges:

> it seems like it might potentially be

→

> may be

Then, if the uncertainty is weak enough:

> may be

→

> probably

But never remove uncertainty that carries technical meaning.

Examples:

> It might be worth considering whether we should revisit the cache.

→

> maybe redo cache

> I think we should merge this.

→

> should merge

> I suspect this is unrelated.

→

> probably unrelated

## Requests

Turn polite requests into compact requests.

> Could you please update the config and rerun the tests?

→

> update config + rerun tests

> Would you mind checking this before we merge?

→

> can you check this before merge

> I'd appreciate it if you could investigate this.

→

> can you investigate this

Commands should not become hostile.

## Technical register

Keep technical terminology precise.

Do not dumbify:

- API names
- CLI commands
- code
- error messages
- function/class names
- configuration keys
- environment variables
- filenames
- URLs
- version numbers
- protocol names
- standards
- identifiers

Example:

> `kubectl rollout status deployment/foo` still hangs because readiness never succeeds

Do not rewrite that into vague prose.

## GitHub PR mode

PR descriptions should usually answer only:

- what changed
- why
- anything a reviewer needs to know
- tests, if relevant

Example:

Normal:

> This PR introduces a new mechanism for handling expired authentication tokens. Previously, expired tokens would result in a failed request and require the client to reauthenticate manually. With this change, the client will automatically refresh the token when possible, improving the overall reliability of authenticated requests.

Dumbify:

> auto-refresh expired auth tokens instead of failing request + forcing reauth

Do not explain implementation details nobody needs.

### PR review comments

Compress aggressively.

> I think we could simplify this slightly by moving this logic into the existing helper rather than introducing another abstraction here.

→

> can use existing helper here

> I'm wondering if we actually need to handle this case given that the caller already validates the input.

→

> caller already validates this

> Nit: I think this variable name could be a little more descriptive.

→

> nit: name could be clearer

> I don't think this needs to block the PR, but it might be worth addressing at some point.

→

> nonblocking but i'd fix this

> Could we potentially add a test covering this case?

→

> can we test this case

Useful prefixes:

- `nit:` = optional cleanup
- `suggest:` = recommendation
- `blocker:` = blocks approval

Do not add prefixes unless the original meaning warrants them.

## Asana / task mode

Task titles should describe the desired result in the fewest useful words.

> Investigate the intermittent failures we're seeing in the deployment pipeline and determine whether they are related to the recent changes to the caching layer.

→

> investigate intermittent deploy failures. check cache changes

> Update the service configuration to use the new endpoint and verify that the integration tests continue to pass.

→

> update service endpoint + run integration tests

> Review the existing documentation and update it to reflect the new authentication flow.

→

> update auth docs

Avoid turning a simple task into a project plan.

## Slack / chat mode

Prefer short bursts.

Normal:

> I checked the deployment and it looks like the issue is related to the stale cache. I don't think the latest change caused it, but I'll keep digging.

Dumbify:

> checked deploy. stale cache looks likely  
> don't think latest change caused it. digging

For short chat, one or two fragments are often better than a polished paragraph.

## Incident mode

Be especially information-dense.

Prefer:

> prod 5xx up since 14:20. likely db connection exhaustion. rolling back latest deploy

over:

> We're currently seeing an increase in 5xx responses in production, which began around 14:20. The likely cause appears to be database connection exhaustion, so we're going to roll back the latest deployment.

Do not sacrifice timestamps, impact, confidence, or mitigation.

## Intensity levels

Default to **level 2**.

### Level 1: casual

> fixed cache issue. tests pass

### Level 2: work brainrot

> fixed cache. tests green

### Level 3: terminally compressed

> cache fixed. green now

### Level 4: maximum sludge

> cache fixed. green

Level 3 or 4 should only be used when explicitly requested.

Never let higher intensity remove semantic information.

## Failure modes

Do NOT:

### Fake Gen-Z

> no cap this PR is actually fire

### Corporate cosplay

> circling back here

### Acronym soup

> afaict tbh imo we can prob just...

### Deliberate misspellings

> gonna wanna fix dis

### Random emoji

> fixed the bug 🚀

### False certainty

Original:

> I suspect this is a race.

Bad:

> this is a race

Good:

> probably race

### Information loss

Original:

> The timeout increase masks the race but does not fix it.

Bad:

> timeout fixed race

Good:

> timeout hides race. doesn't fix it

## "Stupidity budget"

Dumbify should look intentionally under-polished, but not uniformly stupid.

A useful rule:

- make ordinary prose ugly
- keep technical content crisp
- keep important nouns
- keep meaningful qualifiers
- keep identifiers exact
- never add stupidity where precision is needed

The ideal result is **competent thought expressed with almost offensively little ceremony**.

## Anti-watermark note

Dumbify is a rewriting tool, not a watermark-removal tool.

Its genuine-rewrite behavior may change statistical properties of source text because it reconstructs the wording rather than making local edits. Do not claim that this defeats, removes, or guarantees evasion of any particular AI watermark or detector. Watermark robustness is an empirical property of the specific scheme and detector.

If a user asks to evaluate watermark robustness, treat that as a separate technical experiment and do not make unsupported claims.

## Final rule

Before returning the result, ask:

> **would a competent engineer actually type this, or did an AI try to sound casual?**

If it sounds like the latter, remove the slang and compress the syntax.

The target is not "young."

The target is:

> **busy, technically competent, mildly caffeinated, and completely unwilling to waste a word.**
