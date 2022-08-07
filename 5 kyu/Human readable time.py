def make_readable(seconds):
    hours = seconds // 3600
    minutes = (seconds%3600) // 60
    second = (seconds%60) % 60
    return f'%02d:%02d:%02d' % (hours, minutes, second)


print(make_readable(0))
print(make_readable(86399))
print(make_readable(5))
