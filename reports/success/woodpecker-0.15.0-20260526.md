# woodpecker 包引入报告

## 1. 基本信息

| 字段 | 值 |
|------|------|
| 包名 | woodpecker |
| 上游地址 | https://github.com/woodpecker-ci/woodpecker |
| 语言 | Go |
| 版本 | 0.15.0 |
| 引入日期 | 2026-05-26 |
| 包类型 | 顶层包（top-level） |
| 引入模式 | built_new（新引入并构建） |

---

## 2. 上游合规

| 检查项 | 结果 |
|------|------|
| 平台 | GitHub（主流平台） |
| 仓库活跃度 | 0 天前有更新，活跃 |
| 合规结论 | 通过 |

---

## 3. License

License 检查已跳过（`license_check.enabled=false`）。如需合规确认，请手动核查上游 `LICENSE` 文件（当前 spec 声明 `Apache-2.0`）。

---

## 4. 版本决策

| 检查项 | 结果 |
|------|------|
| 官方仓库（openEuler） | 不存在 woodpecker |
| 用户仓库（repo-aitest） | 不存在 woodpecker |
| 决策 | `introduce_new` — 官方仓库和用户仓库均无满足要求（0.15.0）的包 |
| 动作 | `built_new` |

---

## 5. RPM 产物说明

woodpecker 为多二进制项目，主包作为元包（meta-package），可执行文件按功能拆分为三个子包：

| RPM 包 | 用途 |
|------|------|
| `woodpecker-0.15.0-1.<dist>.src.rpm` | 源码包（spec + tarball） |
| `woodpecker-0.15.0-1.<dist>.aarch64.rpm` | 元包，仅含 `LICENSE` 和 `README.md`，无二进制 |
| `woodpecker-agent-0.15.0-1.<dist>.aarch64.rpm` | CI Agent 组件，执行流水线任务（`/usr/bin/woodpecker-agent`） |
| `woodpecker-server-0.15.0-1.<dist>.aarch64.rpm` | CI Server 组件，管理流水线（`/usr/bin/woodpecker-server`，不含 Web UI 前端） |
| `woodpecker-cli-0.15.0-1.<dist>.aarch64.rpm` | 命令行工具（`/usr/bin/woodpecker`） |

> **注意**：woodpecker-server 使用 `go:embed` 内嵌前端资源。由于离线构建环境无法执行 Node.js 前端构建，spec 在 `%prep` 阶段创建了占位 HTML 文件以满足 embed 约束，**不包含完整 Web UI 前端**。

---

## 6. 归档状态

已归档：是（`archived: true`）。RPM 产物已推送到用户仓库（repo-aitest）。

---

## 7. 修复过程摘要

review-fix 循环共执行 **2 轮**，正常退出（`exit_reason: pass`）。

| 轮次 | 修复项 | Oracle 依据 | 结果 |
|------|------|------|------|
| Round 1 | Source0 仅为本地文件名，缺少完整上游 URL（E 级） | rpmlint 输出 `W: invalid-url Source0: woodpecker-0.15.0.tar.gz` | FIX_REQUIRED，spec hash 变更 |
| Round 2 | Source0 修复为 `https://github.com/woodpecker-ci/woodpecker/archive/v%{version}/%{name}-%{version}.tar.gz` | rpmlint 0 error，rpmbuild 成功输出 4 个 RPM | PASS，0 E 级问题 |
| 退出原因 | PASS（零 E 级问题） | — | — |

两轮全程 W 级警告（`no-buildroot-tag` 误报、`go build` 未显式 `-mod=vendor`）保持不变，符合预期（`fix_instruction=null`）。

---

## 8. 质量反馈

**整体评级：`acceptable`**（有 W 级问题但不影响使用）

| 类别 | 发现 | 建议 | 严重度 |
|------|------|------|------|
| 社区惯例 | `%prep` 使用 `%setup -q` 而非现代推荐的 `%autosetup -q` | 改用 `%autosetup -q`；无补丁时功能等价，但社区偏好后者 | W |
| 可维护性 | `GOPROXY=off` 离线构建但三处 `go build` 均未显式传入 `-mod=vendor` | 统一添加 `-mod=vendor`，避免 vendor 目录缺失时错误信息不清晰 | W |
| 合规性 | spec 缺少 `%check` section，未运行任何单元测试 | 若上游有 `go test ./...` 建议在 `%check` 中执行；离线环境可注释说明 | W |
| 可维护性 | 主包 `%files` 仅含 `%license`/`%doc`，无二进制；实质为元包设计 | 在 `%description` 中注明"主包为元包，通过子包提供可执行文件" | W |
| 可维护性 | `BuildRequires: git` 存在，但离线 Go 构建通常不需要 git | 确认是否真正需要；`-buildvcs=false` 在 git 不可用时同样有效 | W |

**构建过程**：修复循环合理（2 轮），go:embed 占位文件处理方式正确，已在 spec 中注明不含 Web UI 前端。

---

## 9. 新增经验

本次引入共提炼 **4 条**新经验，已写入 lessons 文件：

| 适用场景 | 经验摘要 |
|------|------|
| `go/embed` | 使用 `go:embed` 内嵌静态资源的 Go 项目，离线构建时需在 `%prep` 创建占位目录和最小文件，否则 `go build` 报 "directory prefix does not exist" |
| `go/offline-build` | `GOPROXY=off` + vendor 构建应在所有 `go build` 命令中显式添加 `-mod=vendor`，依赖来源意图明确，vendor 缺失时报错更清晰 |
| `go/multi-binary` | 含多个 `cmd/*` 入口的 Go 项目建议拆为多个子包（`%package agent/server/cli`），主包仅含 `%license/%doc` 作为元包 |
| `go/cgo-sqlite` | 依赖 SQLite 的 Go 项目须设置 `CGO_ENABLED=1`，`BuildRequires` 添加 `sqlite-devel` 和 `glibc-devel`，否则链接阶段报找不到 `sqlite3.h` |

---

## 10. 结论

woodpecker 0.15.0 已成功引入并归档。构建经 2 轮 review-fix 循环完成，唯一 E 级问题（Source0 缺少上游 URL）已修复，最终 rpmlint 0 error，4 个 RPM 产物（主包 + agent + server + cli）已推送到用户仓库。spec 质量评级 `acceptable`，存在 5 项 W 级可维护性/合规性改进建议，不影响正常使用。
