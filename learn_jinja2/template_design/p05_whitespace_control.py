#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

ref: http://jinja.pocoo.org/docs/2.9/templates/#whitespace-control
"""

from __future__ import print_function
from jinja2 import Template


# 默认情况下, 用空格替代所有的tag之后就是结果
text = \
"""
-------------------------------------------------------------------------------
{% raw %}
<div>
    {% if True %}
        yay
    {% endif %}
</div>
{%- endraw %}

->

<div>
    {% if True %}
        yay
    {% endif %}
</div>
"""
print(Template(text).render())


# 减号放在tag的开始处意味着删除tag之前的空格
# 减号放在tag的结束处意味着删除tag之后的空格
text = \
"""
-------------------------------------------------------------------------------
{% raw %}
<div>
    {% if True -%}
        yay
    {%- endif %}
</div>
{%- endraw %}

->

<div>
    {% if True -%}
        yay
    {%- endif %}
</div>
"""
print(Template(text).render())


# 删除所有tag前后的空格
text = \
"""
-------------------------------------------------------------------------------
{% raw %}
<div>
    {%- if True -%}
        yay
    {%- endif -%}
</div>
{%- endraw %}

->

<div>
    {%- if True -%}
        yay
    {%- endif -%}
</div>
"""
print(Template(text).render())
