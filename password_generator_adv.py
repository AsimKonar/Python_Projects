import secrets
import string
import math

class PasswordGenerator:

    def __init__(self):
        self.character = {
            "lower": string.ascii_lowercase,
            "upper": string.ascii_uppercase,
            "digit": string.digits,
            "symbol": string.punctuation
        }
    def generate_pool(self, lower, upper, digit, symbol):
        new_string = ""
        if lower:
            new_string += self.character['lower']
        if upper:
            new_string += self.character['upper']
        if digit:
            new_string += self.character['digit']
        if symbol:
            new_string += self.character['symbol']

        return new_string

    def generate_password(self, length, pool):
        password = ''.join(secrets.choice(pool) for _ in range(length))
        return password

    def check_entropy(self, pool, password):
        entropy = round(len(password) * math.log2(len(pool)), 2)
        return entropy

    def strength_meter(self, entropy):
        if entropy < 40:
            return "Week"
        if entropy < 50:
            return "Moderate"
        if entropy < 60:
            return "Strong"
        else:
            return "Very Strong"

def main():
    passwordgenerator = PasswordGenerator()
    try:
        length = int(input("Enter the Expected Length: "))
        if length <= 0:
            print("Length of the password should be Positive.")
            return
    except ValueError:
        print("Enter a Valid Input.")
        return

    lower = input("Do you want lowercase in your Password? (y/n): ").lower().strip() == "y"
    upper = input("Do you want uppercase in your Password? (y/n): ").lower().strip() == "y"
    digit = input("Do you want digit in your Password? (y/n): ").lower().strip() == "y"
    symbol = input("Do you want symbol in your Password? (y/n): ").lower().strip() == "y"

    pool = passwordgenerator.generate_pool(lower,upper,digit,symbol)

    if not pool:
        print("You Must Select at least one character type.")
        return
    password = passwordgenerator.generate_password(length, pool)

    entropy = passwordgenerator.check_entropy(password=password, pool=pool)

    strength = passwordgenerator.strength_meter(entropy)

    print("\nGenerated Password: " + password)
    print("Character Pool Size: " + str(len(pool)))
    print("Entropy: " + str(entropy))
    print("Strength: " + strength)

if __name__ == "__main__":
    main()




