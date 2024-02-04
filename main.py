def sum_of_products(list1, list2):
    sum = 0
    count = 0
    if len(list1) == len(list2):
        for i in list1:
            sum += int(list1[count]) * int(list2[count])
            count += 1
        return sum

list1 = input()
list2 = input()

list1 = list1.split()
list2 = list2.split()

if __name__ == '__main__':
    sum = sum_of_products(list1, list2)
    print(sum)