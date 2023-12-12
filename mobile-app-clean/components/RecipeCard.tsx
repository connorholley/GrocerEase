import React from 'react';
import { View, Text, Image, StyleSheet, TouchableOpacity } from 'react-native';
import Ingredient from './Ingredient';
import { useNavigation } from '@react-navigation/native';
import { AntDesign } from '@expo/vector-icons';
const RecipeCard = ({ route }) => {
  const { recipeName, ingredients, imagePath, recipeDescription } = route.params;
  const navigation = useNavigation();

  const handleGoBack = () => {
    // Pass each parameter separately

    navigation.goBack();
    // navigation.navigate('RecipeCard',{});
  };
  return (
    <View style={styles.outerContainer}>
  
  <View style={styles.container}>
  <TouchableOpacity onPress={handleGoBack} style={styles.goBackClick} >
  <AntDesign name="back" size={24} color="white" />
      </TouchableOpacity>
     <Text style={styles.title}> {recipeName}</Text>
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
  outerContainer:{
   
  
      paddingTop: 40,
      paddingHorizontal: 16,
      backgroundColor: '#2455C2',
      height:'100%'
    
  },
  container: {
   
    backgroundColor: '#9ECE1A',
    padding: 25,
    height:'90%',
    borderRadius: 25,
    
  
  
    
  
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
  goBackClick: {
    position: 'absolute',
    top: 10,
    left: 20,
    borderRadius:20,
    backgroundColor:'#2455C2',
    padding:4
  },
  
});

export default RecipeCard;
