import re
Empty = 0
Occupancy = 0
Used = 0
s = "448x640 2 Empty seat statuss, 2 Occupancy statuss, 3 Used seat statuss, "
match1 = re.search(r'\d+(?= Empty)', s)
match2 = re.search(r'\d+(?= Occupancy)', s)
match3 = re.search(r'\d+(?= Used)', s)

if(re.search(r'\d+(?= Empty)', s) != None):
    Empty = int(match1.group())
if(re.search(r'\d+(?= Occupancy)', s) != None):
    Occupancy = int(match2.group())
if(re.search(r'\d+(?= Used)', s) != None):
    Used = int(match3.group())
print(Empty, Occupancy, Used)