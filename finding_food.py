
def find_food(daily_calories_amount):
    foods_search = client.search_foods(text, 1)
    food_name = next(foods_search)
    print(food_name)

    report = client.get_food_report(food_name.id)

    for nutrient in report.nutrients:
        if nutrient.name == "Energy":
            print(nutrient.name, nutrient.value, nutrient.unit)
            daily_calories_amount += nutrient.value
            if (calories_limit - daily_calories_amount) > 0:
                print("You have %i calories left" % (calories_limit - daily_calories_amount))
            else:
                print("You have passed your daily limit by %i" % (daily_calories_amount - calories_limit))
            break
    return daily_calories_amount

