from Chapter5.dictionary import D2

# D2["Name"] = input("Enter Name --")

# D2["Age"] = int(input("Enter Age --"))

# D2["Salary"] = float(input("Enter Salary --"))

# D2["Organisation"] = input("Enter Organisation --")

# D2["Is_married"] = bool(input("Are you married ?--"))

del D2['Is_married']

print(D2)

print('<=====================>')

for k in D2.keys():
    print(k)

print('<=====================>')

for i in D2.values():
    print(i)

print('<=====================>')

for j in D2.items():
    print(j)
