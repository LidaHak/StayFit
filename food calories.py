import json


print("Hello, this is the app to calculate your calories. PLease input the folowing informaton. ")
try:
      weight = int(input("Enter your weight(in kg): "))
      height = int(input("Enter your height(in cm): "))
      age = int(input("Enter your age(in years): "))
except Exception:
    print("Try again, please")

BMR1 = 0
gender = input("Male or Female?")
if gender.lower() == 'male':
    BMR1 += (10 * weight) + (6.25 * height) - (5 * age) + 5
if gender.lower()== 'female':
    BMR1 += (10 * weight) + (6.25 * height) - (5 * age) - 161
print(BMR1)
activitystatus = input('''Please choose one of the options
                        1.sedentary (little or no exercise)
                        2.lightly active (light exercise/sports 1-3 days/week)
                        3.moderately active (moderate exercise/sports 3-5 days/week)
                        4.very active (hard exercise/sports 6-7 days a week)
                        5.extra active (very hard exercise/sports & physical job or 2x training)
                        ''')

if activitystatus == "1":
    BMR2 =  BMR1 * 1.2
    print(BMR2)
if activitystatus == "2":
    BMR2 = BMR1 * 1.375
    print(BMR2)
if activitystatus == '3':
    BMR2 = BMR1 * 1.55
    print(BMR2)
if activitystatus == '4':
    BMR2 =  BMR1 * 1.725
    print(BMR2)
if activitystatus == '5':
    BMR2 = BMR1 * 1.9
    print(BMR2)

# ideal weight calculator
# ideal_weight =


try:
    goals = int(input('''Please, choose one of the following options: I want to
                    1. loose weight,
                    2. mantain my weight,
                    3. gain weight
                    4. get to an ideal weight
                    '''))
except Exception:
    print("Try again, please")


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


# food
with open("data.csv", 'r') as f:
    dic = {}
    for i in f:
        data = i.split('--')
        cat, name, cal = data[0], data[1], data[2]
        dic[name] = {"cat":cat, "cal":cal}
    # print(dic)

file = open("food.json", "w")
file.write(str(dic))
file.close()

# daily_products

daily_food = input("Enter the foods you ate today separated by space: ")
userList = daily_food.split()
print("The products are ", userList)



print("Calculating sum of element of input list")
sum = 0
for num in userList:
    sum += int(num)
print("Sum of current calories= ", sum)





















