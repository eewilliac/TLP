from chap2 import *

if __name__ == "__main__":
    lst = ['bacon','and','eggs']
    not_lst = [[lst],1,2,3]

    result = is_lat(lst)
    print("result:{}".format(result))
    print("result:{}".format(is_lat(not_lst)))