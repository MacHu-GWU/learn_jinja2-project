#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

ref: http://jinja.pocoo.org/docs/dev/templates/#whitespace-control
"""

# from jinja2 import Template
from learn_jinja2.p01_manage_template import env

tmp = env.get_template("whitespace-control.html")
print(tmp.render())
