#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('learn_jinja2.p01_manage_template', 'templates'))

if __name__ == "__main__":
    template = env.get_template("hello.txt")
    text = template.render(name="Jack")
    assert text == "Hello Jack!"
