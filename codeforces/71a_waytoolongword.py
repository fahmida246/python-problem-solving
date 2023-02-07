n = int(input())

for i in range(n):
    s1 = input()
    s2 = ''
    if len(s1) > 10:
        s2 = s1[0]
        s2 += str(len(s1)-2)
        s2 += s1[-1]
    else:
        s2 = s1
    print(s2)
