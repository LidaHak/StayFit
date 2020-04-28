def exercise_calories():
    excel_file = pd.read_excel('C:\\Users\\TAKIKIDA\\Downloads\\exercise_database.xlsx')
    exercise_type = input("Enter: ")
    first_list = excel_file['Exercise Name']
    second_list = exercise_type
    match_result = difflib.get_close_matches(second_list, first_list)
    print(match_result)
