#REMOVE PASS AND FIX THE FUNCTION
def sum_of_products(list1, list2):
    sum = 0
    for num in list1:
        sum += list1[list1.index(num)] * list2[list1.index(num)]
    return sum

if __name__ == '__main__':
   #REMOVE PASS AND YOUR CODE GOES HERE
    sum = sum_of_products(list1, list2)
    print(sum)