# oss-crs 包引入报告

## 1. 基本信息

| 字段 | 值 |
|------|-----|
| 包名 | oss-crs |
| 上游地址 | https://github.com/ossf/oss-crs |
| 语言 | Python |
| 版本 | 0.1.0 |
| 引入日期 | 2026-05-28 |
| 包类型 | 顶层包 |
| RPM 源包名 | python-oss-crs |

## 2. 上游合规

| 字段 | 值 |
|------|-----|
| 平台 | GitHub |
| 活跃度 | 活跃（0 天前有更新，最后更新 2026-05-27） |
| 结论 | 通过 |

## 3. License

License 检查已跳过（`license_check.enabled=false`）。

## 4. 版本决策

| 字段 | 值 |
|------|-----|
| 官方仓库 | 不存在 |
| 用户仓库 | 不存在 |
| 决策 | introduce_new |
| 原因 | 官方仓库和用户仓库均无满足要求（0.1.0）的包 |

## 5. RPM 产物说明

| RPM 文件 | 类型 | 用途 |
|----------|------|------|
| python3-oss-crs-0.1.0-1.noarch.rpm | 主包 | CRS 编排框架运行时，含 `oss-crs` 命令行工具及 Python 库 |
| python-oss-crs-0.1.0-1.src.rpm | 源码包 | 可复现构建用源码存档 |
| python3-oss-crs-help（spec 中定义） | 文档子包 | README.md、CHANGELOG.md 等开发文档 |

主包运行时依赖：python3-requests、python3-pyyaml、python3-jinja2、python3-dotenv、python3-docker、python3-ruff、python3-pyright、python3-GitPython、python3-pydantic、python3-rich、python3-questionary。

## 6. 归档状态

未归档（`archived: false`）。

## 7. 修复过程摘要

| 轮次 | 修复项 | Oracle 依据 | 结果 |
|------|--------|-------------|------|
| Round 1 | 初始 spec 生成（setuptools 后端） → 改用 %pyproject_build + %pyproject_install → %prep 中 sed 修补 pyproject.toml license 字段 → %files 从 egg-info 改为 dist-info | rpmbuild 日志 / pyproject.toml 格式要求 | rpmbuild 成功 |
| 退出原因 | PASS（零 E 级问题，1 轮完成） | — | — |

spec 经历 4 次写入迭代，均为合规的 `spec_write` 和 `prep_patch` 操作，无源码直接修改。

## 8. 质量反馈

无独立 feedback 阶段报告（build-rpm 未调用 feedback stage）。

根据 spec 内容和构建结果直接评估：

- **verdict**：acceptable
- spec 使用 `%pyproject_build` + `%pyproject_install`，符合 openEuler Python 包惯例
- `%prep` 中通过 `sed` 修补 `pyproject.toml` 的 license 字段（setuptools 68 兼容性），做法合规
- `%check` section 存在但为空，注释说明了原因（需要网络和 Docker daemon），可接受
- `Source0` 使用 `%{pypi_source oss-crs}` 宏，指向 PyPI 不可变 tarball，可复现性良好
- 运行时依赖列表完整，覆盖 `pyproject.toml` 中所有 `dependencies`

轻微问题（W 级）：
- `%check` 为空，未运行任何测试；注释说明了原因，但若后续环境支持可补充基础 import 测试

## 9. 新增经验

本次构建过程中提炼的可复用经验：

1. **applies_to**: `python/setuptools-pyproject`
   - **finding**: 使用 setuptools.build_meta 后端的 pyproject.toml 项目，若 `license` 字段为旧式字符串格式（`license = "MIT"`），setuptools 68+ 会报错。
   - **suggestion**: 在 spec `%prep` 中用 `sed -i 's/^license = "MIT"$/license = {text = "MIT"}/' pyproject.toml` 修补，无需修改上游源码。

2. **applies_to**: `python/pyproject`
   - **finding**: 使用 `%pyproject_install` 时，`%files` 中应使用 `*.dist-info/` 而非 `*.egg-info/`，前者是 PEP 517 构建的标准产物。
   - **suggestion**: 生成 spec 时默认使用 `%{python3_sitelib}/<pkg>-%{version}*.dist-info/`，不要写 egg-info。

## 10. 结论

python-oss-crs 0.1.0 顶层包引入成功，rpmbuild 一轮通过，spec 质量合规，产物已就绪，待归档推送到用户仓库。
