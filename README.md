# Awesome Claude Code Plugins [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![English](https://img.shields.io/badge/English-Click-yellow)](README.md)
[![简体中文](https://img.shields.io/badge/简体中文-点击查看-orange)](README-zh.md)

Awesome Claude Code plugins — a curated list of slash commands, subagents, MCP servers, and hooks for Claude Code

* [What is Claude Code Plugin?](#what-is-claude-code-plugin)
* [Use Cases](#use-cases)
* [Plugins](#plugins)
    - [Workflow & Orchestration](#workflow--orchestration)
    - [Automation & DevOps](#automation--devops)
    - [Business & Sales](#business--sales)
    - [Code Quality & Testing](#code-quality--testing)
    - [Data & Analytics](#data--analytics)
    - [Design & UX](#design--ux)
    - [Development & Engineering](#development--engineering)
    - [Documentation](#documentation)
    - [Git & GitHub Workflow](#git--github-workflow)
    - [Marketing & Growth](#marketing--growth)
    - [Project & Product Management](#project--product-management)
    - [Security, Compliance, & Legal](#security-compliance--legal)
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

## Plugins

### Workflow & Orchestration
- [angelos-symbo](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/angelos-symbo)
- [ceo-quality-controller-agent](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/ceo-quality-controller-agent)
- [claude-desktop-extension](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/claude-desktop-extension)
- [lyra](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/lyra)
- [model-context-protocol-mcp-expert](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/model-context-protocol-mcp-expert)
- [problem-solver-specialist](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/problem-solver-specialist)
- [studio-coach](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/studio-coach)
- [ultrathink](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/ultrathink)

### Automation & DevOps
- [deployment-engineer](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/deployment-engineer)
- [devops-automator](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/devops-automator)
- [infrastructure-maintainer](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/infrastructure-maintainer)
- [monitoring-observability-specialist](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/monitoring-observability-specialist)
- [n8n-workflow-builder](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/n8n-workflow-builder)

### Business & Sales
- [b2b-project-shipper](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/b2b-project-shipper)
- [customer-success-manager](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/customer-success-manager)
- [enterprise-onboarding-specialist](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/enterprise-onboarding-specialist)
- [finance-tracker](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/finance-tracker)
- [pricing-packaging-specialist](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/pricing-packaging-specialist)
- [product-sales-specialist](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/product-sales-specialist)
- [support-responder](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/support-responder)
- [technical-sales-engineer](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/technical-sales-engineer)

### Code Quality & Testing
- [api-tester](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/api-tester)
- [bug-detective](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/bug-detective)
- [code-review](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/code-review)
- [code-review-assistant](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/code-review-assistant)
- [code-reviewer](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/code-reviewer)
- [database-performance-optimizer](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/database-performance-optimizer)
- [debug-session](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/debug-session)
- [debugger](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/debugger)
- [double-check](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/double-check)
- [optimize](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/optimize)
- [performance-benchmarker](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/performance-benchmarker)
- [refractor](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/refractor)
- [test-file](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/test-file)
- [test-results-analyzer](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/test-results-analyzer)
- [test-writer-fixer](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/test-writer-fixer)
- [unit-test-generator](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/unit-test-generator)

### Data & Analytics
- [analytics-reporter](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/analytics-reporter)
- [data-scientist](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/data-scientist)
- [experiment-tracker](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/experiment-tracker)
- [feedback-synthesizer](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/feedback-synthesizer)
- [trend-researcher](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/trend-researcher)

### Design & UX
- [brand-guardian](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/brand-guardian)
- [joker](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/joker)
- [mobile-ux-optimizer](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/mobile-ux-optimizer)
- [onomastophes](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/onomastophes)
- [ui-designer](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/ui-designer)
- [ux-researcher](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/ux-researcher)
- [visual-storyteller](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/visual-storyteller)
- [whimsy-injector](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/whimsy-injector)

### Development & Engineering
- [ai-engineer](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/ai-engineer)
- [api-integration-specialist](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/api-integration-specialist)
- [backend-architect](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/backend-architect)
- [code-architect](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/code-architect)
- [desktop-app-dev](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/desktop-app-dev)
- [enterprise-integrator-architect](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/enterprise-integrator-architect)
- [flutter-mobile-app-dev](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/flutter-mobile-app-dev)
- [frontend-developer](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/frontend-developer)
- [mobile-app-builder](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/mobile-app-builder)
- [project-curator](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/project-curator)
- [python-expert](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/python-expert)
- [rapid-prototyper](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/rapid-prototyper)
- [react-native-dev](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/react-native-dev)
- [vision-specialist](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/vision-specialist)
- [web-dev](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/web-dev)

### Documentation
- [analyze-codebase](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/analyze-codebase)
- [changelog-generator](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/changelog-generator)
- [codebase-documenter](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/codebase-documenter)
- [context7-docs-fetcher](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/context7-docs-fetcher)
- [documentation-generator](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/documentation-generator)
- [generate-api-docs](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/generate-api-docs)
- [openapi-expert](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/openapi-expert)
- [update-claudemd](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/update-claudemd)

### Git & GitHub Workflow
- [analyze-issue](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/analyze-issue)
- [bug-fix](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/bug-fix)
- [commit](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/commit)
- [create-pr](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/create-pr)
- [create-pull-request](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/create-pull-request)
- [create-worktrees](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/create-worktrees)
- [fix-github-issue](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/fix-github-issue)
- [fix-issue](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/fix-issue)
- [fix-pr](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/fix-pr)
- [github-issue-fix](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/github-issue-fix)
- [husky](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/husky)
- [pr-issue-resolve](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/pr-issue-resolve)
- [pr-review](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/pr-review)
- [update-branch-name](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/update-branch-name)

### Marketing & Growth
- [app-store-optimizer](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/app-store-optimizer)
- [content-creator](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/content-creator)
- [growth-hacker](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/growth-hacker)
- [instagram-curator](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/instagram-curator)
- [reddit-community-builder](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/reddit-community-builder)
- [tiktok-strategist](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/tiktok-strategist)
- [twitter-engager](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/twitter-engager)

### Project & Product Management
- [discuss](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/discuss)
- [explore](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/explore)
- [plan](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/plan)
- [planning-prd-agent](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/planning-prd-agent)
- [prd-specialist](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/prd-specialist)
- [project-shipper](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/project-shipper)
- [sprint-prioritizer](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/sprint-prioritizer)
- [studio-producer](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/studio-producer)
- [tool-evaluator](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/tool-evaluator)
- [workflow-optimizer](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/workflow-optimizer)

### Security, Compliance, & Legal
- [ai-ethics-governance-specialist](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/ai-ethics-governance-specialist)
- [audit](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/audit)
- [compliance-automation-specialist](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/compliance-automation-specialist)
- [data-privacy-engineer](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/data-privacy-engineer)
- [enterprise-security-reviewer](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/enterprise-security-reviewer)
- [legal-advisor](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/legal-advisor)
- [legal-compliance-checker](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/legal-compliance-checker)


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