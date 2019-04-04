#!/usr/bin/python

import eel
eel.init('web')
eel.start('main.html')

import math  
print('  ')
print('  ')
print('  ')
print('Cubic function calculator')
print('                         by tun0')
a = input('Enter Your a:')
b = input('Enter Your b:')
c = input('Enter Your c:')
print('  ')
print('  ')
print('  ')
print("discriminant: {}".format(b*b - 4*a*c))
d = b*b - 4*a*c
D = math.sqrt(d)
A = a * 2
print("discriminant root: {}".format(D))
x1 = (b - D)
x2 = (b + D)
print("X1: {}".format(x1/A))
print("X2: {}".format(x2/A))

