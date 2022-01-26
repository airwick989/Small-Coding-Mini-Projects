import pandas

#Everything between these lines was used to take the data from the crazy csv and make our own, simpler csv
################################################################################################################################################
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# grey = data[data["Primary Fur Color"] == "Gray"]
# grey = grey["Primary Fur Color"]
# grey = len(grey)

# red = data[data["Primary Fur Color"] == "Cinnamon"]
# red = red["Primary Fur Color"]
# red = len(red)

# black = data[data["Primary Fur Color"] == "Black"]
# black = black["Primary Fur Color"]
# black = len(black)

# data_dict = {
#     "Fur Colour" : ["Grey", "Red", "Black"],
#     "Count" : [grey, red, black]
# }

# data = pandas.DataFrame(data_dict)

# data.to_csv("squirrel_count.csv")
################################################################################################################################################

new_data = pandas.read_csv("squirrel_count.csv")

print(new_data)