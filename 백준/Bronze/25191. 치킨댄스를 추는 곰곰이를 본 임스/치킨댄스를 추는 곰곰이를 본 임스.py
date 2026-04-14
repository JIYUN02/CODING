chic = int(input())
co, be = map(int,input().split())

total = co//2 + be
print(min(total,chic))