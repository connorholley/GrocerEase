import React from 'react';
import { View, Text, StyleSheet, Image, ImageSourcePropType } from 'react-native';
import Ingredient from './Ingredient';

interface RecipeProps {
  recipeName: string;
  ingredients: Array<{ name: string; amount: string; unit: string }>;
  imagePath: ImageSourcePropType; // Change the type to ImageSourcePropType
}

const Recipe: React.FC<RecipeProps> = ({ recipeName, ingredients, imagePath }) => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Recipe of the day: {recipeName}</Text>
      <Image
        style={styles.image}
        source={imagePath}
      />
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
  image: {
    width: 200,
    height: 200,
    resizeMode: 'cover', 
  },
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
