from __future__ import print_function
def action_b():
    from . import module_a
    print(module_a.action_a.__name__)
