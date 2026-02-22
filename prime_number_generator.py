def prime_generator(n):
    if n<2:
        return "Enter a number greater than 2."
    n_list = []
    for i in range(2,n+1):
        is_prime_num = True
        for j in range(2,int(i**0.5)+1):
            if i%j == 0:
                is_prime_num = False
                break
        if is_prime_num:
            n_list.append(i)
    return n_list

try:
    num = int(input("Enter a number till where all the Prime numbers will be printed: "))
    for i in prime_generator(num):
        print(i)
except Exception as e:
    print(f"Please Enter a Valid Interger. {e}")

