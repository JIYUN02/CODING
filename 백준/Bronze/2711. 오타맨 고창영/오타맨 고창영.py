N = int(input())
for i in range(N):
    conn1, conn2 = map(str, input().split())
    print(conn2[:int(conn1)-1]+conn2[int(conn1):])