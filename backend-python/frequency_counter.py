words = ["api", "backend", "api", "python"]
dict = {}
for n in words:
    dict[n] = dict.get(n,0) +1
print(dict)