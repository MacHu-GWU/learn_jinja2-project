#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Escaping是指如何将在jinja2中有特殊含义的标记字符当做普通字符输出。 

ref: http://jinja.pocoo.org/docs/2.9/templates/#escaping
"""

from __future__ import print_function
from jinja2 import Template

text = 'syntax: {{ "{{" }} variable {{ "}}" }}'
t = Template(text)
print(t.render())


text = \
"""
{% raw %}
    <ul>
    {% for item in seq %}
        <li>{{ item }}</li>
    {% endfor %}
    </ul>
{% endraw %}
"""
t = Template(text)
print(t.render())