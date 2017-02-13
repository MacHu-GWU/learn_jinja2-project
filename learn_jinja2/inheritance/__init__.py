#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
要想使用继承, 需要满足两个条件:

1. 被继承的母template需要跟子template需要在一个环境下。
2. 继承的根据是用block名
"""

import os
from jinja2 import Environment, FileSystemLoader
from dataIO import textfile

def example():
    loader = FileSystemLoader(os.path.dirname(__file__))
    env = Environment(loader=loader)
    
    t_child = env.get_template("child.html")
    textfile.write(t_child.render(), "index.html")

if __name__ == "__main__":
    example()
