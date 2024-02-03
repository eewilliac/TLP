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

