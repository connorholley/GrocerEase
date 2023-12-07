import React, { useState } from 'react';
import { View, Text, StyleSheet, ScrollView } from 'react-native';

import FilterDropdown from '../../components/FilterDropdown';
import RecipeResult from '../../components/RecipeResult';

const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingTop: 40,
    paddingHorizontal: 16,
    backgroundColor: '#f5f5f5',
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

const RecipeCardsView: React.FC = () => {
  const [selectedFilter, setSelectedFilter] = useState('All');
  const filterOptions = [
    { label: 'All', value: 'all' },
    { label: 'Favorites', value: 'favorites' },
    { label: 'New', value: 'new' },
    { label: 'Ready To Make', value: 'readytomake' },
  ];

  const handleFilterChange = (value: string) => {
    setSelectedFilter(value);
    // This will influence which SQL select we undergo
    // For example, favorites would randomly select a recipe marked as a favorite
    // add how many we are cooking for
  };

  const recipeData = [
    {
      recipeName: 'Cheesy Nachos',
      imagePath: require('../../assets/images/nachos-example.jpeg'),
      ingredients: [
        { name: 'cheese', amount: '100', unit: 'g' },
        { name: 'chips', amount: '500', unit: 'g' },
      ],
      recipeDescription:"Delicious chips covered in cheese. Baked to perfection."
    },
    {
      recipeName: 'Tasty Burger',
      imagePath: require('../../assets/images/burger.jpeg'),
      ingredients: [
        { name: 'cheese', amount: '100', unit: 'g' },
        { name: 'ground beef', amount: '1', unit: 'kg' },
      ],
      recipeDescription:"Damn that is a tasty Burger!"
    },
  ];

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
            imagePath={recipe.imagePath}
            recipeDescription={recipe.recipeDescription}
          />
          <View style={styles.separator} />
        </View>
      ))}
    </ScrollView>
  );
};

export default RecipeCardsView;
