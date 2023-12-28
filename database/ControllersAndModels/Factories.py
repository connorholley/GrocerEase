import factory
from factory import LazyAttribute
from Models import User, Recipe, PantryItem, IngredientCategory, Ingredient


class BaseFactory(factory.Factory):
    @classmethod
    def create_batch(cls, size, **kwargs):
        return [cls.create(**kwargs) for _ in range(size)]


class UserFactory(BaseFactory):
    class Meta:
        model = User

    name = factory.Faker('name')


class RecipeFactory(BaseFactory):
    class Meta:
        model = Recipe

    name = factory.Faker('name')
    instructions = factory.Faker('paragraph')
    description = factory.Faker('paragraph')


class IngredientFactory(BaseFactory):
    class Meta:
        model = Ingredient

    name = factory.Faker('word')

class PantryItemFactory(BaseFactory):
    class Meta:
        model = PantryItem
    ingredient_id= IngredientFactory.create().id
    amount = factory.Faker('random_int')
    unit = factory.Faker('random_element', elements=['gram', 'milliliter'])
    


class IngredientCategoryFactory(BaseFactory):
    class Meta:
        model = IngredientCategory

    name = factory.Faker('word')




