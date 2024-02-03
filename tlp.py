def is_null(lst):
    if(type(lst) == list):
        return len(lst) == 0
    else:
        return False

def is_pair(lst):
    if (type(lst) == list):
        return (len(lst) == 2)
    else:
        return False

def is_atom(lst):
    return ((not is_null(lst)) and (not is_pair(lst)) and (not(type(lst) == list)))

def car(lst):
    if (type(lst) == list):
        return lst[0]
    else:
        return []


def cdr(lst):
    if (type(lst) == list):
        return lst[1:]
    else:
        return []


def cons(arg1, arg2):
    if(type(arg2) == list):
        arg2.insert(0,arg1)
        return arg2
    else:
        return []