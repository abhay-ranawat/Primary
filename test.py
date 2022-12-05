n, k, c = map(int, input().strip().split())
ary = list(map(int, input().strip().split()))

dctnry = {}
b = [[ary[i], i+1] for i in range(len(ary))]
b.sort()

dctnry = {}
typ = 0
dctnry[b[0][1]] = [b[0][0], typ]

for i in range(1, len(b)):
    if b[i][0] - b[i-1][0] > k:
        typ += 1

    dctnry[b[i][1]] = [b[i][0], typ]

prnt = ""

for _ in range(c):
    p, q = map(int, input().strip().split())
    if dctnry[p][1] == dctnry[q][1]:
        prnt += "Yes\n"
    else:
        prnt += "No\n"
print(prnt)

n, k, p = map(int, input().strip().split())
a = list(map(int, input().strip().split()))

dicti = {}
b = [[a[i], i+1] for i in range(len(a))]
b.sort()

dicti = {}
type = 0
dicti[b[0][1]] = [b[0][0], type]
for i in range(1, len(b)):
    if b[i][0] - b[i-1][0] > k:
        type += 1
    dicti[b[i][1]] = [b[i][0], type]
s = ""
for h in range(p):
    x, y = map(int, input().strip().split())
    if dicti[x][1] == dicti[y][1]:
        s += "Yes\n"
    else:
        s += "No\n"
print(s)