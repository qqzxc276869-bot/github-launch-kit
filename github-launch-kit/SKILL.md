---
name: github-launch-kit
description: "Use this skill when a repository needs to feel launch-ready on GitHub: sharpening the one-line pitch, restructuring the README, improving onboarding clarity, drafting launch copy, and identifying the fastest changes that increase trust, discoverability, and star-worthiness."
---

# GitHub Launch Kit

## Overview

This skill helps Codex turn a technically solid repository into a public-facing open-source project that is easier to understand, easier to try, and easier to share. It focuses on the launch surfaces that affect first impressions: positioning, README quality, activation speed, credibility signals, and community entry points.

Use it when a user wants more GitHub stars, a cleaner launch, a stronger README, or a clearer repo story before posting on GitHub, X, Reddit, Hacker News, Product Hunt, or developer communities.

## What To Inspect First

Read only what is needed to understand the product and its current presentation:

- Root README and any docs linked from it
- Package metadata or app manifests that reveal the product category
- Main entrypoints, demos, examples, screenshots, or recordings if present
- Supporting trust signals such as tests, benchmarks, `LICENSE`, `CONTRIBUTING`, and issue templates

If the product itself is still ambiguous after a quick pass, pause and infer the most likely user, problem, and moment of use before editing launch-facing copy.

## Launch Workflow

### 1. Clarify the actual promise

- Write a plain one-line explanation of what the repo does.
- Identify the primary audience. Prefer one concrete audience over a broad market.
- Name the strongest differentiator. If none is obvious, say that directly instead of inventing one.
- Reject vague claims such as "all-in-one", "revolutionary", or "next-generation" unless the repository proves them.

### 2. Score the first impression

Evaluate the repo on five axes:

1. Clarity: Can a new visitor tell what it is in under 10 seconds?
2. Activation: Can they run, install, or try it quickly?
3. Credibility: Are there demos, benchmarks, screenshots, tests, or real examples?
4. Focus: Does the repo target a clear use case rather than everything at once?
5. Approachability: Does contributing or exploring feel safe for newcomers?

Call out the top three blockers first. Prioritize structural improvements over copy polish when the repo is confusing.

### 3. Improve the high-impact surfaces

When editing or proposing changes, bias toward the surfaces below because they affect discovery and conversion the most:

- Repository name and one-line description
- README opening section
- Install or quickstart path
- Proof section: screenshots, outputs, benchmarks, before/after, live demo
- Example use cases that help users self-identify
- Community surfaces: `CONTRIBUTING`, issue templates, labels, discussion prompts

If the user wants implementation help, do not stop at advice. Draft or edit the actual files.

### 4. Draft launch assets

When asked, produce concise launch-ready assets such as:

- Three tagline options with different tones
- A 120-160 character repository description
- GitHub topic suggestions
- A short X post
- A Hacker News title and summary
- A Reddit post opener
- A release note or launch checklist

Keep launch copy grounded in the repository. Never fake adoption, user counts, sponsorship, or performance claims.

### 5. Be honest about star-worthiness

If the real problem is weak scope, no clear audience, or no proof, say so. A repo often needs better framing, sharper examples, or a narrower promise more than it needs prettier prose.

This skill should help the user earn trust, not simulate traction.

## Default Deliverables

Unless the user asks for something narrower, aim to provide:

1. A sharper one-line pitch
2. A short diagnosis of launch blockers
3. Concrete file edits or proposed file edits
4. Launch copy snippets tailored to the repo
5. A short list of next artifacts to add, such as screenshots or examples

## Reference Files

- For launch scoring and trust signals, read [references/launch-checklist.md](references/launch-checklist.md).
- For README sequencing and section design, read [references/readme-structure.md](references/readme-structure.md).

Load those references only when the task needs more detailed guidance.

## Example Triggers

This skill should trigger for requests like:

- "Help me make this repo look ready for GitHub."
- "Rewrite the README so more people understand it."
- "Prepare this project for an open-source launch."
- "What should I change before posting this on Hacker News?"
- "I want more stars for this repository. Fix the presentation."
