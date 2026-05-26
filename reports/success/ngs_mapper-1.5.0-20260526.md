# ngs_mapper 包引入报告

## 1. 基本信息

| 字段 | 值 |
|------|-----|
| 包名（spec Name） | python-ngs-mapper |
| 上游地址 | https://github.com/VDBWRAIR/ngs_mapper |
| 语言 | Python |
| 版本 | 1.5.0 |
| 引入日期 | 2026-05-26 |
| 包类型 | 顶层包 |
| 引入模式 | built_new |

## 2. 上游合规

| 项目 | 结果 |
|------|------|
| 平台 | GitHub（主流平台） |
| 最近更新 | 2025-03-26（距今 425 天） |
| 活跃度判断 | 通过（未超过阈值） |
| 阻断 | 否 |

> 注：仓库已超过 1 年未更新，处于低维护状态。ngs_mapper 1.5.0 为 Python 2 代码库，上游似乎已停止活跃开发，引入时应在 spec 中注明此背景。

## 3. License

| 项目 | 结果 |
|------|------|
| SPDX 标识符 | GPL-2.0-only（来自 spec） |
| 分类检查 | 已跳过（`license_check.enabled=false`） |
| 阻断 | 否 |

## 4. 版本决策

| 项目 | 结果 |
|------|------|
| 官方仓库（openEuler） | 不存在 |
| 用户仓库（repo-aitest） | 不存在 |
| 决策 | `introduce_new`（官方仓库和用户仓库均无满足要求的包） |
| 执行动作 | `built_new` |

## 5. RPM 产物说明

| RPM 包名 | 类型 | 用途 |
|----------|------|------|
| python3-ngs-mapper-1.5.0-1.noarch.rpm | 主包 | ngs_mapper Python 库及全部命令行工具（is_sanger、runsample、tagreads 等 26 个可执行文件） |
| python-ngs-mapper-help-1.5.0-1.noarch.rpm | -help 子包 | README.rst 和 CHANGELOG.rst 文档 |
| python-ngs-mapper-1.5.0-1.src.rpm | 源码包 | spec 文件 + 上游 tarball，用于构建复现 |

> 主包通过 `Provides: python-ngs-mapper` 和 `Provides: python3dist(ngs-mapper) = 1.5.0` 提供兼容性别名。

## 6. 归档状态

未归档（`archived: false`）。构建产物尚未推送到用户仓库。

## 7. 修复过程摘要

| 轮次 | 修复项 | Oracle 依据 | 结果 |
|------|--------|------------|------|
| Round 1 | 无需修复（首轮即通过） | rpmlint 0E/4W，rpmbuild 成功 | PASS |
| 退出原因 | PASS（零 E 级问题） | — | — |

**W 级警告（不阻断归档）：**

| 位置 | 警告 | 说明 |
|------|------|------|
| spec line 24 | `unversioned-explicit-provides python-ngs-mapper` | 兼容性 Provides 未附版本号，可接受 |
| spec line 36 | `unversioned-explicit-provides python3-ngs-mapper-doc` | 同上 |
| spec header | `no-buildroot-tag` | 现代 RPM 误报，可忽略 |
| %global + %install | 全局禁用 brp-python-bytecompile | Python 2 代码库需禁止 Python 3 字节编译，注释已说明原因，可接受 |

## 8. 质量反馈

**verdict：acceptable**

构建一次通过，rpmlint 零错误。主要注意事项：

- spec `%install` 使用裸 `python3 setup.py install --no-compile --skip-build` 而非 `%py3_install`，配合顶部全局禁用 `brp-python-bytecompile`，是针对 Python 2 遗留代码库的合理处理方式，但全局禁用会影响同 spec 的所有子包，若将来新增纯 Python 3 子包需注意。
- Source0 使用不可变 tag `v1.5.0`，可复现性良好。
- 操作合规性：无违规（无源码直接修改，无绕过 flag）。

## 9. 新增经验

本次构建未产生超出现有 lessons 范围的新经验。

> 参考经验：Python 2 遗留代码库使用 `%py3_build` + `setup.py install --no-compile` 组合时，需在 spec 顶部通过 `%global __os_install_post` 全局抑制 `brp-python-bytecompile`，并在 `%install` 注释中说明原因（避免因 print 语句等 Python 2 语法导致 SyntaxError）。

## 10. 结论

python-ngs-mapper 1.5.0 构建成功，rpmlint 零错误，首轮即通过 review-fix 循环，产物待归档推送到用户仓库。
