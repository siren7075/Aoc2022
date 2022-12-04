def calculate(pair):
    p1, p2 = pair.split('-')
    return range(int(p1), int(p2)+1)

count1 = 0
count2 = 0

with open("/input.txt") as f: 
  for d in f:
   pair = d.strip()
   e1,e2 = pair.split(',')
   r1,r2 = set(calculate(e1)), set(calculate(e2))

# Part 1
   if r1.issubset(r2) or r2.issubset(r1):
    count1 += 1   
# Part 2
   if len(r1.intersection(r2)):
    count2 += 1
      
print(count1, count2)
