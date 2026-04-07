# OpenEuler RPM 仓库

## 目录结构

```
<pkg-name>/   spec 文件 + 上游源码 tarball
dist/         编译好的 RPM 包 + repodata（yum 软件源）
```

## 使用软件源

```bash
curl -o /etc/yum.repos.d/repo-aitest.repo \
  https://raw.githubusercontent.com/shuyingbanbo/repo-aitest/main/dist/repo-aitest.repo
dnf repolist
```

## 仓库地址

https://github.com/shuyingbanbo/repo-aitest.git
