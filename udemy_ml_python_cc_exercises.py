print(7**4)
s = "Hi there Siddharth!!"
print(s.split())
planet = "Earth"
diameter = 123456

print("The diameter of planet {} is {} km".format(planet, diameter))
my_list = [1,2,3,[1,2,[1,2,["Hello"]]],4,5]
print(my_list[3][2][2][0])
d = {'k1':[1,2,3,{'tricky':['oh', 'man', 'inception', {'target':[1,2,3,4,'Hello']}]}]}
print(d['k1'][3]['tricky'][3]['target'][4])

def domainGet(email):
    l = email.split('@')
    return l[1]

print(domainGet('sid@gmail.com'))

input_str = str(input('Enter string : '))

def findDog(input_str):
    if ('dog' in input_str) or ('DOG' in input_str):
        return True
    else:
        return False

print(findDog(input_str))

input_str_list = input_str.split()
print(input_str_list)
count_dog = 0

def calculateDog(l):
    global count_dog
    for item in l:
        if item=='dog' or item=='Dog' or item=='DOG':
            count_dog+=1
    return count_dog

print('no of times dog occurs = {}'.format(calculateDog(input_str_list)))

print(list(filter(lambda item:item[0]!='s', input_str_list)))


def caught_speeding(speed, is_birthday):
    if is_birthday:
        if(speed <=65):
            return 'No ticket'
        elif(speed>=66 and speed <=85):
            return 'Small ticket'
        else:
            return 'Big ticket'
    else:
        if(speed<=60):
            return 'No ticket'
        elif(speed>=61 and speed<=80):
            return 'Small ticket'
        else:
            return 'Big ticket'


print(caught_speeding(81, True))
