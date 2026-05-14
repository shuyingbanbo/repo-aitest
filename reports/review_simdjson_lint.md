# RPM 审查报告 — simdjson @ lint

## 基本信息

| 字段 | 值 |
|------|----|
| 包名 | simdjson |
| 版本 | 4.6.4 |
| 审查阶段 | lint |
| 审查时间 | 2026-05-14 10:01 |
| 审查轮次 | 1 |
| 输入文件 | `/root/.claude/skills/rpm-repo-github/simdjson/simdjson.spec` |

---

## 审查结论

**裁决：⚠️ `WARN`**

> 发现 3 个 W 级问题，建议修复，不阻断流程。

---

## 问题清单

### E（必须修复，否则阻断）

_无_

### W（建议修复，不阻断）

| # | 位置 | 问题描述 | 修复建议 |
|---|------|----------|----------|
| 1 | `simdjson.spec` | no-buildroot-tag |  |
| 2 | `simdjson.spec` | no-%check-section |  |
| 3 | `simdjson.spec` | invalid-url Source0: simdjson-4.6.4.tar.gz |  |

### I（信息，无需处理）

_无_

---

## 裁决依据

- 无规则违反

---

_由 review-rpm skill 自动生成_
