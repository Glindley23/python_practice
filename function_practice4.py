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

#Write a Python function called rev_string() to reverse a string.
def rev_string(strng):
  return strng[::-1]

print(rev_string('This is a string'))

#Write a Python function called num_within() to check whether a number falls in a given range.
def num_within(num, low_num, high_num):
  if num >= low_num and num <= high_num:
    return True
  else: return False

print(num_within(1,1,2))
print(num_within(4,5,7))