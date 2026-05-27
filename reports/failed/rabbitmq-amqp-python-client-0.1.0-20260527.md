# rabbitmq-amqp-python-client 引入报告

## 1. 基本信息

| 字段 | 值 |
|------|----|
| 包名 | rabbitmq-amqp-python-client |
| 上游地址 | https://github.com/rabbitmq/rabbitmq-amqp-python-client |
| 语言 | Python |
| 版本 | 0.1.0 |
| 构建后端 | poetry |
| 引入日期 | 2026-05-27 |
| 包类型 | 顶层包 |
| 引入结果 | 阻断（未构建） |

## 2. 上游合规

| 字段 | 值 |
|------|----|
| 平台 | GitHub |
| 活跃状态 | 活跃（8 天前有更新，最后更新 2026-05-18） |
| 合规结论 | 通过 |

## 3. License

License 检查已跳过（`license_check.enabled=false`）。

## 4. 版本决策

| 字段 | 值 |
|------|----|
| 官方仓库是否存在 | 否 |
| 用户仓库是否存在 | 否 |
| decision | introduce_new |
| action | blocked |

阻断原因：依赖预检发现 2 个运行时依赖在官方源的可用版本不满足要求，按版本选择规则阻断，需人工决策后重新发起引入。

## 5. 模块说明

不适用（引入流程在依赖预检阶段被阻断，未生成 spec 文件，未执行构建）。

## 6. RPM 产物说明

不适用（构建未执行）。

## 7. 归档状态

未归档（构建未执行）。

## 8. 修复过程摘要

不适用（构建未执行，未进入 review-fix 循环）。

## 9. 质量反馈

不适用（构建未执行）。

## 10. 阻断依赖明细

| 依赖名 | 要求版本 | 官方源最高版本 | 阻断原因 |
|--------|---------|--------------|---------|
| python-qpid-proton | >=0.39.0, <0.40.0 | 0.38.0 | 官方源版本低于要求下限 |
| typing-extensions | >=4.13.0, <5.0.0 | 4.12.2 | 官方源版本低于要求下限 |

构建系统依赖 `poetry-core` 在官方源已满足（v1.4.0），无问题。

**可选处理方案：**

1. 先引入 `python-qpid-proton` 0.39.x（需升级官方源中的 0.38.0），并升级 `python-typing-extensions` 至 >=4.13.0，再重新发起本包引入。
2. 评估是否可接受更宽松的版本约束（需与上游确认兼容性）。
3. 评估能否使用官方源中已有的 `python-qpid-proton` 0.38.0（需确认 rabbitmq-amqp-python-client 是否实际兼容）。

## 11. 新增经验

本次引入因阻断未完成构建，无新经验写入 lessons。

## 12. 结论

rabbitmq-amqp-python-client 0.1.0 引入流程因 2 个运行时依赖（python-qpid-proton、typing-extensions）在 OpenEuler 官方源的可用版本低于要求，在依赖预检阶段被阻断，需先升级或引入对应依赖包后重新发起引入。
