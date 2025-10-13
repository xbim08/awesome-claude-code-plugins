# Awesome Claude Code Plugins [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![English](https://img.shields.io/badge/English-Click-yellow)](README.md)
[![简体中文](https://img.shields.io/badge/简体中文-点击查看-orange)](README-zh.md)

**Awesome Claude Code plugins** —— 精选收录适用于 Claude Code 的 `Slash Commands`、`Subagents`、`MCP Servers` 和 `Hooks` 插件列表。

* [什么是 Claude Code Plugin？](#什么是-claude-code-plugin)
* [使用场景](#使用场景)
* [教程](#教程)
* [如何贡献](#如何贡献)

---

## 什么是 Claude Code Plugin？

[Claude Code Plugin](https://docs.claude.com/en/docs/claude-code/plugins) 是一种轻量级的可扩展包，让你自定义并共享自己的 Claude Code 环境配置。
每个插件可以包含以下任意组合：

* **Slash Commands** — 自定义快捷命令，用于高频操作
* **Subagents** — 针对特定开发任务设计的小型智能体
* **MCP Servers** — 通过 *Model Context Protocol* 集成外部工具与数据源
* **Hooks** — 在 Claude Code 的关键工作流节点插入扩展逻辑

你可以通过 `/plugin` 命令动态安装或禁用插件，从而保持系统上下文的轻量与专注。

---

## 使用场景

* **规范执行标准：** 确保特定 `Hooks` 或工作流在团队中一致运行
* **支持用户：** 打包 `Slash Commands`，简化框架或 SDK 的使用
* **共享工作流：** 发布调试配置、部署脚本或测试框架
* **连接工具：** 通过 `MCP Servers` 安全集成内部系统
* **组合自定义方案：** 将多个扩展组合，打造一致的开发体验

---

## 教程

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