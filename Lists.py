friends=["Karen","Kevin","Jim","Toby","Toby","Oscar"]
lucky_numbers=[1,7,32,24,12,77]

print(friends)
print(friends[1])
print(friends[-1])
print(friends[1:4])
print(friends[3:])

friends.extend(lucky_numbers)
print(friends)
friends.append("Viorel")
print(friends)
friends.insert(3,"marian il bag in".upper())
print(friends)
friends.remove("Karen")
print(friends)
print(friends.index("Kevin"))
print(friends.count("Toby"))

lucky_numbers.reverse()
print(lucky_numbers)

lucky_numbers.sort()
print(lucky_numbers)

friends2=friends.copy()

friends.clear()
print(friends)
print(friends2)