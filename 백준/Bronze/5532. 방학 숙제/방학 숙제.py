import math

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

sub_ko = math.ceil(A/C)
sub_math = math.ceil(B/D)
print(L-max(sub_ko, sub_math))