# publicsuffix 包引入报告

## 1. 基本信息

| 字段 | 值 |
|------|-----|
| 包名 | rust-publicsuffix |
| 上游地址 | https://github.com/rushmorem/publicsuffix |
| 语言 | Rust |
| 版本 | 1.5.4~alpha.0 |
| 引入日期 | 2026-05-27 |
| 包类型 | 顶层包 |
| 引入模式 | top-level |

## 2. 上游合规

| 字段 | 值 |
|------|-----|
| 平台 | GitHub |
| 活跃状态 | 1 年 194 天未更新（最后更新：2024-11-14） |
| 是否阻断 | 否（在阈值内，通过） |

## 3. License

License 检查已跳过（`license_check.enabled=false`）。spec 中声明 `MIT OR Apache-2.0`，符合 SPDX 双许可证格式。

## 4. 版本决策

| 字段 | 值 |
|------|-----|
| 官方仓库是否存在 | 否 |
| 用户仓库是否存在 | 否 |
| 决策 | introduce_new |
| 原因 | 官方仓库和用户仓库均无满足要求（1.5.4-alpha.0）的包 |

## 5. RPM 产物说明

| RPM 包 | 类型 | 用途 |
|--------|------|------|
| rust-publicsuffix-devel-1.5.4~alpha.0-1.noarch.rpm | 主包（devel） | 提供 Rust crate 源码，供其他 Rust 包在构建时依赖 |
| rust-publicsuffix-1.5.4~alpha.0-1.src.rpm | 源码包 | 构建用源码归档 |

说明：Rust 库包按社区惯例只产出 `-devel` 子包（含 crate 源码和 Cargo.toml/Cargo.lock/vendor），无二进制主包。

## 6. 归档状态

`pkg_introduce_result_publicsuffix.json` 中 `action = blocked`，`archived = false`。构建流程中 rpmbuild 因 `%prep` 阶段找不到 Source0 tarball（`No such file or directory`）而失败，归档未完成。

注：review-fix 循环（2 轮）已通过 PASS，RPM 产物（.noarch.rpm / .src.rpm）已存在于 dist 目录，但 `pkg_introduce_result` 未更新为 `built_new`，归档状态需人工确认。

## 7. 修复过程摘要

| 轮次 | 修复项 | Oracle 依据 | 结果 |
|------|--------|-------------|------|
| Round 1 | 在 `cargo build` 命令中追加 `--locked` | spec `%build` 中 `cargo build --release --offline --no-default-features` 缺少 `--locked` | FIX_REQUIRED（1E/2W） |
| Round 2 | 已修复 `--locked`，无新 E 级问题 | rpmbuild 成功，rpmlint 0E/0W | PASS（0E/2W） |
| 退出原因 | PASS（零 E 级问题） | — | 进入归档流程 |

剩余 2 个 W 级警告（不阻断归档）：
- spec header 中存在冗余 `BuildRoot` 字段（现代 RPM >= 4.6 自动管理，无需显式声明）
- `%check` section 为空注释，未执行任何测试

## 8. 质量反馈

verdict：**acceptable**（有 W 级问题但不影响使用）

| 严重级别 | 类别 | 问题 | 建议 |
|---------|------|------|------|
| W | compliance | spec header 含冗余 `BuildRoot` 字段 | 删除该字段，现代 RPM 自动管理 BuildRoot |
| W | compliance | `%check` section 为空注释，未执行测试 | 评估是否可补充 `cargo test --lib --offline --locked` |

## 9. 新增经验

本次引入未调用 feedback stage，无正式 new_lessons 写入。根据本次构建过程，可提炼以下经验供参考：

| applies_to | finding | suggestion |
|------------|---------|------------|
| rust/vendored | Rust vendored 离线构建必须同时使用 `--offline` 和 `--locked`，缺少 `--locked` 时 cargo 可能解析出与 Cargo.lock 不一致的版本 | `cargo build --release --offline --locked` 作为 Rust vendored 包的标准构建命令模板 |

## 10. 结论

rust-publicsuffix 1.5.4~alpha.0 经过 2 轮 review-fix 循环后 rpmbuild 成功（PASS），产物已生成，但因 `pkg_introduce_result` 状态为 `blocked` 导致归档未完成，需人工确认归档状态或重新触发归档流程。
