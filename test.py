import sys
PY = sys.version[0]

if PY == '2':
    from pkg1 import module_a as a1
    a1.action_a()

from pkg2 import module_a as a2
from pkg3 import module_a as a3
from pkg4 import module_a as a4
from pkg4_2 import module_a as a4_2

a2.action_a()
a3.action_a()
a4.action_a()
a4_2.action_a()
