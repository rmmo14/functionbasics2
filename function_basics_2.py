# 1. Countdown from given paramater
def count(num):
    for x in range (num,-1,-1):
        print(x)

holder = count(8)

# 2. Print and return
def prinret(a,b):
    list = [a,b]
    print(list[0])
    return list[1]
hold = prinret(3,4)

# 3. first plus length
def firstlength(mylist):
    print(mylist[0] + len(mylist))
holder = firstlength([4,2,3,5])

# 4. greater than second value
def greater(my_list):
    empty = []
    count = 0
    for x in range (0,len(my_list)):
        if my_list[x] > my_list[1]:
            empty.append(my_list[x])
            count += 1
    print(count)
    return empty
holder = greater([1, 4, 5 , 7 ,8])

#5. length, that value
def func(size, value):
    for x in range (0,size):
        print(value)
holder = func(4,7)