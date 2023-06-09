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

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.

triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)