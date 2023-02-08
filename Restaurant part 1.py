#Nicholas Stevens
#CS 175L 02
#restaurant Part 1

input('Is anyone in your party a vegetarian?')
input('Is anyone in your party vegan?')
input('Is anyone in your party gluton free?')

if vegetarian == 'yes' and vegan == 'yes' and gluten_free == 'yes':
    print("Here are your restaurant choices:"
          "Corner Cafe"
          "The Chef's Kitchen")
if vegetarian == 'no' and vegan == 'no' and gluten_free == 'no':
    print("Here are your restaurant choices:"
          "Joe's Gourmet Burgers")
if vegetarian == 'yes' and vegan == 'no' and gluten_free == 'no':
    print("Here are your restaurant choices:"
          "Mamas Fine Italian")
if vegetarian == 'yes' and vegan == 'no' and gluten_free == 'yes':
    print("Here are your restaurant choices:"
          "Main Street Pizza Company")
