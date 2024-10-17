def find_even_number(lst):
    even_number=[]
    for num in lst:
        if num%2==0:
            even_number.append(num)

    even_number.sort()
    return even_number
print(find_even_number([10,15,16,22,8]))

def remove_vowels(string):
    vowels='aeiouAEIOU'
    result=''

    for char in string:
        if char not in vowels:
            result+=char

    return result
print(remove_vowels("Hello world"))

for i in range(2,10):
    for j in range (1,10):
        print(f'{i}*{j}={j*i}')


def suma_b(a,b):
    print(a*b)

def mula_b(a,b):
    print(a*b)

suma_b(3,4)
mula_b(3,4)

n = int(input("자연수 입력: "))
lst=[]
for i in range(1,n+1):
    if n%i==0:
        lst.append(i)
print(lst)

a = int(input("정수1 입력: "))
b = int(input("정수2 입력: "))
lista=[]
listb=[]
listc=[]
for i in range(1,a+1):
    if a%i==0:
        lista.append(i)
for i in range(1,b+1):
    if b%i==0:
        listb.append(i)
if a>b:
    for j in lista:
        if j in listb:
            listc.append(j)
        
if a<b:
    for j in listb:
        if j in lista:
            listc.append(j)        
print(listc[-1])
