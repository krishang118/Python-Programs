import json
a = {"A1":"a",\
     "A2":"b",\
     "A3":"c",}

print(a)
print(a["A2"])


for key in a:
    print(key,":",a[key])

print(a.keys())
print(a.values())
print(list(a.keys()))
print(tuple(a.values()))
print(str(a.keys()))

a["A2"] = "B"

print(a)
print("A1" in a)
print("A4" in a)
print("a" in a.values())
print("d" in a.values())

print(json.dumps(a,indent = 2))
