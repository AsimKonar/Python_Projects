def prime_generator(n):
    l = []
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    for i in range(2, n):
        if is_prime[i]:
            l.append(i)
    return l
try:
    num = int(input("Enter a number till where all the Prime numbers will be printed: "))
    for i in prime_generator(num):
        print(i)
except Exception as e:
    print(f"Please Enter a Valid Integer. {e}")