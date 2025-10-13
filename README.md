# Awesome Claude Code Plugins [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![English](https://img.shields.io/badge/English-Click-yellow)](README.md)
[![简体中文](https://img.shields.io/badge/简体中文-点击查看-orange)](README-zh.md)

Awesome Claude Code plugins — a curated list of slash commands, subagents, MCP servers, and hooks for Claude Code

* [What is Claude Code Plugin?](#what-is-claude-code-plugin)
* [Use Cases](#use-cases)
* [Tutorials](#tutorials)
* [Contributing](#contributing)

## What is Claude Code Plugin?

[Claude Code Plugin](https://docs.claude.com/en/docs/claude-code/plugins) is lightweight package that let you customize and share your Claude Code setup.
 Each plugin can include any combination of:

- **Slash Commands** — Custom shortcuts for frequent operations
- **Subagents** — Purpose-built agents for specialized dev tasks
- **MCP Servers** — Integrations to tools and data sources via the Model Context Protocol
- **Hooks** — Extensions that modify Claude Code’s behavior at key workflow points

Install or disable them dynamically with the `/plugin` command — enabling you to keep your system context focused and lightweight.

## Use Cases

- **Enforce Standards:** Ensure specific hooks or workflows run consistently across your team
- **Support Users:** Package slash commands that simplify your framework or SDK usage
- **Share Workflows:** Publish debugging setups, deployment scripts, or testing harnesses
- **Connect Tools:** Integrate internal systems securely through MCP servers
- **Bundle Customizations:** Combine multiple extensions for a cohesive developer experience

## Tutorials

You can host and share your own curated plugin marketplace using a simple Git repository with a `.claude-plugin/marketplace.json` file.
 Users can install your marketplace via:

```bash
# /plugin marketplace add dudley02/awesome-claude-code-plugins
/plugin marketplace add user-or-org/repo-name
```

Then browse and install plugins from within Claude Code’s `/plugin` menu.

Example:

```bash
/plugin
/plugin install analyze-codebase@awesome-claude-code-plugins
```

## Contributing

Contributions are welcome!
 You can add your favorite plugins, share best practices, or submit your own marketplace.