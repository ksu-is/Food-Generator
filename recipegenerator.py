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
if len(filtered_recipes) == 0:
    print('Sorry, no recipes found that match your preferences.')
    if len(filtered_recipes)==7:
        print('Here are your suggested seven recipes.')
else:
    print(f'Suggested recipes based on your preferences ({len(filtered_recipes)} found):')
    for index, row in filtered_recipes.iterrows():
        print(f'{row["meal"]} - {row["cuisine"]} cuisine')
