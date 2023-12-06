import React, { useState } from 'react';
import { View, Text, StyleSheet, ScrollView } from 'react-native';
import Recipe from '../../components/Recipe';
import FilterDropdown from '../../components/FilterDropdown';

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

const RecipeCardView: React.FC = () => {
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
  };

  const recipeData = {
    // We will get this data from the backend
    RecipeName: 'Cheesy Nachos',
    ingredients: [
      { name: 'cheese', amount: '100', unit: 'g' },
      { name: 'chips', amount: '500', unit: 'g' },
    ],
  };

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.title}>Recipe Generator</Text>
      <FilterDropdown
        options={filterOptions}
        selectedValue={selectedFilter}
        onValueChange={handleFilterChange}
      />
      <View style={styles.separator} />
      <Recipe RecipeName={recipeData.RecipeName} ingredients={recipeData.ingredients} />
      <View style={styles.separator} />
    </ScrollView>
  );
};

export default RecipeCardView;
