#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jinja2 import Template

def variables():
    """You can use a dot (.) to access attributes of a variable in addition 
    to the standard Python __getitem__ “subscript” syntax ([]).
    
    ref: http://jinja.pocoo.org/docs/dev/templates/#variables
    """
    template = Template('{{ user.name }}')
    text = template.render(user={"name": "Jack"})
    assert text == "Jack"
    
    template = Template('{{ user["name"] }}')
    text = template.render(user={"name": "Jack"})
    assert text == "Jack"
    
    
if __name__ == "__main__":
    #
    variables()