def generator():
    for i in range(1, 11):
        yield i

gen = generator()
for j in 10:
    print(next(gen))