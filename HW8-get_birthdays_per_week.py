from datetime import datetime, timedelta





def get_birthdays_per_week(users):

    days_of_week = {ord('0'): 'Monday:', ord('1'): 'Thuesday:', ord('2'): 'Wednesday:', ord('3'): 'Thursday:', ord('4'): 'Friday:', ord('5'): 'Saturday:', ord('6'): 'Sunday:'}
    delta = timedelta(days=1)
    current_birthday_list = []
    #визначаєм точку відліку (день з якого починаєм шукати іменинників) залежно від дня тижня: для пн - пт це наступний день, сб - поточний, нд - попередній,
    if datetime.now().weekday() == 5:
        time_zero_point = datetime.now()
    elif datetime.now().weekday() == 6:
        time_zero_point = datetime.now() - delta
    else:
        time_zero_point = datetime.now() + delta
        #для кожного дня починаючи з точки відліку...
    for i in range(7):
        current_datetime = time_zero_point + delta * i
        current_weekday = current_datetime.weekday()
        #... знаходим іменинників і додаємо їх у список іменинників
        for user in users:
            if user['birthday'].month == current_datetime.month and user['birthday'].day == current_datetime.day:
                current_birthday_list.append(user.get('name'))
        #...якщо поточний(ітерируємий) день не сб чи неділя виводим на друк список, попередньо вставивши поточний(ітерируємий) день тижня за допомогою метода translate та словника
        if current_weekday not in [5, 6]:
            if current_birthday_list:
                print(str(current_weekday).translate(days_of_week), ', '.join(current_birthday_list))
            #... і обнуляєм список іменинників (звісно якщо поточний(ітерируємий) день не сб чи неділя )
            current_birthday_list = []


# users = [
#     {'name': 'Чт1', 'birthday': datetime(year=1985, month=2, day=9)},
#     {'name': 'Пт2', 'birthday': datetime(year=1985, month=2, day=10)},
#     {'name': 'Пт1', 'birthday': datetime(year=1985, month=2, day=17)},
#     {'name': 'Сб', 'birthday': datetime(year=1987, month=2, day=11)},
#     {'name': 'Нд', 'birthday': datetime(year=1985, month=1, day=29)},
#     {'name': 'Пн', 'birthday': datetime(year=1985, month=1, day=30)},
#     {'name': 'Вт', 'birthday': datetime(year=1985, month=1, day=31)},
#     {'name': 'Ср', 'birthday': datetime(year=1985, month=2, day=1)},
#     {'name': 'Чт', 'birthday': datetime(year=1985, month=2, day=2)}
# ]

get_birthdays_per_week(users)










# def get_birthdays_per_week(users):
#
#     days_of_week = {ord('0'): 'Monday:', ord('1'): 'Thuesday:', ord('2'): 'Wednesday:', ord('3'): 'Thursday:', ord('4'): 'Friday:', ord('5'): 'Saturday:', ord('6'): 'Sunday:'}
#     delta = timedelta(days=1)
#     current_birthday_list = []
#
#     if datetime.now().weekday() == 0:
#         time_zero_point = datetime.now() - delta * 2
#     elif datetime.now().weekday() == 6:
#         time_zero_point = datetime.now() - delta
#     else:
#         time_zero_point = datetime.now()
#     for i in range(7):
#         current_datetime = time_zero_point + delta * i
#         current_weekday = current_datetime.weekday()
#         for user in users:
#             if user['birthday'].month == current_datetime.month and user['birthday'].day == current_datetime.day:
#                 current_birthday_list.append(user.get('name'))
#         if current_weekday not in [5, 6]:
#             if current_birthday_list:
#                 print(str(current_weekday).translate(days_of_week), ', '.join(current_birthday_list))
#             current_birthday_list = []
#
#
# get_birthdays_per_week(users)