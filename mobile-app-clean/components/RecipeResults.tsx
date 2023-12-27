import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, ScrollView } from 'react-native';

import FilterDropdown from './FilterDropdown';
import RecipeResult from './RecipeResult';
import axios from 'axios';
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
    // This will influence which SQL select we undergo
    // For example, favorites would randomly select a recipe marked as a favorite
    // add how many we are cooking for
  };

  const recipeData = [
    {
      recipeName: 'Cheesy Nachos',
      imagePath: require('../assets/images/nachos-example.jpeg'),
      ingredients: [
        { name: 'cheese', amount: '100', unit: 'g' },
        { name: 'chips', amount: '500', unit: 'g' },
      ],
      recipeDescription:"Delicious chips covered in cheese. Baked to perfection."
    },
    {
      recipeName: 'Tasty Burger',
      imagePath: require('../assets/images/burger.jpeg'),
      ingredients: [
        { name: 'cheese', amount: '100', unit: 'g' },
        { name: 'ground beef', amount: '1', unit: 'kg' },
      ],
      recipeDescription:"Damn that is a tasty Burger!"
    },
  ];
  const [message, setMessage] = useState('');

  useEffect(() => {
    // Was having issues with axios localhost requests cause the emulator uses a diff localhost
    // prob a better way of doing this
    // https://stackoverflow.com/questions/42189301/axios-in-react-native-not-calling-server-in-localhost

    axios.get('http://127.0.0.1:5000')
      .then(response => {
        console.log('Response:', response);
        setMessage(response.data.message);
      })
      .catch(error => {
        console.error('Axios Error:', error);
  
        if (error.response) {
          console.error('Response Data:', error.response.data);
          console.error('Response Status:', error.response.status);
          console.error('Response Headers:', error.response.headers);
        } else if (error.request) {
          console.error('No Response Received:', error.request);
        } else {
          console.error('Request Setup Error:', error.message);
        }
      });
  }, []);
  
  

  return (
    
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.title}>
        {message}
        <FilterDropdown
          options={filterOptions}
          selectedValue={selectedFilter}
          onValueChange={handleFilterChange}
        />
      </Text>
      <View style={styles.separator} />
      {recipeData.map((recipe, index) => (
        <View key={index} >
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

export default RecipeResults;
