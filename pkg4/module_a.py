from __future__ import print_function

def action_a():
    from . import module_b
    print(module_b.action_b.__name__)
