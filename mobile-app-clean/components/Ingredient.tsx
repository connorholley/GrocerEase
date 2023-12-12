import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

const styles = StyleSheet.create({
  ingredientList: {
    alignItems: 'center',
  },
});

type IngredientProps = {
  name: string;
  amount: string;
  unit: string;
};

const Ingredient: React.FC<IngredientProps> = (props) => {
  return (
    <View style={styles.ingredientList}>
      <Text>{props.name}: {props.amount + props.unit}</Text>
    </View>
  );
};

export default Ingredient;