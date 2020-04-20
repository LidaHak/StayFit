import datetime
import json
import os
from usda import UsdaClient


def read_user_data():
    while True:
        try:
            weight = int(input("Enter your weight(in kg): "))
            if weight > 150:
                raise ValueError
            else:
                break
        except ValueError:
            print("Please, enter correct values!")
    while True:
        try:
            height = int(input("Enter your height(in cm): "))
            if height > 250:
                raise ValueError
            else:
                break
        except ValueError:
            print("Please, enter correct values!")
    while True:
        try:
            age = int(input("Enter your age(in years): "))
            if age > 120:
                raise ValueError
            else:
                break
        except ValueError:
            print("Please, enter correct values!")
    while True:
        gender = input("Male or Female? ")
        if gender.lower() == 'male':
            BMR1 = (10 * weight) + (6.25 * height) - (5 * age) + 5
            break
        elif gender.lower() == 'female':
            BMR1 = (10 * weight) + (6.25 * height) - (5 * age) - 161
            break
        else:
            print("Please, enter correct values!")
    while True:
        activity_status = input('''Please choose one of the options \r\tEnter '1' if sedentary (little or no 
        exercise) \r\tEnter '2' if lightly active (light exercise/sports 1-3 days/week) \r\tEnter '3' if moderately 
        active (moderate exercise/sports 3-5 days/week) \r\tEnter '4' if active (hard exercise/sports 6-7 days a 
        week) \r\tEnter '5' if extra active (very hard exercise/sports & physical job or 2x training) \r\t> ''')
        if activity_status == "1":
            BMR2 = BMR1 * 1.2
            break
        elif activity_status == "2":
            BMR2 = BMR1 * 1.375
            break
        elif activity_status == '3':
            BMR2 = BMR1 * 1.55
            break
        elif activity_status == '4':
            BMR2 = BMR1 * 1.725
            break
        elif activity_status == '5':
            BMR2 = BMR1 * 1.9
            break
        else:
            print("Please, enter correct values!")
    while True:
        goals = input('''Please, choose one of the following options: I want to
                         \rEnter '1' if you want to loose weight,
                         \rEnter '2' if you want to maintain my weight,
                         \rEnter '3' if you want to gain weight
                         \r> ''')
        if goals == '1':
            BMR2 -= 500
            break
        if goals == '2':
            BMR2 = BMR1
            break
        if goals == '3':
            amount = input("How much you want to gain during the week? 1 pound(~0,4kg) or 2 pounds(~0,9kg)?")
            if amount == "1":
                BMR2 += 500
            else:
                BMR2 += 1000
            break
        else:
            print("Please, enter correct values!")
    print("So, this is the amount of calories you shall take to reach your goal: " + str(BMR2))
    user_initial_info = {
        'weight': weight,
        'height': height,
        'age': age,
        'gender': gender,
        'calories_limit': BMR2}
    with open("data_file.json", "w+") as Writefile:
        json.dump(user_initial_info, Writefile, indent=True)
    return BMR2


def exit_app():
    user_initial_data["calories"] = daily_calories
    person_dict.append(user_initial_data)
    with open("daily_calories2.json", "w+") as WRITE_FILE:
        json.dump(person_dict, WRITE_FILE, indent=True)
    exit("Bye")


def print_date_used_calories():
    user_input_date = text[5:]
    for d in person_dict:
        if d["date"] == user_input_date:
            print("In %s you have used %s calories" % (user_input_date, d["calories"]))
            break
        else:
            print("There is no data for current date")


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


print("Hello, this is the app to calculate your calories ")
if os.stat("data_file.json").st_size == 0:
    print("PLease input the following information. ")
    calories_limit = read_user_data()
else:
    with open("data_file.json", "r") as read_file:
        calories_limit = float(json.loads(read_file.read())["calories_limit"])

client = UsdaClient('7wAkGt3olo20fa4ylx2hQr1ege8R4hZsGchImWt1')
foods_list = client.list_foods(1)
for _ in range(1):
    food_item = next(foods_list)
    # print(food_item.name)
daily_calories = 0
if os.stat("daily_calories2.json").st_size == 0:
    with open("daily_calories2.json", "w+") as write_file:
        json.dump([], write_file)

with open("daily_calories2.json", "r") as read_file:
    person_dict = json.loads(read_file.read())

with open("daily_calories2.json", "w+") as write_file:
    json.dump(person_dict, write_file, indent=True)

for i in range(len(person_dict)):
    if person_dict[i]["date"] == datetime.datetime.today().date().isoformat():
        daily_calories = float(person_dict[i]["calories"])
        del person_dict[i]
        break

user_initial_data = {
    'date': datetime.datetime.today().date().isoformat(),
    'calories': daily_calories
}

print("Commands 1.food name, 2.calories, 3.date yyyy-MM-dd, 4.exit, 5.Add new food name")

while True:
    print("Enter command")
    text = input()
    if text == "Add new food name":
        print("ok")
        continue
    if text == "exit":
        exit_app()
    elif "date" in text:
        print_date_used_calories()
        continue
    elif text == "calories":
        print("Today you have consumed %i calories" % daily_calories)
        continue
    try:
        daily_calories = find_food(daily_calories)
    except:
        print("Food not found, try to write another food name")
        continue
