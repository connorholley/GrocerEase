import React from 'react';
import { View, Text } from 'react-native';
import RNPickerSelect from 'react-native-picker-select';
import { StyleSheet } from 'react-native';

interface FilterDropdownProps {
  options: Array<{ label: string; value: string }>;
  selectedValue: string;
  onValueChange: (value: string) => void;
}

const FilterDropdown: React.FC<FilterDropdownProps> = ({
  options,
  selectedValue,
  onValueChange,
}) => {
  return (
    <View style={styles.container}>
      <Text style={styles.label}>Recipe Generator Filter:</Text>
      <RNPickerSelect
        items={options}
        onValueChange={onValueChange}
        style={pickerSelectStyles}
        value={selectedValue}
        useNativeAndroidPickerStyle={false}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flexDirection: 'row',
    alignItems: 'center',
    marginVertical: 0,
  },
  label: {
    marginRight: 10,
    fontSize: 16,
  },
});

const pickerSelectStyles = StyleSheet.create({
  inputIOS: {
    fontSize: 16,
    paddingVertical: 12,
    paddingHorizontal: 10,
    borderWidth: 1,
    borderColor: 'gray',
    borderRadius: 4,
    color: 'black',
    paddingRight: 30,
    backgroundColor: 'white',
    marginTop: 2, // Adjust this value to align the center points
  },
  inputAndroid: {
    fontSize: 16,
    paddingHorizontal: 10,
    paddingVertical: 8,
    borderWidth: 0.5,
    borderColor: 'purple',
    borderRadius: 8,
    color: 'black',
    paddingRight: 30,
    backgroundColor: 'white',
    marginTop: 2, // Adjust this value to align the center points
  },
});

export default FilterDropdown;
