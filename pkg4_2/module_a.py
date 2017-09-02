from __future__ import print_function

def action_a():
    from .module_b import action_b
    print(action_b.__name__)
