import React, { useState } from 'react';
import { View, FlatList, TextInput, TouchableOpacity, Text, StyleSheet } from 'react-native';
import { Icon } from 'react-native-elements';

interface Ingredient {
  id: string;
  name: string;
  amount: string;
  unit: string;
}

interface EditableListProps {
  data: Ingredient[];
  onItemChange: (id: string, field: string, text: string) => void;
  onItemRemove: (id: string) => void;
  onItemAdd: () => void;
}

const EditableList: React.FC<EditableListProps> = ({ data, onItemChange, onItemRemove, onItemAdd }) => {
    
  const renderItem = ({ item }: { item: Ingredient }) => (
    <View style={styles.listItem}>
      <TextInput
        style={styles.input}
        value={item.name}
        placeholder="Ingredient Name"
        onChangeText={(text) => onItemChange(item.id, 'name', text)}
      />
      <TextInput
        style={styles.input}
        value={item.amount}
        placeholder="Amount"
        onChangeText={(text) => onItemChange(item.id, 'amount', text)}
      />
        <TextInput
        style={styles.input}
        value={item.unit}
        placeholder="Unit"
        onChangeText={(text) => onItemChange(item.id, 'unit', text.toLowerCase())}
        />

      <TouchableOpacity onPress={() => onItemRemove(item.id)}>
        <Icon name="delete" type="material" color="red" />
      </TouchableOpacity>
    </View>
  );

  return (
    <View>
      <FlatList
        data={data}
        renderItem={renderItem}
        keyExtractor={(item) => item.id}
      />
      <TouchableOpacity style={styles.addButton} onPress={onItemAdd}>
        <Text style={styles.addText}>Add Item</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  listItem: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    margin: 5,
  },
  input: {
    flex: 1,
    borderWidth: 1,
    borderRadius: 5,
    padding: 5,
    marginRight: 10,
  },
  addText:{
    color:'white',
  },
  addButton: {
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#2455C2',
  
    padding: 10,
    marginTop: 10,
    borderRadius: 5,
  },
});

export default EditableList;
