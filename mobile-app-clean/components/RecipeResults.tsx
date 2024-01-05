import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, ScrollView } from 'react-native';

import FilterDropdown from './FilterDropdown';
import RecipeResult from './RecipeResult';
import axios from 'axios';

interface Ingredient {
  name: string;
  amount: string;
  unit: string;
}

interface Recipe {
  recipeName: string;
  ingredients: Ingredient[];
  recipeDescription: string;
  
}


const styles = StyleSheet.create({
  container: {
    paddingTop: 40,
    paddingHorizontal: 16,
    backgroundColor: '#2455C2',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 16,
  },
  separator: {
    marginVertical: 20,
    height: 1,
    width: '100%',
    backgroundColor: '#ccc',
  },
});

const RecipeResults: React.FC = () => {
  const [selectedFilter, setSelectedFilter] = useState('All');
  const filterOptions = [
    { label: 'All', value: 'all' },
    { label: 'Favorites', value: 'favorites' },
    { label: 'New', value: 'new' },
    { label: 'Ready To Make', value: 'readytomake' },
  ];

  const handleFilterChange = (value: string) => {
    setSelectedFilter(value);
  };

  const [recipeData, setRecipeData] = useState<Recipe[]>([]);

  useEffect(() => {
    axios
      .get('http://127.0.0.1:5000')
      .then(response => {
        setRecipeData(response.data.recipe_array);
      })
      .catch(error => {
        console.error('Axios Error:', error);
        // Handle other error cases
      });
  }, []);

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.title}>
        <FilterDropdown
          options={filterOptions}
          selectedValue={selectedFilter}
          onValueChange={handleFilterChange}
        />
      </Text>
      <View style={styles.separator} />
      {recipeData.map((recipe, index) => (
        <View key={index}>
          <RecipeResult
            recipeName={recipe.recipeName}
            ingredients={recipe.ingredients}
            imagePath={require('../assets/images/nachos-example.jpeg')}
            recipeDescription={recipe.recipeDescription}
          />
          <View style={styles.separator} />
        </View>
      ))}
    </ScrollView>
  );
};

export default RecipeResults;
