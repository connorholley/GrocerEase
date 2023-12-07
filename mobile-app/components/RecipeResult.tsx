import React from 'react';
import { View, Text, StyleSheet, Image, ImageSourcePropType } from 'react-native';
import Ingredient from './Ingredient';

interface RecipeProps {
  recipeName: string;
  recipeDescription:string;
  ingredients: Array<{ name: string; amount: string; unit: string }>;
  imagePath: ImageSourcePropType; // Change the type to ImageSourcePropType
}

const RecipeResult: React.FC<RecipeProps> = ({ recipeName, ingredients, imagePath, recipeDescription }) => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>{recipeName}</Text>
      <Image
        style={styles.image}
        source={imagePath}
      />
      <Text style={styles.subtitle}>Description:</Text>
      <Text style={styles.description}>{recipeDescription}</Text>
      <Text style={styles.subtitle}>Ingredients not in pantry:</Text>
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
    alignSelf: 'center',
    borderRadius:20,
    
  },
  container: {
    margin: 16,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    paddingBottom:25,
    alignSelf: 'center',
  },
  subtitle: {
    fontSize: 16,
    fontWeight: 'bold',
    marginTop: 25,
  },
  description:{
    marginLeft: 16,
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

export default RecipeResult;
