import random
import string

def passwordgen():
    special_char = "!@#$%^&*()?"
    char = special_char+string.ascii_uppercase+string.digits+string.ascii_lowercase
    word = ''.join(random.choice(char) for _ in range (4)) + ''.join(random.choice(special_char) for _ in range(1))
    p = ''.join(random.choice(special_char) for _ in range(1))
    a = ''.join(random.choice(string.ascii_uppercase) for _ in range(1))
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(1))
    ss = ''.join(random.choice(string.digits) for _ in range(1))
    return p + a + s+ ss + word


def main():
    return


if __name__ == '__main__':
    main()

print(passwordgen())