# rabbitmq-amqp-python-client 引入报告

## 1. 基本信息

| 字段 | 值 |
|------|-----|
| 包名 | rabbitmq-amqp-python-client |
| 上游地址 | https://github.com/rabbitmq/rabbitmq-amqp-python-client |
| 语言 | Python |
| 版本 | 0.1.0 |
| 引入日期 | 2026-05-28 |
| 包类型 | 顶层包 |
| 构建后端 | hatchling（pip-wheel fallback） |

---

## 2. 上游合规

| 项目 | 结果 |
|------|------|
| 平台 | GitHub（主流平台） |
| 活跃度 | 9 天前有更新（2026-05-18），活跃 |
| 阻断 | 否 |

---

## 3. License

License 检查已跳过（`license_check.enabled=false`）。spec 中声明 `License: Apache-2.0`，符合 SPDX 标准标识符格式。

---

## 4. 版本决策

| 项目 | 结果 |
|------|------|
| 官方仓库（openEuler） | 不存在 |
| 用户仓库（repo-aitest） | 不存在 |
| 决策 | introduce_new |
| 执行动作 | built_new |
| 原因 | 官方仓库和用户仓库均无满足要求（0.1.0）的包 |

---

## 5. RPM 产物说明

spec 定义了以下子包：

| RPM 包名 | 用途 |
|---------|------|
| python3-rabbitmq-amqp-python-client | 主包，包含 Python 库文件（site-packages） |
| python-rabbitmq-amqp-python-client-help | 文档包，包含 README.md |
| python-rabbitmq-amqp-python-client（src.rpm） | 源码包，用于构建复现 |

---

## 6. 归档状态

`pkg_introduce_result` 中 `archived: false`，构建产物尚未推送到用户仓库。

---

## 7. 修复过程摘要

| 轮次 | 修复项 | Oracle 依据 | 结果 |
|------|--------|------------|------|
| Round 1 | 无需修复 | rpmlint 0E/4W，rpmbuild 成功 | PASS |
| 退出原因 | PASS（零 E 级问题） | — | — |

首轮 rpmbuild 即成功，无 E 级问题，review-fix 循环一轮退出。4 个 W 级警告均为已知误报或可接受的维护性问题，不阻断归档。

---

## 8. 质量反馈

**verdict：acceptable**

| 严重级别 | 类别 | 问题摘要 |
|---------|------|---------|
| W | 构建系统选择 | %build 使用 pip-wheel fallback 而非 %pyproject_build/%pyproject_install，偏离 openEuler Python 包社区惯例 |
| W | Requires 包名规范 | 手写 Requires 将版本号嵌入包名（python3-python-qpid-proton-0.39），与 pythondistdeps.py 自动生成的 dist Requires 不一致 |
| W | 测试缺失说明 | 无 %check section，也无注释说明原因（测试需要运行中的 RabbitMQ broker） |
| W | rpmlint 警告 | 3 个已知误报：unversioned-explicit-provides × 2、no-buildroot-tag × 1 |

---

## 9. 新增经验

本次引入提炼了 2 条新经验，已写入 lessons 文件：

**python/versioned-requires-pkgname**
手写 Requires 时将版本号嵌入包名（如 `python3-python-qpid-proton-0.39`）是非标准写法，与 pythondistdeps.py 自动生成的 `python3.11dist(...)` Requires 不一致，可能导致依赖解析异常。标准写法是 `python3-<pkgname> >= <ver>`，或直接依赖自动生成的 dist Requires。

**python/hatchling-pip-wheel-fallback**
以 hatchling 为构建后端的 Python 包，若容器内 %pyproject_build 宏链不可用，可用 `pip3 wheel --no-build-isolation --no-deps -w wheelhouse . + pip3 install` 作为 fallback。需在 %build 前 `export PYTHONPATH` 指向 pip 安装的 hatchling 路径。优先尝试 %pyproject_build + %pyproject_install，不可用时使用 fallback 并在 spec 注释中说明原因。

---

## 10. 结论

rabbitmq-amqp-python-client 0.1.0 首轮构建成功，无 E 级问题，verdict 为 acceptable；存在 Requires 包名非标准写法和 pip-wheel fallback 两个 W 级改进点，不影响包的正常使用，可在后续迭代中优化。
