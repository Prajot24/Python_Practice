
def my_gen():
    for i in range(30):
        yield i

p = my_gen()

print(next(p))
print(next(p))

for i in p:
    print(next(p))