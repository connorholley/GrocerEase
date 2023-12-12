
import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

interface MyPantryProps {}

const MyPantry: React.FC<MyPantryProps> = ({}) => {
  return (
    <View style={styles.container}>
      <Text>Welcome to MyPantry!</Text>
      {/* Add your components and logic here */}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  // Add additional styles as needed
});

export default MyPantry;
