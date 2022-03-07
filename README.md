# ballancemaps-fetch-py

[ballancemaps-fetch](https://github.com/KambuchiTeam/ballancemaps-fetch) 的 Python 实现。

## 与原 JavaScript 版本的区别

### 结构

不同于 ballancemaps-fetch 的 JavaScript 版，本项目使用 Python 模块代替类的功能。初始化应当使用 `import ballancemaps_fetch`。

本项目中的函数均为同步函数。

### 变量名称

配合 Python 命名惯例，本项目中的变量名称由原项目的 *camelCase* 改为 *snake_case*。例如，原项目中的 `getMapList(index)` 在本项目中被写作 `get_map_list(index)`。

### 测试

直接使用 Python 运行即可（`python ballancemaps_fetch.py`）。
