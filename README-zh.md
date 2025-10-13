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
    - [Git 工作流](#Git工作流)
    - [市场营销与增长](#市场营销与增长)
    - [项目与产品管理](#项目与产品管理)
    - [安全、合规与法律](#安全、合规与法律)
* [使用教程](#使用教程)
* [如何贡献](#如何贡献)

## 什么是 Claude Code 插件？

[Claude Code 插件](https://docs.claude.com/en/docs/claude-code/plugins) 是一种轻量级的扩展包，用于自定义并分享你的 Claude Code 开发环境配置。  
每个插件都可以包含以下任意组合：

- **斜杠命令（Slash Commands）** — 为常用操作创建自定义快捷指令  
- **子智能体（Subagents）** — 为特定开发任务构建的专用智能体  
- **MCP 服务器（MCP Servers）** — 通过 Model Context Protocol 将 Claude Code 与外部工具或数据源集成  
- **钩子（Hooks）** — 在关键工作流节点扩展或修改 Claude Code 的行为  

你可以通过 `/plugin` 命令动态安装或禁用插件，从而保持系统上下文的轻量与聚焦。

## 应用场景

- **规范统一：** 确保特定钩子或工作流在团队中一致执行  
- **方便使用：** 将框架或 SDK 的常用命令封装为斜杠命令，简化使用体验  
- **共享工作流：** 发布调试配置、部署脚本或测试工具集  
- **连接工具：** 通过 MCP 服务器安全集成内部系统  
- **组合自定义：** 将多个扩展整合成统一的开发体验  

## 插件列表


### 工作流编排
- [angelos-symbo](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/angelos-symbo)
- [ceo-quality-controller-agent](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/ceo-quality-controller-agent)
- [claude-desktop-extension](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/claude-desktop-extension)
- [lyra](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/lyra)
- [model-context-protocol-mcp-expert](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/model-context-protocol-mcp-expert)
- [problem-solver-specialist](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/problem-solver-specialist)
- [studio-coach](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/studio-coach)
- [ultrathink](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/ultrathink)

### 自动化运维
- [deployment-engineer](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/deployment-engineer)
- [devops-automator](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/devops-automator)
- [infrastructure-maintainer](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/infrastructure-maintainer)
- [monitoring-observability-specialist](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/monitoring-observability-specialist)
- [n8n-workflow-builder](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/n8n-workflow-builder)

### 商务销售
- [b2b-project-shipper](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/b2b-project-shipper)
- [customer-success-manager](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/customer-success-manager)
- [enterprise-onboarding-specialist](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/enterprise-onboarding-specialist)
- [finance-tracker](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/finance-tracker)
- [pricing-packaging-specialist](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/pricing-packaging-specialist)
- [product-sales-specialist](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/product-sales-specialist)
- [support-responder](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/support-responder)
- [technical-sales-engineer](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/technical-sales-engineer)

### 代码质量测试
- [api-tester](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/api-tester)
- [bug-detective](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/bug-detective)
- [code-review](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/code-review)
- [code-review-assistant](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/code-review-assistant)
- [code-reviewer](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/code-reviewer)
- [database-performance-optimizer](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/database-performance-optimizer)
- [debug-session](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/debug-session)
- [debugger](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/debugger)
- [double-check](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/double-check)
- [optimize](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/optimize)
- [performance-benchmarker](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/performance-benchmarker)
- [refractor](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/refractor)
- [test-file](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/test-file)
- [test-results-analyzer](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/test-results-analyzer)
- [test-writer-fixer](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/test-writer-fixer)
- [unit-test-generator](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/unit-test-generator)

### 数据分析
- [analytics-reporter](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/analytics-reporter)
- [data-scientist](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/data-scientist)
- [experiment-tracker](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/experiment-tracker)
- [feedback-synthesizer](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/feedback-synthesizer)
- [trend-researcher](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/trend-researcher)

### 用户体验设计
- [brand-guardian](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/brand-guardian)
- [joker](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/joker)
- [mobile-ux-optimizer](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/mobile-ux-optimizer)
- [onomastophes](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/onomastophes)
- [ui-designer](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/ui-designer)
- [ux-researcher](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/ux-researcher)
- [visual-storyteller](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/visual-storyteller)
- [whimsy-injector](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/whimsy-injector)

### 工程开发
- [ai-engineer](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/ai-engineer)
- [api-integration-specialist](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/api-integration-specialist)
- [backend-architect](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/backend-architect)
- [code-architect](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/code-architect)
- [desktop-app-dev](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/desktop-app-dev)
- [enterprise-integrator-architect](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/enterprise-integrator-architect)
- [flutter-mobile-app-dev](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/flutter-mobile-app-dev)
- [frontend-developer](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/frontend-developer)
- [mobile-app-builder](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/mobile-app-builder)
- [project-curator](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/project-curator)
- [python-expert](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/python-expert)
- [rapid-prototyper](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/rapid-prototyper)
- [react-native-dev](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/react-native-dev)
- [vision-specialist](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/vision-specialist)
- [web-dev](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/web-dev)

### 文档管理
- [analyze-codebase](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/analyze-codebase)
- [changelog-generator](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/changelog-generator)
- [codebase-documenter](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/codebase-documenter)
- [context7-docs-fetcher](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/context7-docs-fetcher)
- [documentation-generator](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/documentation-generator)
- [generate-api-docs](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/generate-api-docs)
- [openapi-expert](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/openapi-expert)
- [update-claudemd](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/update-claudemd)

### Git工作流
- [analyze-issue](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/analyze-issue)
- [bug-fix](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/bug-fix)
- [commit](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/commit)
- [create-pr](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/create-pr)
- [create-pull-request](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/create-pull-request)
- [create-worktrees](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/create-worktrees)
- [fix-github-issue](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/fix-github-issue)
- [fix-issue](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/fix-issue)
- [fix-pr](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/fix-pr)
- [github-issue-fix](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/github-issue-fix)
- [husky](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/husky)
- [pr-issue-resolve](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/pr-issue-resolve)
- [pr-review](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/pr-review)
- [update-branch-name](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/update-branch-name)

### 市场营销与增长
- [app-store-optimizer](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/app-store-optimizer)
- [content-creator](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/content-creator)
- [growth-hacker](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/growth-hacker)
- [instagram-curator](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/instagram-curator)
- [reddit-community-builder](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/reddit-community-builder)
- [tiktok-strategist](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/tiktok-strategist)
- [twitter-engager](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/twitter-engager)

### 项目与产品管理
- [discuss](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/discuss)
- [explore](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/explore)
- [plan](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/plan)
- [planning-prd-agent](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/planning-prd-agent)
- [prd-specialist](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/prd-specialist)
- [project-shipper](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/project-shipper)
- [sprint-prioritizer](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/sprint-prioritizer)
- [studio-producer](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/studio-producer)
- [tool-evaluator](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/tool-evaluator)
- [workflow-optimizer](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/workflow-optimizer)

### 安全、合规与法律
- [ai-ethics-governance-specialist](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/ai-ethics-governance-specialist)
- [audit](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/audit)
- [compliance-automation-specialist](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/compliance-automation-specialist)
- [data-privacy-engineer](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/data-privacy-engineer)
- [enterprise-security-reviewer](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/enterprise-security-reviewer)
- [legal-advisor](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/legal-advisor)
- [legal-compliance-checker](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/legal-compliance-checker)


## 使用教程

你可以使用一个包含 `.claude-plugin/marketplace.json` 文件的 Git 仓库，托管并共享你自己的插件市场（plugin marketplace）。
用户可以通过以下命令添加你的 marketplace：

```bash
# /plugin marketplace add ccplugins/marketplace
/plugin marketplace add user-or-org/repo-name
```

随后即可在 Claude Code 的 `/plugin` 菜单中浏览并安装插件。

示例：

```bash
/plugin
/plugin install analyze-codebase
```


## 如何贡献

欢迎贡献！
你可以：

* 添加你喜欢的插件
* 分享最佳实践
* 提交你自己的插件