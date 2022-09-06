import random

def random_item (items):
    print(items[random.randint(0, len(items))])

animales = ["Oso Polar", "Tigre", "Puma"]

random_item(animales)


