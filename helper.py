import random


import random

def random_phone_number():
    words = ["SPAM", "BY", "ADNANBOOT", "ANJAY", "MABAR"]
    return " ".join(random.choices(words, k=random.randint(3, 5)))


    start_digits = "8" + str(random.choice(prefix))
    middle_digits = str(random.randint(10000000, 99999999))
    random_number = start_digits + middle_digits

    return str(random_number)


def random_single_number():
    return str(random.randint(0, 9))

