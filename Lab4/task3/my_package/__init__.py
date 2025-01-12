from Lab4.task3.my_package.modules import module_int, module_str


def sum(*args):
    return module_int.sum(*args)


def mult(*args):
    return module_int.mult(*args)


def make_line(*args):
    return module_str.make_line(*args)


def substr(s, start, end):
    return module_str.substr(s, start, end)

