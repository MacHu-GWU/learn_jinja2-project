#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
变量可以被filters所改变, 换言之, filters就是一个接受变量为输入的函数。

ref: http://jinja.pocoo.org/docs/dev/templates/#filters
list of built-in filters: http://jinja.pocoo.org/docs/dev/templates/#list-of-builtin-filters
"""

from jinja2 import Template


def join():
    """
        
    ref: http://jinja.pocoo.org/docs/dev/templates/#join
    """
    template = Template('{{ l|join(", ") }}')
    text = template.render(l=[1, 2, 3])
    assert text == "1, 2, 3"
    
    template = Template('{{ [key for key, value in data.items()]|join(", ") }}')
    text = template.render(data={"id": 1, "name": "John"})
    print(text)
   
if __name__ == "__main__":
    #
    join()
    

def length():
    """
    
    ref: http://jinja.pocoo.org/docs/dev/templates/#length
    """
    template = Template('{{ sequence|length }}')
    
    text = template.render(sequence=[1, 2, 3])
    assert text == "3"
    
    text = template.render(sequence=set([1, 2, 3]))
    assert text == "3"
    
    text = template.render(sequence={"a": 1, "b":2, "c":3})
    assert text == "3"


if __name__ == "__main__":
    #
    length()
    
    
def random():
    """
    
    ref: http://jinja.pocoo.org/docs/dev/templates/#random
    """
    template = Template('{{ sequence|random }}')
    
    text = template.render(sequence=[1, 2, 3])
    assert text in ["1", "2", "3"]
    
    
if __name__ == "__main__":
    #
    random()
    
    
def round():
    """
    
    ref: http://jinja.pocoo.org/docs/dev/templates/#round
    """
    template = Template('{{ number|round }}')
    text = template.render(number=42.555)
    assert text == "43.0"
    
    template = Template('{{ number|round(2, "floor") }}')
    text = template.render(number=42.555)
    assert text == "42.55"
    
    
if __name__ == "__main__":
    #
    round()