import json
import datetime
import os
from usda import UsdaClient
import difflib
import pandas as pd
import xlrd


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
        activity_status = input('''Please choose one of the options 
                                   \r\tEnter '1' if sedentary (little or no exercise) 
                                   \r\tEnter '2' if lightly active (light exercise/sports 1-3 days/week) 
                                   \r\tEnter '3' if moderately active (moderate exercise/sports 3-5 days/week) 
                                   \r\tEnter '4' if active (hard exercise/sports 6-7 days a week) 
                                   \r\tEnter '5' if extra active (very hard exercise/sports & physical job or 2x training) 
                                   \r\t> ''')
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
            BMR2 += 500
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
    with open("user_data.json", "w+") as Writefile:
        json.dump(user_initial_info, Writefile, indent=True)
    return BMR2


def exit_app(user_initial_data, daily_calories, person_dict):
    user_initial_data["calories"] = daily_calories
    person_dict.append(user_initial_data)
    with open("daily_calories.json", "a+") as WRITE_FILE:
        json.dump(person_dict, WRITE_FILE, indent=True)
    exit("Bye")


def print_date_used_calories(text, person_dict):
    seeked_date = text[5:]
    for d in person_dict:
        if d["date"] == seeked_date:
            print("In %s you have used %s calories" % (seeked_date, d["calories"]))
            break
        else:
            print("There is no data for current date")


def find_food(daily_calories_amount, text, client, calories_limit):
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


def exercise_calories(daily_calories, text):
    file_location = r'C:\\Users\\TAKIKIDA\\Downloads\\exercise_database.xlsx'
    workbook = xlrd.open_workbook(file_location)
    excel_file = pd.read_excel('C:\\Users\\TAKIKIDA\\Downloads\\exercise_database 2.xlsx')
    format = ['Exercise Name', 'Calories per minute']
    df_selected = excel_file[format]
    exercise_type = text[8:]
    print(exercise_type)
    first_list = excel_file['Exercise Name']
    match_result = difflib.get_close_matches(exercise_type, first_list)

    for item in range(len(match_result)):
        print('For %s type %i' % (match_result[item], item))
    while True:
        try:
            exercise = match_result[int(input())]
            exercise_time = int(input("Exercise Time in minutes:"))

            for el in df_selected.values:
                if el[0] == exercise:
                    burnt = float(el[1]) * exercise_time
                    print('you have burnt %f calories' % burnt)
                    daily_calories -= burnt
                    return daily_calories
        except ValueError:
            print('Enter correct values')
            break


def main():
    print("Hello, this is the app to calculate your calories ")
    with open("user_data.json", "a+"):
        pass
    if os.stat("user_data.json").st_size == 0:
        print("PLease input the following information... ")
        calories_limit = read_user_data()
    else:
        with open("user_data.json", "r") as read_file:
            calories_limit = float(json.loads(read_file.read())["calories_limit"])

    client = UsdaClient('7wAkGt3olo20fa4ylx2hQr1ege8R4hZsGchImWt1')
    foods_list = client.list_foods(1)
    for _ in range(1):
        food_item = next(foods_list)
        # print(food_item.name)
    daily_calories = 0
    with open("daily_calories.json", "w+"):
        pass
    if os.stat("daily_calories.json").st_size == 0:
        with open("daily_calories.json", "w+") as write_file:
            json.dump([], write_file)
    with open("daily_calories.json", "r") as read_file:
        person_dict = json.loads(read_file.read())
    with open("daily_calories.json", "w+") as write_file:
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

    print("""Available Commands: 
                  \r1. Type the food name.
                  \r2. Type "calories" to view your calories.
                  \r3. Type date(yyyy-ww-dd) to view your calories at particular date.
                  \r4. Type "workout " +  name of the exercise to view your calories burnt during exercising
                  \r5. Type "exit" to exit the app.
                      """)

    while True:
        print("Enter command")
        text = input(">")
        if text == "exit":
            exit_app(user_initial_data, daily_calories, person_dict)
        elif "date" in text:
            print_date_used_calories(text, person_dict)
            continue
        elif text == "calories":
            print("Today you have consumed %i calories" % daily_calories)
            continue
        elif "workout" in text:
            daily_calories = exercise_calories(daily_calories, text)
            continue
        try:
            daily_calories = find_food(daily_calories, text, client, calories_limit)
        except ValueError:
            print("Food not found, try to write another food name")


main()
