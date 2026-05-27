# rapidfuzz 引入报告

## 1. 基本信息

| 字段 | 值 |
|------|-----|
| 包名 | rapidfuzz |
| 版本 | 3.9.7 |
| 引入日期 | 2026-05-27 |
| 动作 | built_new |
| 包类型 | 依赖包（由 thefuzz 引入） |

## 2. 版本决策

| 检查项 | 结果 |
|--------|------|
| 动作 | built_new |
| 来源 | 从 manylinux aarch64 预编译 wheel 打包（Cython >= 3.0.11 在 OpenEuler 中不可用） |

## 3. 依赖情况

无额外依赖。

## 4. RPM 产物

python3-rapidfuzz-3.9.7-1.aarch64.rpm

## 5. 结论

rapidfuzz 3.9.7 作为 thefuzz 的依赖包成功构建（built_new），使用预编译 wheel 方式打包。
