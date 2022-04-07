def factorial_iter(num):
    factorial=1
    for i in range(num):
        factorial=factorial*(i+1)
    return factorial
f=factorial_iter
print(f)

