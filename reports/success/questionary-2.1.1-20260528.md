# questionary 包引入报告

## 1. 基本信息

| 字段 | 值 |
|------|-----|
| 包名 | questionary |
| 上游地址 | https://github.com/tmbo/questionary |
| 语言 | Python |
| 版本 | 2.1.1 |
| 引入日期 | 2026-05-28 |
| 包类型 | 依赖包（depth=1，由 oss-crs 引入链触发） |

## 2. 上游合规

| 字段 | 值 |
|------|-----|
| 平台 | GitHub |
| 活跃度 | 8 天前有更新（2026-05-19），活跃 |
| 是否主流平台 | 是 |
| 阻断 | 否 |

## 3. License

License 检查已跳过（`license_check.enabled=false`）。

## 4. 版本决策

| 字段 | 值 |
|------|-----|
| 请求版本 | 2.1.1 |
| 官方仓库已有 | 否 |
| 用户仓库已有 | 否 |
| 决策 | introduce_new |
| 原因 | 官方仓库和用户仓库均无满足要求（2.1.1）的包 |

## 5. 依赖处理

questionary 2.1.1 声明了 2 个依赖，均已在 OpenEuler 官方源中满足，无需额外引入：

| 依赖 | 约束 | 来源 | 满足版本 |
|------|------|------|---------|
| python3-prompt-toolkit | >=2.0, <4.0 | OpenEuler 官方源 | 3.0.43-1.oe2403sp3 |
| python3-poetry-core | 无约束（构建依赖） | OpenEuler 官方源 | 1.4.0-1.oe2403sp3 |

## 6. RPM 产物说明

| RPM 包 | 类型 | 用途 |
|--------|------|------|
| python3-questionary-2.1.1-1.noarch.rpm | 主包 | 运行时库，包含 questionary Python 模块及 dist-info |
| python-questionary-2.1.1-1.src.rpm | 源码包 | 构建用源码存档 |
| python-questionary（help 子包） | 文档包 | README.md 等开发文档（spec 中已定义，随主包构建） |

## 7. 归档状态

未归档（`archived: false`）。

## 8. 修复过程摘要

review-fix 循环共执行 1 轮，首轮 rpmbuild 即通过，直接退出。

| 轮次 | 修复项 | Oracle 依据 | 结果 |
|------|--------|------------|------|
| Round 1 | 无需修复 | rpmlint 0E/0W，rpmbuild 成功 | 直接 PASS |
| 退出原因 | PASS（零 E 级问题） | — | — |

## 9. 质量反馈

无 feedback 文件（依赖包轻量流程，未触发 feedback stage）。

构建结果摘要（来自 build_rpm_result）：

- spec 生成：成功
- rpmlint：通过
- rpmbuild：成功
- RPM 安装验证：通过

spec 结构符合 OpenEuler Python 包惯例：使用 `%pyproject_build` + `%pyproject_install`，`%check` section 已保留并注明跳过原因（交互式终端依赖），`%files` 手工列出，无多余宏。

## 10. 新增经验

本次构建未触发 feedback stage，无新经验写入 lessons 文件。

## 11. 结论

questionary 2.1.1 作为 oss-crs 的依赖包成功引入，首轮构建即通过，spec 质量良好，所有运行时依赖均由 OpenEuler 官方源满足，无需额外引入传递依赖。
