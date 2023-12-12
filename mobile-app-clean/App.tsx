import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import RecipeResults from './components/RecipeResults';
import RecipeResult from './components/RecipeResult';
import RecipeCard from './components/RecipeCard';
const Stack = createStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="RecipeResults">
        <Stack.Screen name="RecipeResults" component={RecipeResults} />
        <Stack.Screen name="RecipeCard" component={RecipeCard} />
      </Stack.Navigator>
      <StatusBar style="auto" />
    </NavigationContainer>
    // <View><Text>Here I am</Text></View>
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
