#Unsorted list of tuples: [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)] 
#Sorted list of tuples: [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

report_card = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
sorted_report_card = sorted(report_card, key = lambda i: i[1])
print(sorted_report_card)

list = [3, 6, 9, 2]

cubed = [num * num * num for num in list]
print(cubed)

even_odd = lambda x: True if x % 2 == 0 else False
print([even_odd(x) for x in [3,6,9,2]])

big_list = [num + 1 for num in range(100)]
print(big_list)

sentence = "The quick brown fox jumped over the fence."
print({word: len(word) for word in sentence.split()})