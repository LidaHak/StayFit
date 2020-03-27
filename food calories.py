import json
import csv

print("Hello, this is the app to calculate your calories. PLease input the folowing informaton. ")
while(True):
    try:
      weight = int(input("Enter your weight(in kg): "))
      break
    except:
         print("The answer is invalid")
while(True):
    try:
      height = int(input("Enter your height(in cm): "))
      break
    except:
         print("The answer is invalid")
while(True):
    try:
      age = int(input("Enter your age(in years): "))
      break
    except:
         print("The answer is invalid")
BMR1 = 0
while(True):
    gender = input("Male or Female?")
    if gender.lower() == 'male':
        BMR1 += (10 * weight) + (6.25 * height) - (5 * age) + 5
        print(BMR1)
        break
    else:
        if gender.lower() == 'female':
            BMR1 += (10 * weight) + (6.25 * height) - (5 * age) - 161
            print(BMR1)
            break
        else:
            print("The answer is invalid")
while(True):
    try:
        activitystatus = input('''Please choose one of the options
                            1.sedentary (little or no exercise)
                            2.lightly active (light exercise/sports 1-3 days/week)
                            3.moderately active (moderate exercise/sports 3-5 days/week)
                            4.very active (hard exercise/sports 6-7 days a week)
                            5.extra active (very hard exercise/sports & physical job or 2x training)
                            ''')
        if activitystatus == "1":
            BMR2 = BMR1 * 1.2
            print(BMR2)
            break
        if activitystatus == "2":
            BMR2 = BMR1 * 1.375
            print(BMR2)
            break
        if activitystatus == '3':
            BMR2 = BMR1 * 1.55
            print(BMR2)
            break
        if activitystatus == '4':
            BMR2 = BMR1 * 1.725
            print(BMR2)
            break
        if activitystatus == '5':
            BMR2 = BMR1 * 1.9
            print(BMR2)
            break
        else:
            print("The answer is invalid")
    except:
        pass
while(True):
    try:
        goals = int(input('''Please, choose one of the following options: I want to
                        1. loose weight,
                        2. mantain my weight,
                        3. gain weight
                        4. get to an ideal weight
                        '''))
        break
    except Exception:
        print("The answer is invalid")
if goals == '1':
    BMR2 -= 500
if goals == '2':
    BMR2 = BMR2
if goals == '3':
    amount = input("How much you want to gain during the week? 1 pound(~0,4kg) or 2 pounds(~0,9kg)?")
    if goals == "1":
        BMR2 += 500
    else:
        BMR2 += 1000
print("So, this is the amount of calories you shall take to reach your goal:  " + str(BMR2))
# userinitialdata
userinitialdata = {'weight': weight,
                    'height': height,
                    'age': age,
                    'gender': gender
                    }
with open('userinitialdata.json') as data_file:
    data = json.load(data_file)
j = json.dumps(userinitialdata)
with open('userinitialdata.json', 'w') as f:
    f.write(j)
    f.close()




















