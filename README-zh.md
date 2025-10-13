# Awesome Claude Code Plugins [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![English](https://img.shields.io/badge/English-Click-yellow)](README.md)
[![简体中文](https://img.shields.io/badge/简体中文-点击查看-orange)](README-zh.md)

**Awesome Claude Code plugins** —— 精选收录适用于 Claude Code 的 `Slash Commands`、`Subagents`、`MCP Servers` 和 `Hooks` 插件列表。

* [什么是 Claude Code 插件？](#什么是-claude-code-插件)
* [应用场景](#应用场景)
* [插件列表](#插件列表)
    - [工作流编排](#工作流编排)
    - [自动化运维](#自动化运维)
    - [商务销售](#商务销售)
    - [代码质量测试](#代码质量测试)
    - [数据分析](#数据分析)
    - [设计与用户体验](#用户体验设计)
    - [工程开发](#工程开发)
    - [文档管理](#文档管理)
    - [Git与GitHub工作流](#Git与GitHub工作流)
    - [市场营销与增长](#市场营销与增长)
    - [项目与产品管理](#项目与产品管理)
    - [安全、合规与法律](#安全、合规与法律)
* [使用教程](#使用教程)
* [如何贡献](#如何贡献)

## 什么是 Claude Code 插件？

[Claude Code 插件](https://docs.claude.com/en/docs/claude-code/plugins) 是一种轻量级的可扩展包，让你自定义并共享自己的 Claude Code 环境配置。
每个插件可以包含以下任意组合：

* **Slash Commands** — 自定义快捷命令，用于高频操作
* **Subagents** — 针对特定开发任务设计的小型智能体
* **MCP Servers** — 通过 *Model Context Protocol* 集成外部工具与数据源
* **Hooks** — 在 Claude Code 的关键工作流节点插入扩展逻辑

你可以通过 `/plugin` 命令动态安装或禁用插件，从而保持系统上下文的轻量与专注。

## 应用场景

* **规范执行标准：** 确保特定 `Hooks` 或工作流在团队中一致运行
* **支持用户：** 打包 `Slash Commands`，简化框架或 SDK 的使用
* **共享工作流：** 发布调试配置、部署脚本或测试框架
* **连接工具：** 通过 `MCP Servers` 安全集成内部系统
* **组合自定义方案：** 将多个扩展组合，打造一致的开发体验


## 插件列表


### 工作流编排
- [angelos-symbo](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/angelos-symbo)
- [ceo-quality-controller-agent](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/ceo-quality-controller-agent)
- [claude-desktop-extension](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/claude-desktop-extension)
- [lyra](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/lyra)
- [model-context-protocol-mcp-expert](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/model-context-protocol-mcp-expert)
- [problem-solver-specialist](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/problem-solver-specialist)
- [studio-coach](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/studio-coach)
- [ultrathink](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/ultrathink)

### 自动化运维
- [deployment-engineer](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/deployment-engineer)
- [devops-automator](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/devops-automator)
- [infrastructure-maintainer](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/infrastructure-maintainer)
- [monitoring-observability-specialist](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/monitoring-observability-specialist)
- [n8n-workflow-builder](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/n8n-workflow-builder)

### 商务销售
- [b2b-project-shipper](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/b2b-project-shipper)
- [customer-success-manager](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/customer-success-manager)
- [enterprise-onboarding-specialist](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/enterprise-onboarding-specialist)
- [finance-tracker](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/finance-tracker)
- [pricing-packaging-specialist](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/pricing-packaging-specialist)
- [product-sales-specialist](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/product-sales-specialist)
- [support-responder](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/support-responder)
- [technical-sales-engineer](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/technical-sales-engineer)

### 代码质量测试
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

### 数据分析
- [analytics-reporter](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/analytics-reporter)
- [data-scientist](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/data-scientist)
- [experiment-tracker](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/experiment-tracker)
- [feedback-synthesizer](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/feedback-synthesizer)
- [trend-researcher](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/trend-researcher)

### 用户体验设计
- [brand-guardian](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/brand-guardian)
- [joker](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/joker)
- [mobile-ux-optimizer](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/mobile-ux-optimizer)
- [onomastophes](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/onomastophes)
- [ui-designer](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/ui-designer)
- [ux-researcher](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/ux-researcher)
- [visual-storyteller](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/visual-storyteller)
- [whimsy-injector](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/whimsy-injector)

### 工程开发
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

### 文档管理
- [analyze-codebase](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/analyze-codebase)
- [changelog-generator](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/changelog-generator)
- [codebase-documenter](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/codebase-documenter)
- [context7-docs-fetcher](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/context7-docs-fetcher)
- [documentation-generator](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/documentation-generator)
- [generate-api-docs](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/generate-api-docs)
- [openapi-expert](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/openapi-expert)
- [update-claudemd](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/update-claudemd)

### Git与GitHub工作流
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

### 市场营销与增长
- [app-store-optimizer](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/app-store-optimizer)
- [content-creator](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/content-creator)
- [growth-hacker](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/growth-hacker)
- [instagram-curator](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/instagram-curator)
- [reddit-community-builder](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/reddit-community-builder)
- [tiktok-strategist](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/tiktok-strategist)
- [twitter-engager](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/twitter-engager)

### 项目与产品管理
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

### 安全、合规与法律
- [ai-ethics-governance-specialist](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/ai-ethics-governance-specialist)
- [audit](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/audit)
- [compliance-automation-specialist](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/compliance-automation-specialist)
- [data-privacy-engineer](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/data-privacy-engineer)
- [enterprise-security-reviewer](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/enterprise-security-reviewer)
- [legal-advisor](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/legal-advisor)
- [legal-compliance-checker](https://github.com/dudley02/awesome-claude-code-plugins/tree/main/plugins/legal-compliance-checker)


## 使用教程

你可以使用一个包含 `.claude-plugin/marketplace.json` 文件的 Git 仓库，托管并共享你自己的插件市场（plugin marketplace）。
用户可以通过以下命令添加你的 marketplace：

```bash
# /plugin marketplace add dudley02/awesome-claude-code-plugins
/plugin marketplace add user-or-org/repo-name
```

随后即可在 Claude Code 的 `/plugin` 菜单中浏览并安装插件。

示例：

```bash
/plugin
/plugin install analyze-codebase@awesome-claude-code-plugins
```

---

## 如何贡献

欢迎贡献！
你可以：

* 添加你喜欢的插件
* 分享最佳实践
* 提交你自己的插件