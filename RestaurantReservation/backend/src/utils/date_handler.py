from datetime import time
import re


def get_day_range(partitioned_schedule):
    pattern = '[a-zA-Z/,/ /-]*'
    day_range = re.match(pattern, partitioned_schedule)
    if day_range.group(0):
        return get_days(day_range.group(0)), day_range.group(0)
    return None, None


def get_days(days):
    available_days = [
        'Mon',
        'Tues',
        'Wed',
        'Thu',
        'Fri',
        'Sat',
        'Sun'
    ]

    day_list = []
    for day in days.split(','):
        day = day.strip()
        if '-' in day:
            start_day, end_day = day.split('-')
            got_first = False
            for day in available_days:
                if got_first:
                    day_list.append(day)
                else:
                    if day == start_day.strip():
                        day_list.append(day)
                        got_first = True
                if day == end_day.strip():
                    break
        else:
            if day in available_days:
                if day not in day_list:
                    day_list.append(day)
    return day_list


def get_time_range(times):
    start, end = times.split('-')
    start_time = get_time(start)
    end_time = get_time(end)
    return f'{start_time}-{end_time}'


def get_time(t):
    pattern = '[\d/:]*'
    t_time = re.match(pattern, t.strip()).group(0)
    meridiem = t.split(t_time)[1].strip()
    min = '00'
    if ':' in t_time:
        min = t_time.split(':')[1]
    hour = t_time.split(':')[0]
    if meridiem == 'pm':
        hour = str(int(hour) + 12)
    return f'{hour}:{min}'


def get_weekday(day):
    days = [
        'monday',
        'tuesday',
        'wednesday',
        'thursday',
        'friday',
        'saturday',
        'sunday'
    ]
    return days[day]


def get_datetime_range(times):
    hour, minute = times.split(':')
    if hour == '24':
        hour, minute = '23', '59'
    return time(int(hour), int(minute))


def get_day_column(table, day):
    days = {
        'monday': table.monday,
        'tuesday': table.tuesday,
        'wednesday': table.wednesday,
        'thursday': table.thursday,
        'friday': table.friday,
        'saturday': table.saturday,
        'sunday': table.sunday
    }
    return days[day]
