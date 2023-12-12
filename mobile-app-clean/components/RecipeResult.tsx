import React from 'react';
import { View, Text, StyleSheet, Image, ImageSourcePropType, TouchableOpacity  } from 'react-native';
import Ingredient from './Ingredient';
import { MaterialIcons } from '@expo/vector-icons';
import { useNavigation } from '@react-navigation/native';
interface RecipeProps {
  recipeName: string;
  recipeDescription: string;
  ingredients: Array<{ name: string; amount: string; unit: string }>;
  imagePath: ImageSourcePropType; 
}

const RecipeResult: React.FC<RecipeProps> = ({ recipeName, ingredients, imagePath, recipeDescription }) => {
  const navigation = useNavigation();

  const handleRecipeClick = () => {
    // Pass each parameter separately
    console.log('Navigating to RecipeCard with data:', {
      recipeName,
      ingredients,
      imagePath,
      recipeDescription,
    });
    navigation.navigate('RecipeCard', {
      recipeName,
      ingredients,
      imagePath,
      recipeDescription,
    });
    // navigation.navigate('RecipeCard',{});
  };
  
  
  return (
    <View style={styles.container}>
      {/* Add TouchableOpacity for the arrow button */}
      <TouchableOpacity onPress={handleRecipeClick} style={styles.recipeClick}>
      <MaterialIcons name="integration-instructions" size={24} color="white" />
      </TouchableOpacity>

      <Text style={styles.title}>{recipeName}</Text>
      <Image style={styles.image} source={imagePath} />
      <Text style={styles.subtitle}>Description:</Text>
      <Text style={styles.description}>{recipeDescription}</Text>
      <Text style={styles.subtitle}>Ingredients not in pantry:</Text>
      <View style={styles.ingredientsList}>
        {ingredients.map((ingredient, index) => (
          <View key={index} style={styles.listItem}>
            <Text style={styles.bullet}>•</Text>
            <Ingredient name={ingredient.name} amount={ingredient.amount} unit={ingredient.unit} />
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
    borderRadius: 20,
  },
  container: {
    margin: 16,
    backgroundColor: '#9ECE1A',
    borderRadius: 25,
    padding: 25,
    position: 'relative', // Position relative to allow absolute positioning of arrow button
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    paddingBottom: 25,
    alignSelf: 'center',
  },
  subtitle: {
    fontSize: 16,
    fontWeight: 'bold',
    marginTop: 25,
  },
  description: {
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
  // Styles for the arrow button
  recipeClick: {
    position: 'absolute',
    top: 20,
    right: 20,
    borderRadius:20,
    backgroundColor:'#2455C2',
    padding:4
  },
});

export default RecipeResult;