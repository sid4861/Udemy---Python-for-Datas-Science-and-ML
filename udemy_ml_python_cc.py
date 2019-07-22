########part1#######
a = 10
b = 100

print(a+b)
print(a-b)
print(b/a)
print(b%a)
print(2**3)

c = 10
name = "Siddharth"
print("number is {}, name is {}".format(c, name))

print(name[0:])
print(name[:4])
print(name[0:4])

#lists

my_list = [1,2,3,4,5]
print(my_list[0:])
print(my_list[:3])
print(my_list[0:3])

my_list_nested = [1,2,3,4,[1,2,3,4]]
print(my_list_nested[4][3])


########part2#######

#dictionaries

dict1 = {'k1':"Siddharth", "k2":"Lodha"}
print(dict1["k1"])

dict2 = {'k1':[1,2,3,4,5]}
print(dict2['k1'][3])

dict3 = {'k1':{'inner_key':[1,2,3,4,5]}}
print(dict3['k1']['inner_key'][4])

#tuples
my_tuple=(1,2,3,4,5)
print(my_tuple)

#not allowed
#my_tuple[0] = 10

#sets - unique values
my_set = {1,2,3,4,5,55,5,5,5,4,5}
print(my_set)

my_list1 = [1,1,2,2,3,3,4,4,5,5]
print(set(my_list1))

#conditional operators

print(1 > 2)
print(1 < 2)
print(1 >= 2)
print(1 <= 2)
print(1 != 2)
print(1 == 2)

if 10>8 and 10>5:
    print('and condition satisfied')
else:
    print('NA')

if 100<3 and 100<4:
    print('and')
elif 3==3:
    print('elif')
else:
    print('else')


########part3#######

seq = [1,2,3,4,5]
for num in seq:
    print(num)

for num in range(5):
    print(num)
for num in range(1,6):
    print(num)
i = 1
while i<5:
    print("num is {}".format(i))
    i+=1

out=[]
seq2 = [1,2,3,4,5]
for num in seq2:
    out.append(num**2)
print(out)

#list comprehensions

out = [num**2 for num in seq2]
print(out)

#functions

def my_func(name="default name"):
    print("Hi "+name)

my_func("Siddharth")
my_func()
print(my_func)

def my_func2(num):
    """
        This is a docstring
        this function squares the number passed to it as an argument
    """
    return num**2

output = my_func2(5)
print(output)
          
########part4#######

#map function

def times2(num):
    return num*2

seq = [1,2,3,4,5]
print(list(map(times2, seq)))

#lambda function with map

print(list(map(lambda num: num*2, seq)))

#filter function

print(list(filter(lambda num: num%2==0, seq)))

#common methods

str1 = 'my Name is Siddharth'
print(str1.lower())
print(str1)

print(str1.upper())
print(list(str1.split()))

str2 = "HI Siddharth #weekend"
print(list(str2.split('#')))

print(list(dict1.keys()))
print(list(dict1.values()))
print(list(dict1.items()))

seq = [1,2,3,4,5]
print(seq.pop())
print(seq)
print(seq.pop(1))
print(seq)

#tuple unpacking

for a,b in dict1.items():
    print("keys are {}".format(a))
    print("values are {}".format(b))
