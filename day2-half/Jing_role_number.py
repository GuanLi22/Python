import random
import string

for i in range(1, 5):
    print()

    for j in range(1, 5):
        head = random.choice(string.ascii_uppercase)
        data = string.ascii_uppercase + string.digits
        car_plate = "".join(random.sample(data, 5))
        print(f"京{head}•{car_plate}", end=" ")



