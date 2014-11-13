

# this is a comment
'''
x = 3

y = 4.2

z = 'hello'
a = "world"
b = x + y
c = 8 / 3
d = 8 // 3
e = 8 % 3
f = 8 ** 3
# string concat
g = z + a

#h = int(input("enter a number: "))
if h < 0:
  h = 0
  print('negative changed to zero')
elif h == 0:
  print('zero')
elif h == 1:
  print('single')
else: print('more')

words = ['blah', 'fhfhf', 'asdfsdfsdfsdfds']
for w in words:
  print(w, len(w))
for i in range(0, 10, 3):
  print(i)
i = list(range(6))
print(i)
def ask_ok(prompt, retries=4, complaint = 'yes or no'):
  while True:
    ok = input(prompt)
    if ok in('y', 'ye', 'yes'):
      return True
    if ok in('n', 'no', 'nop', 'nope'):
      return False
    retries = retries - 1
    if retries < 0:
      raise IOError('stupid user')
    print(complaint)

#ask_ok('ok to overwrite file?', 2)

i = 5
def f(arg=i):
  print(arg)
i = 7
# f returns 5
f()

def j(x, L=[]):
  L.append(x)
  return L

print(j(1))
print(j(4))
print(j(7))

while True:
  for i in ["/","-","|","\\","|"]:
    print("%s\r" % i),
#print("How old are you?"),
age = input('how old are oyu')
#print("How tall are you?"),
height = input('how tall')
#print("How much do you weigh?"),
weight = input('weight?')

print("So, you're %s old, %s tall and %s heavy.") % (age, height, weight)

def f(ham: 42, eggs: int = 'spam') -> "Nothing to see here":
  print("Annotations:", f.__annotations__)
  print("Arguments:", ham, eggs)

f('blah', int = 'www')
'''
'''
age = 20
gender = 'female'

if age >= 21 and (gender =='female' or gender == 'male'):
  print('go drink')
else:
  print('go have parents buy drink')

for x in range(20, -50, -5):
  print('{0} to the {1} power is {2}'.format(x, 2, x**2))

evens = []
for x in range(0, 20, 2):
    for y in range(3, 15, 3):
        if x == 10:
            evens.append((x, x ** 2, y, y ** 3, x + y))


def sum(a, b):
    return a + b

a = sum(3, 4)

from math import pi
def vol(height, radius):
    return pi * radius**2 * height


b = vol(10, 30) # radius = 10 height = 30
'''
def bin2dec():
    w = str(input('enter a binary number: '))
    d = int(w, 2)
    print('your decimal is ', d)
    return d

def dec2bin():
    w = int(input('enter a decimal number: '))
    d = bin(w)
    print('your binary number is: ', d)
    return d

#bin2dec()
#dec2bin()

def bin(bin):
    sum = 0
    for index, bit in enumerate(bin[::-1]):
        sum += int(bit) * (2**index)
    return sum

dec = bin('1010111')
print(dec)

a = 4


