def to_binary_representation(number):
    return bin(number)[2:]
try:
    input_number = int(input("Enter a positive integer: "))
    binary_result = to_binary_representation(input_number)
    print(f"The binary representation of {input_number} is: {binary_result}")
except ValueError:
    print("Error: Please enter a valid positive integer.")
if __name__ == '__main__':
    def find_factors(number):
        factors = []
        for i in range(1, number + 1):
            if number % i == 0:
                factors.append(i)
        return factors
    try:
        input_number = int(input("Enter an integer: "))
        result_factors = find_factors(input_number)
        print(f"The factors of {input_number} are: {result_factors}")
    except ValueError:
        print("Error: Please enter a valid integer.")
if __name__ == '__main__':
    def is_prime(number):
        if number <= 1:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True
    try:
        input_number = int(input("Enter an integer: "))
        if is_prime(input_number):
            print(f"{input_number} is a prime number.")
        else:
            print(f"{input_number} is not a prime number.")
    except ValueError:
        print("Error: Please enter a valid integer.")
if __name__ == '__main__':
    def encrypt_message(message):
        encrypted_message = message.replace(" ", "")[::-1]
        return encrypted_message
    input_message = input("Enter a message: ")
    encrypted_result = encrypt_message(input_message)
    print(f"Encrypted Message: {encrypted_result}")
if __name__ == '__main__':
    import random
    import string
    def encrypt_message(message):
        interval = random.randint(2, 20)
        random_letters = ''.join(random.choice(string.ascii_lowercase) for _ in range(interval - 1))
        encrypted_message = ''.join(
            char if char.isalpha() else random_letters[i % len(random_letters)] for i, char in enumerate(message))
        return encrypted_message, interval
    input_message = input("Enter a message: ")
    encrypted_result, interval_used = encrypt_message(input_message)
    print(f"Encrypted Message: {encrypted_result}")
    print(f"Interval Used: {interval_used}")
if __name__ == '__main__':
    def decrypt_message(encrypted_message, interval):
        decrypted_message = ''
        j = 0
        for i, char in enumerate(encrypted_message):
            if char.isalpha():
                decrypted_message += char
            else:
                decrypted_message += ' ' if interval == 1 else encrypted_message[i + interval - 1]
                j += 1

        return decrypted_message


    # Example usage:
    encrypted_message = "sxyexynxydxy cxyhxyexyexysxye"
    interval_used = 2
    decrypted_result = decrypt_message(encrypted_message, interval_used)
    print(f"Decrypted Message: {decrypted_result}")