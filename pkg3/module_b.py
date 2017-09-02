from __future__ import print_function

def action_b():
    print(action_a.__name__)

from .module_a import action_a
