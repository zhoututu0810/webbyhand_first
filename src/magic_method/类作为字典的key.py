class Animal(object):
    print('Animal')

d1 = {Animal: Animal()}
print(d1.keys())
print(d1[Animal])