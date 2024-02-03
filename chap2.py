#import tlp as toys (but I do not want to prefix everything with toys)
#so.
from tlp import *



def is_lat(lst):
    if(type(lst) == list):
        if(is_null(lst)):
            return True
        elif(is_atom(car(lst))):
            return (is_lat(cdr(lst)))
        else:
            return False



