from datetime import datetime, timedelta
birthday = input('When is your birthday (dd/mm/yyyy) : ')
# strptime(date_string, 'format')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('Birthday: ' + str(birthday_date))
one_day = timedelta(days=1)
birthday_eve = birthday_date - one_day
print('Day before Birthday :' + str(birthday_eve))
