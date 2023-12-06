import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import Ingredient from './Ingredient';

interface RecipeProps {
  RecipeName: string;
  ingredients: Array<{ name: string; amount: string; unit: string }>;
}

const Recipe: React.FC<RecipeProps> = ({ RecipeName, ingredients }) => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Recipe Title: {RecipeName}</Text>
      <Text style={styles.subtitle}>Ingredients:</Text>
      <View style={styles.ingredientsList}>
        {ingredients.map((ingredient, index) => (
          <View key={index} style={styles.listItem}>
            <Text style={styles.bullet}>•</Text>
            <Ingredient
              name={ingredient.name}
              amount={ingredient.amount}
              unit={ingredient.unit}
            />
          </View>
        ))}
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    margin: 16,
  },
  title: {
    fontSize: 18,
    fontWeight: 'bold',
  },
  subtitle: {
    fontSize: 16,
    fontWeight: 'bold',
    marginTop: 8,
  },
  ingredientsList: {
    marginLeft: 16,
    marginTop: 8,
  },
  listItem: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  bullet: {
    marginRight: 8,
    fontSize: 16,
  },
});

export default Recipe;
