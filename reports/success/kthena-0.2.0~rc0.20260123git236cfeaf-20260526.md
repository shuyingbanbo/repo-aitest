# kthena 包引入报告

## 1. 基本信息

| 字段 | 值 |
|------|----|
| 包名 | kthena |
| 上游地址 | https://github.com/volcano-sh/kthena |
| 语言 | Go |
| 版本 | 0.2.0~rc0.20260123git236cfeaf |
| 引入日期 | 2026-05-26 |
| 包类型 | 顶层包 |

## 2. 上游合规

| 字段 | 值 |
|------|----|
| 平台 | GitHub（主流平台）|
| 最近更新 | 2026-05-26（0 天前） |
| 活跃度 | 活跃 |
| 结论 | 通过 |

## 3. License

License 检查已跳过（`license_check.enabled=false`）。spec 中声明 `License: Apache-2.0`，属 OSI 批准的宽松许可证，无合规风险。

## 4. 版本决策

| 字段 | 值 |
|------|----|
| 官方仓库（openEuler）| 不存在 |
| 用户仓库（repo-aitest）| 不存在 |
| 决策 | `introduce_new` |
| 执行动作 | `built_new` |
| 原因 | 官方仓库和用户仓库均无满足要求的包 |

## 5. 模块说明

kthena 为多二进制 Go 项目，包含三个独立可执行组件，分别构建并拆入独立子包：

| 二进制 | 源路径 | 子包 | 说明 |
|--------|--------|------|------|
| kthena-controller-manager | `./cmd/kthena-controller-manager/` | `kthena-controller-manager` | 控制平面组件，负责 LLM 推理生命周期管理，持续 reconcile Kthena CRD |
| kthena-router | `./cmd/kthena-router/` | `kthena-router` | 数据平面入口，按模型名/请求头/URI 分类推理流量并执行负载均衡 |
| kthena | `./cli/kthena/` | `kthena-cli` | Kthena CLI 工具，用于管理 LLM 推理工作负载 |

## 6. RPM 产物说明

| RPM 文件 | 类型 | 用途 |
|----------|------|------|
| `kthena-0.2.0~rc0.20260123git236cfeaf-1.aarch64.rpm` | 主包 | 包含 LICENSE、README.md，作为元数据锚点；不含任何二进制 |
| `kthena-controller-manager-0.2.0~rc0.20260123git236cfeaf-1.aarch64.rpm` | 子包 | 控制器管理组件二进制 `/usr/bin/kthena-controller-manager` |
| `kthena-router-0.2.0~rc0.20260123git236cfeaf-1.aarch64.rpm` | 子包 | 路由组件二进制 `/usr/bin/kthena-router` |
| `kthena-cli-0.2.0~rc0.20260123git236cfeaf-1.aarch64.rpm` | 子包 | CLI 工具二进制 `/usr/bin/kthena` |
| `kthena-0.2.0~rc0.20260123git236cfeaf-1.src.rpm` | 源码包 | spec + Source tarball，供构建复现使用 |

## 7. 归档状态

已成功归档到用户仓库（`archived: true`）。

## 8. 修复过程摘要

| 轮次 | 修复项 | Oracle 依据 | 结果 |
|------|--------|-------------|------|
| Round 1 | 无 E 级问题，无需修复 | rpmlint: 0E / 1W（no-buildroot-tag，可忽略） | rpmbuild ✓，Critic verdict: PASS |
| 退出原因 | PASS（零 E 级问题，一轮即通过） | — | — |

共执行 1 轮 review-fix 循环，首轮即通过，无振荡，无强制退出。

## 9. 质量反馈

**整体评级：`good`（构建成功，无 E 级问题）**

| 类别 | 发现 | 建议 | 级别 |
|------|------|------|------|
| 社区合规 | rpmlint 报 `W: no-buildroot-tag`；现代 RPM（>= 4.6）无需显式声明 BuildRoot，属误报 | 可忽略，无需修改 | W |
| 社区惯例 | spec 缺少 `%check` section；Go 项目可用 `go test ./...` 运行单元测试，离线环境需配合 `-mod=vendor` | 酌情添加 `%check` section；若上游测试不适合 RPM 构建环境，可添加注释说明原因 | W |
| BuildRequires 精简 | `BuildRequires: git` 冗余——`%build` 设置了 `GOFLAGS=-buildvcs=false`，Go toolchain 不会调用 git 获取 VCS 信息 | 可移除 `BuildRequires: git`，减少不必要的构建依赖 | W |

**过程亮点：**
- 构建一次成功，Source0 使用完整 commit SHA（`236cfeaf...`），确保源码不可变
- `GOPROXY=off` + `-mod=vendor` 实现全离线可复现构建
- `GOFLAGS=-buildvcs=false` 正确规避 tarball 构建中 VCS 元数据缺失问题
- 三个二进制组件分别拆入独立子包，符合 `go/multi-binary` 最佳实践

## 10. 新增经验

本次引入提炼到以下可复用经验：

**`go/buildvcs-false`**

- **发现**：Go 1.18+ 默认尝试从 VCS（git/svn 等）读取提交信息嵌入二进制；在 RPM `%build` 环境中源码从 tarball 解压，无 VCS 元数据，`go build` 会报 `error obtaining VCS status: exit status 128`。设置 `GOFLAGS=-buildvcs=false` 或在 `go build` 命令追加 `-buildvcs=false` 可安全关闭此行为。
- **建议**：所有通过 tarball 构建的 Go 包（非 git clone），`%build` 均应设置 `export GOFLAGS=-buildvcs=false`；同时可移除 `BuildRequires: git`，因为 VCS 查询已被关闭。

## 11. 结论

kthena 0.2.0~rc0.20260123git236cfeaf 首次引入成功，构建可复现，多组件分包结构规范，已归档至用户仓库；3 条 W 级建议（`%check` 缺失、`git` BuildRequires 冗余、rpmlint no-buildroot-tag 误报）不影响包的使用，可在后续迭代中改进。
