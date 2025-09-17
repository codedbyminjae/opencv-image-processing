import numpy as np

# 수직으로 합치는 경우와 수평으로 합치는 경우
# hstack, vstack
a = np.arange(4).reshape(2, 2)
print(a)

b = np.arange(10, 14).reshape(2, 2)
print(b)

v = np.vstack((a, b))
print(v)
t = np.hstack((a, b))
print(t)

# concatenate = hstack
k = np.concatenate((a, b), 0)
print(k)
# concatenate = vstack
l = np.concatenate((a, b), 1)
print(l)

a = np.arange(12).reshape(4,3)
print(a)

b = np.arange(10,130,10).reshape(4,3)
print(b)

print('\n0번 축으로 a와 b를 병합\n')
m = np.stack((a,b),0)
print(m)

print('\n1번 축으로 a와 b를 병합\n')
n = np.stack((a,b),1)
print(n)

print('\n2번 축으로 a와 b를 병합\n')
z = np.stack((a,b),2)
print(z)
