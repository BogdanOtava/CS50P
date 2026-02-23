# https://cs50.harvard.edu/python/psets/2/nutrition/

def main():
    fruit = input("Item: ").lower()

    calories_amount = get_calories_amount(fruit)

    if calories_amount:
        print(calories_amount)
    else:
        print("")


def get_calories_amount(fruit: str):
    """Retrieves the calorie amount of the given fruit."""

    fruits_nutrition = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80,
    }

    return fruits_nutrition.get(fruit)


main()
