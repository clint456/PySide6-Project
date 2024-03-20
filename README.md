# 一个使用Pyside6正在开发的多线程上位机界面程序

## 1.安装poetry（依赖scoop、pipx）

> 1. 安装scoop
>
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
> ```

>   2. 安装pipx
>
> ```powershell
> scoop install pipx
> pipx ensurepath
> ```

---

## 2.poetry简单使用

[Poetry 使用指南](docs\Poetry 使用指南 (版本 1.8.2).md)

[Poetry 官网方文档](https://python-poetry.org/docs/#system-requirements)

```powershell
# 加载环境
poetry install --no-root
```

## 3.运行

```powershell
poetry run python main.py
```
