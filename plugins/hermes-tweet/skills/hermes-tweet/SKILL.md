---
name: hermes-tweet
description: Use when a user wants to install or operate Hermes Tweet, the native Hermes Agent X/Twitter plugin for Xquik workflows.
version: 0.1.12
license: MIT
metadata:
  author: Xquik
---

# Hermes Tweet

Use this skill when Claude Code users need Hermes Agent to search, inspect, or
act on X/Twitter through Hermes Tweet.

Xquik is an independent third-party service. Not affiliated with X Corp.
"Twitter" and "X" are trademarks of X Corp.

## Install

Recommended Hermes install:

```bash
hermes plugins install Xquik-dev/hermes-tweet --enable
```

If Hermes discovers the plugin but leaves it disabled, run:

```bash
hermes plugins enable hermes-tweet
```

Configure `XQUIK_API_KEY` on the Hermes runtime host for authenticated reads.
Reload an active CLI or restart gateway and cron sessions after changing the
environment. Do not ask the user to paste API keys into chat.

Confirm registration with `hermes plugins list` and `hermes tools list`.

## Workflow

1. Use `tweet_explore` to discover the catalog route.
2. Use `tweet_read` for catalog-listed, read-only X/Twitter endpoints.
3. Use `tweet_action` only after the user approves a write, private read,
   monitor, webhook, extraction job, giveaway draw, or media operation.
4. Report authentication, policy, or validation failures. Do not retry through
   direct HTTP or guessed routes.

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
- Keep `HERMES_TWEET_ENABLE_ACTIONS=false` unless the user approved the exact
  action and side effects.
