now = input()
bomb = input()

h1, m1, s1 = map(int, now.split(":"))
h2, m2, s2 = map(int, bomb.split(":"))

now_sec = h1 * 3600 + m1 * 60 + s1
bomb_sec = h2 * 3600 + m2 * 60 + s2

diff = bomb_sec - now_sec

if diff <= 0:
    diff += 24 * 3600

h = diff // 3600
m = (diff % 3600) // 60
s = diff % 60

print(f"{h:02d}:{m:02d}:{s:02d}")