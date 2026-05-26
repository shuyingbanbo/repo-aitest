# vega 包引入报告

## 1. 基本信息

| 字段 | 值 |
|------|------|
| 包名 | vega |
| 上游地址 | https://github.com/vegaprotocol/vega |
| 语言 | Go |
| 版本 | 0.23.1.20200903gitd44074135 |
| 引入日期 | 2026-05-26 |
| 包类型 | 顶层包 |
| 引入模式 | top-level |

## 2. 上游合规

| 字段 | 值 |
|------|------|
| 托管平台 | GitHub（主流平台）|
| 最近更新 | 2025-02-03 |
| 不活跃天数 | 476 天（1 年 111 天）|
| 是否阻断 | 否，仍在阈值内，通过 |

## 3. License

| 字段 | 值 |
|------|------|
| SPDX 标识 | MIT |
| 分类 | 宽松许可证 |
| License 检查 | 已跳过（license_check.enabled=false）|

## 4. 版本决策

| 字段 | 值 |
|------|------|
| 官方仓库（EPOL/OS/everything 等） | 不存在 |
| 用户仓库（repo-aitest） | 不存在 |
| 决策 | introduce_new |
| Action | built_new |
| 原因 | 官方仓库和用户仓库均无满足要求的包，执行全新引入 |

## 5. RPM 产物说明

| RPM 包名 | 类型 | 说明 |
|------|------|------|
| vega-0.23.1.20200903gitd44074135-1.aarch64.rpm | 主包 | 去中心化衍生品交易平台主二进制（`/usr/bin/vega`），含 README.md |
| vegastream-0.23.1.20200903gitd44074135-1.aarch64.rpm | 子包 | Vega 流式服务组件（`/usr/bin/vegastream`）|
| vega-0.23.1.20200903gitd44074135-1.src.rpm | 源码包 | 含 spec 和源码 tarball，用于可复现重建 |

Source0 使用完整 40 位 commit hash（d44074135ac1685dbdca9143f41263ac9fca2853）作为不可变 ref，满足可复现性要求。

## 6. 归档状态

未归档（`archived: false`）。构建产物位于 `/root/.claude/skills/rpm-repo-github/dist`，待后续归档推送。

## 7. 修复过程摘要

| 轮次 | 修复项 | Oracle 依据 | 结果 |
|------|------|------|------|
| Round 1 | 无需修复 | rpmlint 0E/1W；rpmbuild 正常退出 | PASS |
| 退出原因 | PASS（零 E 级问题） | — | — |

构建首轮即通过，无需进入修复循环。唯一警告（`W: no-buildroot-tag`）为 rpmlint 对现代 RPM spec 的误报，无需修复。

## 8. 质量反馈

**verdict：acceptable**

| 类别 | 问题 | 严重级 | 建议 |
|------|------|------|------|
| 社区惯例 | 主包和 vegastream 子包均缺少 `%license` 宏，仅用 `%doc README.md` 记录文档，未在 `%files` 中声明 LICENSE 文件 | W | 每个 `%files` section 添加 `%license LICENSE`；先确认源码包内 license 文件实际名称 |
| 合规性 | rpmlint `W: no-buildroot-tag`，现代 RPM 对旧式 spec 的误报 | W | 可忽略 |
| 可测试性 | spec 无 `%check` section，未运行任何单元测试 | W | 若上游含 `go test ./...`，可在 `%check` 添加 `go test -mod=vendor ./...`；若依赖网络可在注释中说明跳过原因 |

构建过程质量良好：Source0 不可变 ref、`-mod=vendor` + `GOPROXY=off` 离线构建、关键环境变量（`CGO_ENABLED`、`GOPROXY`、`GOFLAGS`、`GOPATH`）均在 spec 内显式设定，无隐式环境依赖。

## 9. 新增经验

| applies_to | 经验要点 | 建议 |
|------|------|------|
| go/license-missing | Go RPM 包中容易遗漏 `%license` 宏：仅写 `%doc README.md` 而不写 `%license LICENSE`，导致安装后缺少 license 文件；含多个子包时每个 `%files` section 都需要单独声明 | Go spec 的每个 `%files` section（主包和所有子包）均应包含 `%license LICENSE` 行；构建前先确认源码包内 license 文件的实际名称（LICENSE、LICENSE.md、LICENSE.txt 等）|

## 10. 结论

vega 0.23.1.20200903gitd44074135 首轮构建即通过，产物可复现性满足要求，主要待改进项为补充 `%license` 宏声明，整体引入质量 **acceptable**，待归档推送。
