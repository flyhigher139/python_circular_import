from __future__ import print_function

def action_a():
    print(action_b.__name__)

from .module_b import action_b
