def execute(s: str) -> int:
    ns = sorted(
        sum(int(line) for line in part.splitlines())
        for part in s.split('\n\n')
    )
        # part 1 
        # return max(ns[-3:])
        # part 2
    return sum(ns[-3:])
    
with open('/input.txt') as f:
  print(execute(f.read()))
