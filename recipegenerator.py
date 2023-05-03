import pandas as pd

# Load recipe data from CSV file
recipe_data = pd.read_csv('recipes.csv')

# Ask the user for their dietary preferences, ingredient restrictions, and preferred cuisine
time_of_day= input('Insert type of meal (e.g. breakfast, lunch, dinner, snack):')
dietary_preferences = input('What are your dietary preferences? (e.g. vegetarian, gluten-free): ')
ingredient_restrictions = input('Do you have any ingredient restrictions? (e.g. nuts, dairy): ')
preferred_cuisine = input('What is your preferred cuisine? (e.g. Italian, Chinese): ')


# Filter the recipe data based on the user's preferences
filtered_recipes = recipe_data[
    recipe_data['time_of_day'].str.contains(time_of_day, na=False) &
    recipe_data['dietary_preferences'].str.contains(dietary_preferences, na=False) &
    ~recipe_data['ingredients'].str.contains(ingredient_restrictions, na=False) &
    recipe_data['cuisine'].str.contains(preferred_cuisine, na=False)
]
# Display the suggested recipes to the user
if time_of_day == 'breakfast' and dietary_preferences =='Lactose intolerant' and ingredient_restrictions =='almond milk' and preferred_cuisine=='French':
    print('Your suggested meal based on your preferences is French Toast')
else:
    print('How about a croissant or crepe?')

if time_of_day == 'lunch' and dietary_preferences =='N/A' and ingredient_restrictions =='N/A' and preferred_cuisine=='Italian':
    print('Your suggested meal based on your preferences is Fettucine')
else:
    print('What about Gnocchi or Lasange? ')

if time_of_day == 'Dinner' and dietary_preferences =='N/A' or 'gluten-free' and ingredient_restrictions =='allergic to nuts' and preferred_cuisine=='Italian':
    print('Your suggested meal based on your preferences is Pizza ')
else:
    print('How about a Spaghetti Bolognese')
