import random
import string


def password_generator(length, use_spl_chr):

    password = string.ascii_letters + string.digits

    if use_spl_chr:
        password += string.punctuation
    # x = list(random.choice(password) for i in range(length))
    final_password = ''.join(list(random.choice(password) for i in range(length)))

    return final_password

def strength_checker(password):
    st = 0
    if any(c.islower() for c in password):
        st += 1
    if any(c.isupper() for c in password):
        st += 1
    if any(c.isdigit() for c in password):
        st += 1
    if any(c in string.punctuation for c in password):
        st += 1

    if len(password) >= 12:
        st += 1

    if st <= 2:
        return "Week"
    elif st <= 4:
        return "Moderate"
    else:
        return "Strong"

def main():

    try:
        length = int(input("Enter the expected length of the password: "))
    except ValueError:
        print("Invalid Input.")
        return

    if length <= 0:
        print("Please enter a positive.")
        return

    use_spl_chr = input("Do you want to use special character in your password?: (y/n)").lower().strip() == "y"

    password = password_generator(length, use_spl_chr)

    print("\nGenerated Password:" + password)
    print(f"Your password Strength is {strength_checker(password)}")

if __name__ == "__main__":
    main()