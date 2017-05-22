#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

print('请输入分销商的数量：')
line = sys.stdin.readline().strip()
n = int(line)

print('请依次输入每个分销商中的产品数量：')
line = sys.stdin.readline().strip()
astr = line.split()
a = [0 for i in range(n)]
for i in range(n):
	a[i] = int(astr[i])

print('请依次输入每个分销商与生产总数的距离：')
line = sys.stdin.readline().strip()
sToDesStr = line.split()
# 每个分销商到目的地（生产总部）的距离
sToDes = [0 for i in range(n)]
for i in range(n):
	sToDes[i] = int(sToDesStr[i])

print('请输入运输成本与距离的比例系数x：')
line = sys.stdin.readline().strip()
x = int(line)

print('请输入货车大小造成的额外运输费与产品数量的比例系数y：')
line = sys.stdin.readline().strip()
y = int(line)

print('请输入%s个分销商之间的距离，按%s*%s的矩阵形式输入：' %(n, n, n))
# 分销商与分销商之间的距离
s = [[0 for i in range(n)] for j in range(n)]
count = 0
while True:
	line = sys.stdin.readline().strip()
	if line == '':
		break
	lines = line.split()
	for i in range(n):
		s[count][i] = int(lines[i])
	count += 1

# 分销商是否已经确定方案
judge = [0 for i in range(n)]

# 方案输出
res = ''

# 总费用
cost = 0

for k in range(n):
	f = 0
	to = -1
	tmp = 0
	for i in range(n):
		if judge[f] == 1:
			f += 1
		if judge[i] == 1:
			continue
		for j in range(n):
			if j == i or judge[j] == 1:
				continue
			mid = sToDes[i]*x + a[i]*y + sToDes[j]*x + a[j]*y - (s[i][j]*x + a[i]*y + (sToDes[j]*x + (a[i] + a[j])*y))
			if mid > tmp:
				tmp = mid
				f = i
				to = j
	if to == -1:
		if res == '':
			res += '每个分销商的商品分别独自运到生产总部。'
		else:
			res += '余下的分销商的商品分别独自运到生产总部。'
		for m in range(n):
			if judge[m] == 0:
				cost += sToDes[m]*x + a[m]*y
		break
	else:
		judge[f] = 1
		a[to] += a[f]
		res += '将 %s 的产品全部运送到 %s 分销商处；' %(f, to)
		cost += s[f][to]*x + a[f]*y

print('最优方案如下：')
print(res)
print('总费用为：%s' %(cost))


