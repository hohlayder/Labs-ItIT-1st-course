from my_package.modules import module_int
from my_package import make_line
import my_package

print(module_int.sum(1, 2, 3))
print(module_int.mult(2, 3, 4))
print(make_line('hello', 'world', '123', 'XDXDXD'))
print(my_package.substr('hello world', 1, 9))