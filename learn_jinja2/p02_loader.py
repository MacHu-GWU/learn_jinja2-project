#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
loader是jinja2中用于从文件中读取模板代码的中间类。

- FileSystemLoader: 指定一个目录, 在目录下根据文件名寻找模板。
- PackageLoader: 指定一个安装好的python包, 在 ``package_name.package_path`` 目录
  下寻找模板。
- DictLoader: 使用 ``{key: source}`` 的形式读取模板。
- FunctionLoader: 使用一个函数, 接受key为输入, 返回模板源代码。

ref: http://jinja.pocoo.org/docs/2.9/api/#loaders
"""