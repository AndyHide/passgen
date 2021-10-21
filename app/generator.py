import hashlib

from transliterate import translit


def change_x(x):
    if x > 68:
        x = x - 68
    return x

def count_iterations(secret):
    iterations = 0
    for letter in secret:
        iterations += ord(letter)
    iterations *= 356473
    iterations = 800000 + iterations % 400000
    return iterations


def generate_password(username, secret, length):
    # p = hashlib.sha256()
    tr_username = translit(username, language_code='ru', reversed=True)
    tr_secret = translit(secret, language_code='ru', reversed=True)
    b_username = bytes(tr_username, 'utf-8')
    b_secret = bytes(tr_secret, 'utf-8')
    iterations = count_iterations(tr_secret)
    # p.update(b_username)
    # p.update(b_secret)
    p = hashlib.pbkdf2_hmac('sha256', b_username, b_secret, iterations, 256)

    # symbols = string.digits + string.ascii_uppercase + string.ascii_lowercase + string.punctuation
    symbols = "23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz!#$%&*-<=>?@"
    # print(f"symbols: {symbols}")
    # decimal_hash = int(p.hexdigest(), 16)
    decimal_hash = int(p.hex(), 16)
    # print(f"hex hash: {p.hex()}")

    listed_hash = list(str(decimal_hash))
    paired_integers = [int(a + b) for a, b in list(zip(listed_hash, listed_hash[1:]))[::2]]
    # print(f"integers: {paired_integers}")
    paired_integers = [change_x(int(x)) for x in paired_integers]
    # print(f"integers: {paired_integers}")
    password = ''.join([symbols[x] for x in paired_integers])
    # print(f"password length: {len(password)}")

    if not (length == 0 or length >= len(password) - 1):
        password = password[:length]

    return password


if __name__ == "__main__":
    username = input("Enter username:")
    secret = input("Enter secret:")
    length = int(input("Enter length:"))

    password = generate_password(username, secret, length)
    print(f"Password: {password}")
