#Write a Python function called max_num()to find the maximum of three numbers
def max_num(num1, num2, num3):
    x=0
    if x < num1: x = num1
    if x < num2: x = num2
    if x < num3: x = num3
    return x
max = max_num(1,2,3)
print(max)

#Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(list):
  if len(list) == 0:
    return 0
  
  prod = list[0]

  if len(list) > 1:
    for i in list[1:]:
      prod = prod * i

  return prod