def Fibo_generator(upper_limit):
    counter = 0
    a = 0
    b = 1
    while counter <= upper_limit:
        lst = []
        c = a + b
        yield c
        a = b
        b = c
        counter +=1

a = Fibo_generator(9)
for i in a:
    print (i)


