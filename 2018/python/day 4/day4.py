import re


with open('input.txt', 'r') as f:
  slurp = f.read()
  
logs = slurp.splitlines()

logs.sort()

guard_pattern = 'Guard #(\d+)'

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
