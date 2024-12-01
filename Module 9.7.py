def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args)

        flag = True
        for i in range(2, int(result / 2 + 0.5)):
            if result % i == 0:
                print("Составное")
                flag = False
                break
        if flag:
            print("Простое")
        return result
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(1, 1, 1)
print(result)