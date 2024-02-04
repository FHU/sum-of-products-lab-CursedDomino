def sum_of_products(list1, list2):
    sum = 0
    if len(num1) == len(num2):
        for i in num1:
            sum += int(num1[num1.index(i)]) * int(num2[num1.index(i)])
        return sum

num1 = input()
num2 = input()

if __name__ == '__main__':
    sum = sum_of_products(num1, num2)
    print(sum)