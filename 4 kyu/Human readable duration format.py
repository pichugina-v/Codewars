# first solution

def format_duration(seconds):
    if seconds == 0:
        return "now"
    res = []
    y = seconds // 31536000
    d = seconds % 31536000 // 86400
    h = seconds % 86400 // 3600
    m = (seconds%3600) // 60
    s = (seconds % 60) % 60
    years = str(y) + ''.join([' years' if y > 1 else ' year' if 1 <= y > 0 else ''])
    if years != '0':
        res.append(years)
    days = str(d)  + ''.join([' days' if d > 1 else ' day' if 1 <= d > 0 else ''])
    if days != '0':
        res.append(days)
    hours = str(h) + ''.join([' hours' if h > 1 else ' hour' if 1 <= h > 0 else ''])
    if hours != '0':
        res.append(hours)
    minutes = str(m) + ''.join([' minutes' if m > 1 else ' minute' if 1 <= m > 0 else ''])
    if minutes != '0':
        res.append(minutes)
    secs = str(s) + ''.join([' seconds' if s > 1 else ' second' if 1 <= s > 0 else ''])
    if secs != '0':
        res.append(secs)
    l = len(res)
    if l == 1:
        return res[0]
    elif l > 1:
        return ', '.join([r for r in res[:-1]]) + ' and ' + ''.join(res[-1])

# refactored solution

sec = {
    "year": 60*60*24*365,
    "day": 60*60*24,
    "hour": 60*60,
    "minute": 60,
    "second": 1
}

def format_duration(seconds):
    if seconds == 0:
        return "now"
    res = []
    for name, divider in sec.items():
        temp = seconds // divider
        if temp > 1:
            res.append(str(temp) + f" {name}s")
        elif temp == 1:
            res.append(str(temp) + f" {name}")
        else: 
            continue
        seconds = seconds % divider
    l = len(res)
    if l == 1:
        return res[0]
    elif l > 1:
        return ', '.join([r for r in res[:-1]]) + ' and ' + ''.join(res[-1])
