t1 = (1, 2, "hello")
print(t1[2]) # hello

t2 = (1, 2, 'hello', 3, 4, 'hello')
print(t2.index('hello')) # 2
print(t2.count('hello')) # 2
print(len(t2)) # 6

t3 = (1, 2, ['leo', 'laurent'])
print(t3[1])  # 2
print(t3[2])  # ['leo', 'laurent']
print(t3[2][0]) # leo
print(len(t3)) # 3