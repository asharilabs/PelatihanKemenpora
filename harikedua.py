# bilangan = input('input bilangan: ')

# for i in range(int(bilangan) + 1):
#     if i != 0:
#         print('Hitung %d' %i)

# x = 3
# y = 3
# a = [1,2,3]
# b = [1,2,3]
# print( x is y)

# print(x is x)
# print([1,2,3] == [1,2,3])

# print ('123 ->' + (a is b))

lst = [1,2,3,4,5,['a','b','c','d']]
for x in lst:    
    if isinstance(x, list):
        for y in x:
            print(y)
    else:
        print (x)