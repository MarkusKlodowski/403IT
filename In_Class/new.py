cites_temp_data = {'FR': [('Paris',26),('Lyon', 25),('Marseille', 27),('Nice', 28),]
                ,'PL': [('Warsaw', 293),('Wroclaw', 298),('Krakow', 300),('Lodz', 295),('gdanz', 301),]
                ,'IT': [('Rome', 27),('Milan', 26),('Venice', 26),('Florence', 25),]}

# 1. Converte the temperature to from Kelvin to Celsius
l1 = []

for i in cites_temp_data['PL']:
    cities = i[0], i[1] -273
    l1.append(cities)
print(l1)



# 2. Print all lists of cities with temperature below 25C from l1
l2 = []
for i in l1:
    if i[1] < 25:
        l2.append(i)
print(l2)

# 3. Print all lists of cities with temperature below 25C from cites_temp_data(updated)
cites_temp_data['PL'] = l1
l3 = []
for i in cites_temp_data:
    for j in cites_temp_data[i]:
        if j[1] < 25:
            l3.append(j)


def sqw(x):
    return x*x

l1 = [2,4]
l2 = list(map(sqw,l1))
print(l2)