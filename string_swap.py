import random

def sentence(list,num):
    i = 0
    s = ""
    while (i < num):
        s = s + list[i] + " "
        i += 1
    return s

def string_swap(string_1,string_2):
    split_index = random.randint(1,len(string_1))

    a = string_1.split(' ',split_index)
    b = string_2.split(' ',split_index)

    a_1 = sentence(a,len(a)-1)
    a_2 = a[len(a)-1]

    b_1 = sentence(b,len(b)-1)
    b_2 = b[len(b)-1]

    new_string_1 = b_1 + a_2
    new_string_2 = a_1 + b_2

    strings = [new_string_1,new_string_2]

    return(strings)