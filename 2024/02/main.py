import re;

filename = 'input.txt'

def parse_line(line):
    nums = re.findall(r'\d+', line)
    return list(map(int, nums))

def get_direction(levelA, levelB):
    if (levelA > levelB):
      return -1
    else:
      if (levelA < levelB):
        return 1
      else:
        return 0

def compare_levels(levelA, levelB):
    diff = abs(levelA - levelB)
    direction = get_direction(levelA, levelB)
    
    return diff, direction

def get_report_direction(report):
    direction = 0
    ix = 0
    while (direction == 0 and ix < len(report)):
        _, direction = compare_levels(report[ix], report[ix + 1])
        ix += 1
    return direction    

MAX_SAFE = 3
MIN_SAFE = 1

def some_variant_is_safe(report):
  for ix in range(0, len(report)):   
      copy_report = report.copy() 
      copy_report.pop(ix)
      if is_safe(copy_report):
          print("safe variant", report, " -> ", copy_report)
          return True  
  return False;

def is_safe(report, with_dampener = False):
    direction = None

    for ix in range(0, len(report) - 1):
        diff, level_direction = compare_levels(report[ix], report[ix + 1])
        if (direction == None) and (level_direction != 0):
            direction = level_direction
        if (level_direction == 0) or (level_direction != direction) or (diff > MAX_SAFE) or (diff < MIN_SAFE):
            if (with_dampener):
              return some_variant_is_safe(report)
            else:
              return False
    return True

with open(filename, 'r') as f:
    reports = []
    safe_reports = 0
    safe_reports_with_dampener = 0

    for line in f:
        report = parse_line(line.strip())
        safe_reports += 1 if is_safe(report) else 0
        # print("report", report, "is safe", is_safe(report))
        safe_reports_with_dampener += 1 if is_safe(report, True) else 0
        reports.append(report)

    print('Part 1:', safe_reports)
    print('Part 2:', safe_reports_with_dampener)