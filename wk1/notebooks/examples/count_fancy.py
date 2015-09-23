str1 = "ThiS is String with Upper and lower case Letters"

res = {}
for char in str1.replace(" ", ""):
    char = char.lower()
    res[char] = res.get(char, 0) + 1

for k in sorted(res):
    print(k, res[k])

