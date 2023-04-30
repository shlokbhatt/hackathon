dimensions = input("Enter the dimensions of your box in inches: ")

dimensions_list = dimensions.split()

scoops = 1

for dimension in dimensions_list:
    scoops *= int(dimension)

scoops = scoops // 25

cost = scoops / 4

print("This box holds {} full scoops of peanuts and costs ${}.".format(scoops, "%.2f" % cost))

