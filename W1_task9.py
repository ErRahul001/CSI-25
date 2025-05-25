n = int(input())
records = {}

for _ in range(n):
    name, *scores = input().split()
    records[name] = list(map(float, scores))

query_name = input()

avg = sum(records[query_name])/len(records[query_name])

print(f"{avg:.2f}")