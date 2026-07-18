# Hermes Tweet

Hermes Tweet is the native Hermes Agent X/Twitter plugin for Xquik workflows.
Use it for social listening, launch monitoring, support triage, creator
research, brand research, giveaway audits, community audits, and controlled
publishing.

## Install

Install this Claude Code guide from the marketplace, then install the Hermes
Agent plugin:

```bash
hermes plugins install Xquik-dev/hermes-tweet --enable
```

Hermes prompts for `XQUIK_API_KEY` during interactive install. For
non-interactive installs, set the key in the Hermes runtime environment or
`~/.hermes/.env` before calling `tweet_read`.

## Safety

- Use `tweet_explore` before any endpoint call.
- Use `tweet_read` for read-only X/Twitter endpoints.
- Use `tweet_action` only after explicit approval.
- Keep `HERMES_TWEET_ENABLE_ACTIONS=false` unless actions are required.
- Never paste credentials or secrets into chat.

Repository: <https://github.com/Xquik-dev/hermes-tweet>
