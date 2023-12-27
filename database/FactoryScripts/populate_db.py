
from ControllersAndModels.Factories import UserFactory, IngredientFactory, IngredientCategoryFactory, RecipeFactory, PantryItemFactory

def main():
    users = UserFactory.create_batch(20)
    ingredients = IngredientFactory.create_batch(20)
    ingredient_categories = IngredientCategoryFactory.create_batch(20)
    recipes = RecipeFactory.create_batch(20)
    pantry_items = PantryItemFactory.create_batch(20)

    # Linking them together
    for pantry_item in pantry_items:
        pantry_item.recipe_id = RecipeFactory().id
        pantry_item.save()

    for recipe in recipes:
        recipe.ingredients.extend(ingredients)
        recipe.save()

    for ingredient in ingredients:
        ingredient.category_id = IngredientCategoryFactory().id
        ingredient.save()

if __name__ == "__main__":
    main()
