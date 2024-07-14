from datetime import datetime

def solution(date1, date2):
    return int(datetime(*date1) < datetime(*date2))
    