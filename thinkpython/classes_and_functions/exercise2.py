class Time(object):

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

time2 = Time()
time2.hour = 11
time2.minute = 59
time2.second = 35

def is_after(t1, t2):
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)
