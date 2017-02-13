#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ref: http://jinja.pocoo.org/docs/2.9/templates/#line-statements
"""

from __future__ import print_function
import jinja2
from jinja2 import Template

jinja2.environment.LINE_STATEMENT_PREFIX = "#"

text = \
"""
<ul>
# for item in seq
    <li>{{ item }}</li>
# endfor
</ul>
"""
t = Template(text)
print(t.render(seq=list("ABCD")))


text = \
"""
<ul>
{% for item in seq %}
    <li>{{ item }}</li>
{% endfor %}
</ul>
"""
t = Template(text)
print(t.render(seq=list("ABCD")))