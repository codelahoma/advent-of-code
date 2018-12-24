import re
from functools import reduce
from collections import Counter, namedtuple

with open('input.txt', 'r') as f:
    slurp = f.read()

logs = slurp.splitlines()

logs.sort()

guard_pattern = r'Guard #(\d+)'

logs_by_guard = {}

for log in logs:
    m = re.search(guard_pattern, log)
    if m is not None:
        guard = m.groups()[0]
        if guard not in logs_by_guard.keys():
            logs_by_guard[guard] = []
    else:
        logs_by_guard[guard].append(log)

sleepers = [(k, v) for (k, v) in logs_by_guard.items() if len(v) > 0]

sleep_pattern = r'(\d\d\d\d-\d\d-\d\d) \d\d:(\d\d)'

naps_by_guard = {}

for (guard, naps) in sleepers:
    naps_mins = naps_by_guard[guard] = {}

    for nap in naps:
        (d, t) = re.search(sleep_pattern, nap).groups()
        if d not in naps_mins.keys():
            naps_mins[d] = []

        naps_mins[d].append(t)

nap_mins_by_guard_by_date = {}

for (guard, naps_by_date) in naps_by_guard.items():
    nap_mins_by_guard_by_date[guard] = {}

    for (date, nap_log_mins) in naps_by_date.items():
        ranges = zip(nap_log_mins[::2], nap_log_mins[1::2])
        mins = nap_mins_by_guard_by_date[guard][date] = []
        for (s, w) in ranges:
            mins.extend(range(int(s), int(w)))


def count_summer(accum, list):
    return accum + len(list)


mins_by_guard = {
    guard: reduce(count_summer, mins.values(), 0)
    for guard, mins in nap_mins_by_guard_by_date.items()
}

max_mins = max(mins_by_guard.values())

max_sleepy_guard = [
    guard for guard, count in mins_by_guard.items() if count == max_mins
][0]

sleep_guard_mins = nap_mins_by_guard_by_date[max_sleepy_guard]

minutes_counter = Counter()

for minutes in sleep_guard_mins.values():
    minutes_counter.update(minutes)

sleepiest_minute = minutes_counter.most_common(1)[0][0]

answer1 = sleepiest_minute * int(max_sleepy_guard)

print(answer1)

sleepiest_minute_by_guard = {}

SleepMin = namedtuple('SleepMin', 'minute, frequency')
for (guard, mins_by_date) in nap_mins_by_guard_by_date.items():
    minutes_counter = Counter()
    for mins in mins_by_date.values():
        minutes_counter.update(mins)
    sleepiest_minute_by_guard[guard] = SleepMin(
        *minutes_counter.most_common(1)[0])

sleepiest_overall_minute_frequency = max(
    map(lambda s: s.frequency, sleepiest_minute_by_guard.values()))

sleepiest_minute_guard_key = [
    guard for guard, minute in sleepiest_minute_by_guard.items()
    if minute.frequency == sleepiest_overall_minute_frequency
][0]

answer2 = int(sleepiest_minute_guard_key) * sleepiest_minute_by_guard[sleepiest_minute_guard_key].minute
print(answer2)

