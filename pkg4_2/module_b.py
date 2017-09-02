from __future__ import print_function
def action_b():
    from .module_a import action_a
    print(action_a.__name__)
