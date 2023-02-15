#Nicholas Stevens
#CS 175L 02
#restaurant Part 2

vegetarian = input('Is anyone in your party a vegetarian?')
vegan = input('Is anyone in your party vegan?')
glutonFree = input('Is anyone in your party glutonFree?')

while vegetarian == "yes" and vegan == "yes" and glutonFree == "yes":
    print("Here are your restaurant choices:"
          "Corner Cafe"
          "The Chef's Kitchen")
if vegetarian == "no" and vegan == "no" and glutonFree == "no":
    print("Here are your restaurant choices:"
          "Joe's Gourmet Burgers")
if vegetarian == "yes" and vegan == "no" and glutonFree == "no":
    print("Here are your restaurant choices:"
          "Mamas Fine Italian")
if vegetarian == "yes" and vegan == "no" and glutonFree == "yes":
    print("Here are your restaurant choices:"
          "Main Street Pizza Company")
