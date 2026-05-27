# pyright 包引入报告

## 1. 基本信息

| 字段 | 值 |
|------|-----|
| 包名 | pyright |
| 上游地址 | https://github.com/RobertCraigie/pyright-python |
| 语言 | Python |
| 版本 | 1.1.409 |
| 引入日期 | 2026-05-28 |
| 包类型 | 依赖包（depth=1，由 oss-crs 引入） |

## 2. 上游合规

| 字段 | 值 |
|------|-----|
| 平台 | GitHub |
| 活跃度 | 1 天前有更新，活跃 |
| 结论 | 通过 |

## 3. License

license_check.enabled=false，已跳过 License 检查。spec 中声明 `MIT`。

## 4. 版本决策

| 字段 | 值 |
|------|-----|
| 官方仓库 | 不存在 |
| 用户仓库 | 不存在 |
| 决策 | introduce_new |
| 原因 | 官方仓库和用户仓库均无满足要求（1.1.409）的包 |
| 执行动作 | built_new |

## 5. RPM 产物说明

| RPM 包 | 类型 | 用途 |
|--------|------|------|
| python3-pyright-1.1.409-1.noarch.rpm | 主包 | pyright 命令行工具及 Python 库，提供 `pyright`、`pyright-langserver`、`pyright-python`、`pyright-python-langserver` 四个可执行文件 |
| python3-pyright-help | 子包（-help） | 文档包，包含 README.md |
| python-pyright-1.1.409-1.src.rpm | 源码包 | 构建用源码 RPM |

## 6. 归档状态

未归档（`archived: false`）。

## 7. 修复过程摘要

| 轮次 | 修复项 | Oracle 依据 | 结果 |
|------|--------|------------|------|
| Round 1 | 修复 %files：添加缺失的 pyright-python 和 pyright-python-langserver 二进制文件 | rpmbuild 打包阶段文件缺失 | rpmbuild 成功 |
| 退出原因 | PASS（零 E 级问题） | — | — |

round_history 记录 total_rounds=1，exit_reason=pass，rounds 数组为空（Critic 未输出详细轮次记录）。

## 8. 质量反馈

无独立 feedback 文件（依赖包场景，feedback stage 未单独执行）。

根据 spec 和 build_actions 分析：

- 操作合规性：build_actions 仅含两次 `spec_write`（初始生成 + 修复 %files），无源码直接修改，合规。
- spec 结构：使用 `%py3_build` / `%py3_install`，符合 openEuler Python 包惯例。
- `%check` section 存在，注释说明了跳过原因（需网络下载 pyright 二进制，离线构建无法执行），可接受。
- Source0 使用 `%{pypi_source pyright}` 宏，指向 PyPI 不可变版本 tarball，可复现性良好。
- BuildRequires 包含 `python3-nodeenv >= 1.6.0` 和 `python3-typing-extensions >= 4.1`，与运行时 Requires 对齐，合理。

**verdict: acceptable**（无 E 级问题，无明显 W 级问题）

## 9. 新增经验

本次引入为依赖包，feedback stage 未单独执行，无新经验写入 lessons。

## 10. 结论

pyright 1.1.409 作为 oss-crs 的依赖包成功引入，构建一轮通过，spec 质量合格，产物已就绪待归档。
