self.second
        time2 = other.hour, other.minute, other.second
        return cmp(time1, time2)

    def cmp2(self, other):
        return cmp(self.time_to_int(), other.time_to_int())


def int_to_time(seconds):
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    time = Time(hour, minute, second)
    return time


t = Time(11, 54, 12)
t2 = Time(11, 54, 10)


print t.__cmp__(t2)
print t.cmp2(t2)
