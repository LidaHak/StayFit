import json
import datetime
import os
from usda import UsdaClient


def read_user_data():
    while True:
        try:
            weight = int(input("Enter your weight(in kg): "))
            height = int(input("Enter your height(in cm): "))
            age = int(input("Enter your age(in years): "))
            break
        except ValueError:
            print("Please, enter correct values!")
    while True:
        gender = input("Male or Female? ")
        if gender.lower() == 'male':
            BMR1 = (10 * weight) + (6.25 * height) - (5 * age) + 5
            # print(BMR1)
            break
        elif gender.lower() == 'female':
            BMR1 = (10 * weight) + (6.25 * height) - (5 * age) - 161
            # print(BMR1)
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
    # print(BMR2)
    while True:
        goals = input('''Please, choose one of the following options: I want to
                         \rEnter '1' if you want to loose weight,
                         \rEnter '2' if you want to maintain my weight,
                         \rEnter '3' if you want to gain weight
                         \r> ''')
        if goals == '1':

            amount = input("How much you want to loose during the week? 1 pound(~0,4kg) or 2 pounds(~0,9kg)? ")
            if amount == '1':
                BMR2 -= 500
            else:
                BMR2 -= 1000
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
    with open("data_file.json", "w+") as writeFile:
        json.dump(user_initial_info, writeFile, indent=True)
    return BMR2




















