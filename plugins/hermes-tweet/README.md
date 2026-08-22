# Hermes Tweet

Hermes Tweet is the native Hermes Agent X/Twitter plugin for Xquik workflows.
Use it for social listening, launch monitoring, support triage, creator
research, brand research, giveaway audits, community audits, and controlled
publishing.

Xquik is an independent third-party service. Not affiliated with X Corp.
"Twitter" and "X" are trademarks of X Corp.

## Install

Install this Claude Code guide from the marketplace, then install the Hermes
Agent plugin:

```bash
hermes plugins install Xquik-dev/hermes-tweet --enable
```

Configure `XQUIK_API_KEY` on the Hermes runtime host before calling
`tweet_read`. Reload the CLI or restart gateway and cron sessions after an
environment change. Never paste the key into chat.

Verify the installation:

```bash
hermes plugins list
hermes tools list
```

`tweet_explore` works without an API key or network call. `tweet_read` appears
after the key is configured. `/xstatus` and `/xtrends` are active-session slash
commands.

## Safety

- Use `tweet_explore` before any endpoint call.
- Use `tweet_read` for read-only X/Twitter endpoints.
- Use `tweet_action` only after explicit approval.
- Keep `HERMES_TWEET_ENABLE_ACTIONS=false` unless actions are required.
- Keep direct HTTP fallbacks disabled. Use catalog-listed routes only.
- Never paste credentials or secrets into chat.

Repository: <https://github.com/Xquik-dev/hermes-tweet>
