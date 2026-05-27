# mcp-atlassian 引入报告

生成时间：2026-05-27

## 1. 基本信息

| 字段 | 值 |
|------|-----|
| 包名 | python-mcp-atlassian |
| RPM Name | python3-mcp-atlassian |
| 上游地址 | https://github.com/sooperset/mcp-atlassian |
| 语言 | Python |
| 版本 | 0.13.0 |
| 引入日期 | 2026-05-27 |
| 包类型 | 顶层包 |

## 2. 版本决策

| 检查项 | 结果 |
|--------|------|
| 官方仓库 | 不存在 |
| 用户仓库 | 不存在 |
| 决策 | introduce_new |
| 动作 | built_new |

## 3. 依赖构建摘要

本次引入共构建了 **17 个依赖包**，其中：
- 8 个 compat 包（官方版本太旧，以 compat 包名共存）
- 9 个新建包

| 包名 | 版本 | 类型 |
|------|------|------|
| atlassian-python-api | 4.0.8 | built_new |
| beautifulsoup4 | 4.14.3 | compat (python3-beautifulsoup4-4.14) |
| httpx | 0.28.1 | compat (python3-httpx-0.28) |
| trio | 0.29.0 | compat (python3-trio-0.29) |
| starlette | 1.0.1 | compat (python3-starlette-1.0) |
| urllib3 | 2.7.0 | compat (python3-urllib3-2) |
| python-dateutil | 2.9.0.post0 | compat (python3-python-dateutil-2.9) |
| types-python-dateutil | 2.9.0.20260518 | compat (python3-types-python-dateutil-2.9) |
| keyring | 25.7.0 | compat (python3-keyring-25) |
| markdownify | 1.2.2 | built_new |
| types-cachetools | 7.0.0.20260518 | built_new |
| unidecode | 1.4.0 | built_new |
| truststore | 0.10.4 | built_new |
| fakeredis | 2.34.1 | built_new |
| thefuzz | 0.22.1 | built_new (rapidfuzz via pip) |
| markdown-to-confluence | 0.3.5 | built_new |
| fastmcp | 2.14.7 | built_new |

## 4. RPM 产物

- python3-mcp-atlassian-0.13.0-1.noarch.rpm
- python-mcp-atlassian-help-0.13.0-1.noarch.rpm

## 5. 结论

mcp-atlassian 0.13.0 首次引入成功（built_new），构建耗时较长，需处理大量依赖和版本冲突。
