import datetime

def search_friday_13(year, month):
    result = datetime.date(year, month, 13).weekday()
    print(result)
    if result == 4:
        return True
    else:
        return False


print(search_friday_13(2023, 1))