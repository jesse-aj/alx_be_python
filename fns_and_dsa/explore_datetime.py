from datetime import datetime, timedelta


def display_curent_datetime():
    current_date = datetime.now()
    print(current_date.strftime("%Y-%m-%d  %H:%M:%S"))
    return current_date


def calculate_future_date(current_date):
    num_days = int(input("Enter the number of days: "))
    future_date = current_date + timedelta(num_days)
    print(future_date.strftime("%Y-%m-%d"))
    return future_date


current_date = display_curent_datetime()
calculate_future_date(current_date)
