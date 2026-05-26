# php-parser 包引入报告

生成日期：2026-05-26

---

## 1. 基本信息

| 字段 | 值 |
|------|-----|
| 包名 | php-parser |
| 上游地址 | https://github.com/VKCOM/php-parser |
| 语言 | Go |
| 版本 | 0.8.0~rc2.20210731git44bbff6 |
| 引入日期 | 2026-05-26 |
| 包类型 | 顶层包 |
| 决策 | 引入新包（introduce_new） |

---

## 2. 上游合规

| 检查项 | 结果 |
|------|------|
| 平台 | GitHub（主流平台）|
| 活跃度 | 2 年 246 天未更新（最后更新：2023-09-23），在阈值内，**通过** |
| 阻断 | 否 |

---

## 3. License

License 检查已跳过（`license_check.enabled=false`）。

spec 声明 License 为 `MIT`，源码仓库包含 LICENSE 文件，由构建结果的 `%license LICENSE` 宏打包。

---

## 4. 版本决策

| 检查项 | 结果 |
|------|------|
| 官方仓库（OS/EPOL/everything 等） | 不存在 |
| 用户仓库（repo-aitest） | 不存在 |
| 决策 | `introduce_new` — 官方仓库和用户仓库均无满足要求的包 |
| 执行动作 | `built_new` |

---

## 5. 模块说明

该包为单模块命令行工具（`./cmd/php-parser/`），不含多模块结构，无需分包，不适用模块表格。

---

## 6. RPM 产物说明

| 产物 | 架构 | 用途 |
|------|------|------|
| `php-parser-0.8.0~rc2.20210731git44bbff6-1.aarch64.rpm` | aarch64 | 主包，包含 `/usr/bin/php-parser` 可执行文件，LICENSE 及 README |
| `php-parser-0.8.0~rc2.20210731git44bbff6-1.src.rpm` | noarch | 源码包，含 spec + Source0 源码 tar + Source1 vendor tar |

spec `%files` 内容：
- `%license LICENSE`
- `%doc README.md`
- `%{_bindir}/php-parser`

---

## 7. 归档状态

**未归档**（`archived: false`）。构建产物已生成但尚未推送到用户 RPM 仓库（repo-aitest）。

---

## 8. 修复过程摘要

review-fix 循环共执行 **2 轮**，退出原因：**PASS（零 E 级问题）**。

| 轮次 | 修复项 | Oracle 依据 | 结果 |
|------|------|------|------|
| Round 1 | 识别 E 级问题：go build 通过 GOPROXY=https://goproxy.cn,direct 联网下载传递依赖（`github.com/pkg/profile`、`github.com/yookoala/realpath`），离线构建失败 | rpmbuild 日志含 `go: downloading ...` 行 | FIX_REQUIRED，1E/3W |
| Round 2 | 修复：引入 vendor tarball（Source1）；GOPROXY 改为 `off`；go build 添加 `-mod=vendor`；移除 GONOSUMDB=* | 构建日志无任何 `go: downloading` 行，exit 0，RPM/SRPM 均成功生成 | PASS，0E/2W |
| 退出原因 | **PASS（零 E 级问题）** | — | — |

剩余 W 级警告（不阻断归档）：
- `W: no-buildroot-tag`（rpmlint 误报，现代 RPM 无需 BuildRoot）
- 缺少 `%check` section（可选改进项）

---

## 9. 质量反馈

**verdict：`acceptable`**

| 类别 | 发现 | 严重级别 | 建议 |
|------|------|------|------|
| 合规性 | spec 缺少 %check section，未运行任何测试 | W | 建议添加 `go test -mod=vendor ./...`，增强 PHP 语法解析逻辑的质量保障 |
| 可复现性 | Source0 使用原始 commit hash（44bbff6）而非命名 tag，因上游仅有 RC 版本，无稳定 tag 可用 | W | commit hash 方式合理；版本字符串格式 `0.8.0~rc2.20210731git44bbff6` 符合 OpenEuler 快照包命名规范 |

构建过程总体高效：2 轮循环最少化，Round 1 准确定位 vendor 缺失问题，Round 2 完整修复并通过验证。

---

## 10. 新增经验

本次引入提炼了以下可复用经验（已写入 go lessons）：

| 适用范围 | 经验摘要 |
|------|------|
| `go/vendor-missing` | Go spec 中若同时出现 `GOPROXY=<外部镜像>` 和 `GONOSUMDB=*`，是依赖在线下载的诊断信号，离线 RPM 构建（OBS/mock）将失败。正确做法：执行 `go mod vendor` 生成 vendor 目录，以 Source1 形式打包，`%prep` 中解包，go build 添加 `-mod=vendor`，`GOPROXY` 改为 `off`，删除 `GONOSUMDB`。 |

---

## 11. 结论

php-parser（Go 语言，版本 0.8.0~rc2.20210731git44bbff6）构建成功，经 2 轮 review-fix 循环修复了 vendor 缺失导致的离线不可复现问题，产出 aarch64 RPM 和 SRPM，质量评级 `acceptable`，待归档到用户仓库。
