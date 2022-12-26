# Напишите программу, которая по списку дружественных пар
# для каждого человека определяет список «друзей 2-го уровня».
#
# Q: https://new.contest.yandex.ru/41238/problem?id=149944/2022_10_13/Z4TZboVPOx

n = input()
d = dict()

while n != '':
    x = n.split()
    if x[0] not in d.keys():
        d[x[0]] = {x[1]}
    else:
        d[x[0]].add(x[1])

    if x[1] not in d.keys():
        d[x[1]] = {x[0]}
    else:
        d[x[1]].add(x[0])

    n = input()

d_res = {i: set() for i in d.keys()}
for i in d.keys():
    for j in d[i]:
        temp = d[j].copy()
        temp.discard(i)
        temp.difference_update(d[i])
        d_res[i] = d_res[i].union(temp)


for i in sorted(d_res):
    print(f"{i}: {', '.join(sorted(d_res[i]))}")
