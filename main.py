def sum_of_products(list1, list2):
    sum = 0
    for num in list1:
        sum += list1[list1.index(num)] * list2[list1.index(num)]
    return sum

list1 = [1, 2, 3]
list2 = [4, 5, 6]

if len(list1) == len(list2):
   #REMOVE PASS AND YOUR CODE GOES HERE
    print(sum_of_products(list1, list2))