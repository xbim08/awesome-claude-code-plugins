---
name: hermes-tweet
description: Use when a user wants to install or operate Hermes Tweet, the native Hermes Agent X/Twitter plugin for Xquik workflows.
---

# Hermes Tweet

Use this skill when Claude Code users need Hermes Agent to search, inspect, or
act on X/Twitter through Hermes Tweet.

## Install

Recommended Hermes install:

```bash
hermes plugins install Xquik-dev/hermes-tweet --enable
```

If Hermes discovers the plugin but leaves it disabled, run:

```bash
hermes plugins enable hermes-tweet
```

Hermes prompts for `XQUIK_API_KEY` during interactive install. In
non-interactive installs, configure it in the Hermes runtime environment or in
`~/.hermes/.env`. Do not ask the user to paste API keys into chat.

## Workflow

1. Use `tweet_explore` to discover the catalog route.
2. Use `tweet_read` for read-only X/Twitter endpoints.
3. Use `tweet_action` only after the user approves a write, private read,
   monitor, webhook, extraction job, giveaway draw, or media operation.

## Good Fits

- Social listening
- Launch monitoring
- Support triage
- Creator or brand research
- Giveaway and community audits
- Controlled publishing with explicit approval

## Safety

- Never request, reveal, or place credentials in tool arguments.
- Never use account connection, re-authentication, API key, billing, credit
  top-up, or support-ticket endpoints.
- Do not guess endpoint paths. Use the catalog returned by `tweet_explore`.
- Summarize any write or private action before calling `tweet_action`.
