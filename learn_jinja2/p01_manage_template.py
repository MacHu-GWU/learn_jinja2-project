#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
jinja2使用Environment来管理模板。只有在同一个环境下的多个模板才能使用继承功能。
"""

from jinja2 import Environment, PackageLoader, FileSystemLoader

env = Environment(loader=PackageLoader("learn_jinja2", package_path="templates"))

if __name__ == "__main__":
    t = env.get_template("hello.txt")
    assert t.render(name="Jack") == "Hello Jack!"
