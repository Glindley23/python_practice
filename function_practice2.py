def arb_args(*args): 
        for i in args:
            print(i) 

def inner_func(int1, int2):
    def add_ints(int1, int2):
        return int1 + int2
    def subtract_ints(int1, int2):
        return int1 - int2
    return add_ints(int1, int2) - subtract_ints(int1, int2)

#print(inner_func(1, 2))

#arb_args(1, "five", True)

def lunch_lady(str1, str2="Mystery Meat"):
    print(str1 + ' ' + str2)

#lunch_lady("graham", "notmystery meat")
#lunch_lady('Andrew')

def sum_n_product(int1, int2):
    int_sum= int1 + int2
    int_prod= int1 * int2
    return int_sum, int_prod

#print(sum_n_product(5, 10))

alias_arg = arb_args

#alias_arg(1, "Five", False)



def arg_mean(*ints):
    total = 0
    for i in ints:
        total += i
    average = total / len(ints)
    return average
    
#print(arg_mean(1,2,3,4))



def arb_longest_string(*args):
  length = 0
  longest = ""
  for a in args:
    if len(a) > length:
      length = len(a)
      longest = a
      print(longest)
  return longest

arb_longest_string("caterpillar", "three", "very longerist")