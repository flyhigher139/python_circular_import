from __future__ import print_function
import pkg2.module_b

def action_a():
    print(pkg2.module_b.action_b.__name__)
