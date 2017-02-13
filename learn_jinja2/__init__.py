#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
jinja2是Python社区的一个文本模板引擎, 功能非常强大。

- 英文文档: http://jinja.pocoo.org/docs/dev/
- 中文文档: http://docs.jinkan.org/docs/jinja2/index.html
"""

__version__ = "0.0.1"
__short_description__ = "Learn jinja2."
__license__ = "MIT"

try:
    from .pkg.decorator import run_if_is_main
    from .p01_manage_template import env
except:
    from learn_jinja2.pkg.decorator import run_if_is_main
    from learn_jinja2.p01_manage_template import env