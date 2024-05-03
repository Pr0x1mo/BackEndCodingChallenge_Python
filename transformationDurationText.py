def solution (seconds):
    if seconds == 0:
        return "now"
    
    minute = 60
    hour = minute * 60
    day = hour * 24
    year = day * 365

    years = seconds // year
    seconds %= year
    days = seconds // day
    seconds %= day
    hours = seconds //hour
    seconds %= hour
    minutes = seconds //minute
    seconds %= minute

    result = []
    if years > 0:
        result.append(f"{years} year{'s' if years > 1 else ''}")
    if days > 0:
        result.append(f"{days} day{'s' if days > 1 else ''}")
    if hours > 0:
        result.append(f"{hours} hour{'s' if hours > 1 else ''}")
    if minutes > 0:
        result.append(f"{minutes} minute{'s' if minutes > 1 else ''}")
    if seconds > 0:
        result.append(f"{seconds} second{'s' if seconds > 1 else ''}")

    if len(result)>1:
        return ', '.join(result[:-1]) + ' and ' + result[-1]
    elif result:
        return result[0]
    else:
        return "now"

seconds = int(input())

out_ = solution(seconds)
print (out_)