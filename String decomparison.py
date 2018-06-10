import re
import numpy as np
from scipy.spatial.distance import cosinefrom scipy import optimize
from matplotlib import pylab as plt
import math
from numpy.linalg import solve

sentences = []
words = []
with open('text.txt') as f:
    for i in f:
        sentences.append(re.split('[^a-z]', (i.lower()).strip()))
print sentences
for i in sentences:
    for j in range(i.count('')):
        i.remove('')
for i in sentences:
    for j in i:
        if j not in  words:
            words.append(j)
table = np.zeros((22, 254))
for i in range(22):
    for j in range(254):
        table[i, j] = sentences[i].count(words[j])
res = {}
for i in range(21):
    res[1 + i] = cosine(table[0], table[1 + i])
ans = sorted(res, key = lambda x : res[x])
string = str(ans[0]) + ' ' + str(ans[1])
with open('submission-1.txt', 'w') as f:
    f.write(string)

with open('result.txt') as f:
    print f.readline()

def f(x):
    x = float(x)
    return math.sin(x / 5) * math.exp(x / 10) + 5 * math.exp(-x / 2)
x = np.zeros([4, 4])
points = [1, 4, 10, 15]
for i in range(4):
    for j in range(4):
        x[i,j] = points[i] ** j
b = []
for i in points:
    b.append(f(i))
a = solve(x, b)
def g(x):
    return a[0] + a[1] * x + a[2] * (x ** 2) + a[3] * (x ** 3)
string = str(a[0]) + ' ' + str(a[1]) + ' ' + str(a[2]) + ' ' + str(a[3])
print f(1), f(1.)