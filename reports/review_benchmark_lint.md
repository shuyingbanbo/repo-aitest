# RPM 审查报告 — benchmark @ lint

## 基本信息

| 字段 | 值 |
|------|----|
| 包名 | benchmark |
| 版本 | 1.9.5 |
| 审查阶段 | lint |
| 审查时间 | 2026-05-13 20:58 |
| 审查轮次 | 3 |
| 输入文件 | `/tmp/benchmark.spec` |

---

## 审查结论

**裁决：⚠️ `WARN`**

> 发现 5 个 W 级问题，建议修复，不阻断流程。

---

## 问题清单

### E（必须修复，否则阻断）

_无_

### W（建议修复，不阻断）

| # | 位置 | 问题描述 | 修复建议 |
|---|------|----------|----------|
| 1 | `benchmark.x86_64` | unstripped-binary-or-object /usr/lib64/libbenchmark.so.1.9.5 |  |
| 2 | `benchmark.x86_64` | unstripped-binary-or-object /usr/lib64/libbenchmark_main.so.1.9.5 |  |
| 3 | `benchmark-devel.x86_64` | requires-on-release benchmark(x86-64) = 1.9.5-1 |  |
| 4 | `benchmark-devel.x86_64` | no-major-in-name benchmark-devel |  |
| 5 | `benchmark.x86_64` | no-documentation |  |

### I（信息，无需处理）

| # | 位置 | 说明 |
|---|------|------|
| 1 | `benchmark.x86_64` | no-signature |
| 2 | `benchmark-devel.x86_64` | no-signature |
| 3 | `benchmark-devel.x86_64` | no-library-dependency-for /usr/lib64/libbenchmark.so.1 |
| 4 | `benchmark.x86_64` | missing-hash-section /usr/lib64/libbenchmark.so.1.9.5 |
| 5 | `benchmark.x86_64` | missing-hash-section /usr/lib64/libbenchmark_main.so.1.9.5 |
| 6 | `benchmark.x86_64` | invalid-license Apache-2.0 |
| 7 | `benchmark-devel.x86_64` | invalid-license Apache-2.0 |

---

## 裁决依据

- 无规则违反

## 与上轮对比

| 问题 | 上轮状态 | 本轮状态 |
|------|----------|----------|
| spelling-error ('microbenchmark', '%description -l en_US mic | 已修复 | ✓ 已修复 |
| spelling-error ('Microbenchmark', 'Summary(en_US) Microbench | 已修复 | ✓ 已修复 |
| header-only 库的 -devel 包不应声明 Requires: %{name}（没有主包） | 已修复 | ✓ 已修复 |
| no-documentation | 存在 | W（仍存在） |
| requires-on-release benchmark(x86-64) = 1.9.5-1 | 存在 | W（仍存在） |
| unstripped-binary-or-object /usr/lib64/libbenchmark.so.1.9.5 | 存在 | W（仍存在） |
| unstripped-binary-or-object /usr/lib64/libbenchmark_main.so. | 存在 | W（仍存在） |
| no-major-in-name benchmark-devel | 存在 | W（仍存在） |
| missing-hash-section /usr/lib64/libbenchmark.so.1.9.5 | 存在 | I（仍存在） |
| invalid-license Apache-2.0 | 存在 | I（仍存在） |
| missing-hash-section /usr/lib64/libbenchmark_main.so.1.9.5 | 存在 | I（仍存在） |
| no-library-dependency-for /usr/lib64/libbenchmark.so.1 | 存在 | I（仍存在） |
| no-signature | 存在 | I（仍存在） |

---

_由 review-rpm skill 自动生成_
