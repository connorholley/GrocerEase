import React, { useState } from 'react';
import { View, Text, StyleSheet } from 'react-native';
import EditableList from './EditableList';

interface MyPantryProps {}
interface Ingredient {
    id: string;
    name: string;
    amount: string;
    unit: string;
  }
const MyPantry: React.FC<MyPantryProps> = ({}) => {
    const [listData, setListData] = useState<Ingredient[]>([
        { id: '1', name: 'Item 1', amount: '', unit: '' },
       
        // Add more initial items as needed
      ]);
    
      const handleItemChange = (id: string, field: string, text: string) => {
        const updatedList = listData.map((item) =>
          item.id === id ? { ...item, [field]: text } : item
        );
        setListData(updatedList);
      };
    
      const handleItemRemove = (id: string) => {
        const updatedList = listData.filter((item) => item.id !== id);
        setListData(updatedList);
      };
    
      const handleItemAdd = () => {
        // Check if all fields (name, amount, and unit) are non-empty
        const isAnyFieldEmpty = listData.some(item => item.name === '' || item.amount === '' || item.unit === '');
      
        if (!isAnyFieldEmpty) {
          const newItem: Ingredient = { id: `${listData.length + 1}`, name: '', amount: '', unit: '' };
          setListData([...listData, newItem]);
        } else {
          // Optionally, you can provide user feedback or handle the case when an empty ingredient is not allowed
          console.warn('Please fill in all fields before adding a new ingredient.');
        }
      };
      
  return (
    <View style={styles.outerContainer}>
  
    <View style={styles.container}>

  
        <Text style={styles.title}>My Pantry</Text>
      
      
        
        <Text style={styles.subtitle}>My Ingredients:</Text>
        
        <View style={styles.ingredientsList}>
        <EditableList
        data={listData}
        onItemChange={handleItemChange}
        onItemRemove={handleItemRemove}
        onItemAdd={handleItemAdd}
      />
            
         
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
        alignSelf: 'center',
        textDecorationLine: 'underline',
        textDecorationColor:'#2455C2'
      }
   ,
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

export default MyPantry;
