import React from 'react';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import RecipeResults from './components/RecipeResults';
import RecipeCard from './components/RecipeCard';
import MyPantry from './components/MyPantry'
import { MaterialIcons } from '@expo/vector-icons'; 
import { MaterialCommunityIcons } from '@expo/vector-icons';

const Stack = createStackNavigator();
const Tab = createBottomTabNavigator();

const HomeTabs = () => {
  return (
    <Tab.Navigator>
      <Tab.Screen name="Recipe Results" component={RecipeResults} options={{
            tabBarLabel: 'Recipe Results',
            tabBarIcon: ({ color, size }) => (
              <MaterialCommunityIcons name="chef-hat" size={size} color={color}  />
            ),
          }} />
      <Tab.Screen name="My Pantry" component={MyPantry} options={{
            tabBarLabel: 'My Pantry',
            tabBarIcon: ({ color, size }) => (
              <MaterialIcons name="kitchen" size={size} color={color} />
            ),
          }}/>
      {/* Add more tabs/screens as needed */}
    </Tab.Navigator>
  );
};

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="HomeTabs" screenOptions={{ headerShown: false }}>
        <Stack.Screen name="HomeTabs" component={HomeTabs} />
        <Stack.Screen name="RecipeCard" component={RecipeCard} />
      </Stack.Navigator>
      <StatusBar style="auto" />
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
