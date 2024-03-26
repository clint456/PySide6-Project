# 一个使用Pyside6正在开发的多线程上位机界面程序

## 1.安装poetry (依赖scoop、pipx)

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

> 3. 安装poetry
>
> ```powershell
> pipx install poetry
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

> `win/loadWin.py` 为加载页面
>
> 运行: `python load_test.py`


> `win/mainWin.py` 为反无人机操作页面
>
> 运行：`python main_test.py`

--- 
## Bug
> `run.py` 为系统启动入口
>
> 但目前还有bug，问题是：
>  - 主线程的子线程里，貌似不能再启动子线程【还未解决】
> ```ERROR
> # 报错1.
> QObject::setParent: Cannot set parent, new parent is in a different thread
> QBasicTimer::stop: Failed. Possibly trying to stop from a different thread
> QBasicTimer::stop: Failed. Possibly trying to stop from a different thread
> QBasicTimer::stop: Failed. Possibly trying to stop from a different thread
> QBasicTimer::stop: Failed. Possibly trying to stop from a different thread

```
# 报错2 
Traceback (most recent call last):
  File "/home/clint/workspace/dev/pyside6Projcet/thr/mainWinThread.py", line 25, in run
    self.main.exec()
AttributeError: 'MainWin' object has no attribute 'exec'
QBasicTimer::start: Timers cannot be started from another thread
QObject::startTimer: Timers can only be used with threads started with QThread
QBasicTimer::start: Timers cannot be started from another thread
QObject::killTimer: Timers cannot be stopped from another thread
QBasicTimer::start: Timers cannot be started from another thread
```
 

## 4.待完成的任务
1. 使用`run.py` 启动 `win/loadWin.py`,然后通过`class loadWin`再开启`class mainWin`
2. `thr/socketThread.py`数据传输模块测试
3. 添加一个实时显示下位机云台状态的动画