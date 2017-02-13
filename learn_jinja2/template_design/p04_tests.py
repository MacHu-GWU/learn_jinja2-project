#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jinja2 import Template

def test():
    text = \
    """
    {%- for i in range(10) -%}
    {%- if i is divisibleby(3) -%}
    {{ i }}
    {%- endif -%}
    {%- endfor -%}
    """
    t = Template(text)
    assert t.render() == "0369"
    
test()