#Import json library
import json

#Create the data dictionary for program
data = {
    #Create key value pairs
    'name':'Daniella Echevestre', #Need comma between pairs
    'age':26,
    'city':'Tacoma',
    'interest':['skating','reading','videogames'],
    'is_student':True

}

#With statement for JSON file with open function with two arguements, w = write
with open('data.json','w') as json_file:
    
    #Three arguements to start dump: data, the open file, set the indentation for data structure
    json.dump(data,json_file,indent=4)
    
print('Data has been written to data.json')

#Read the data from the JSON file with statement, need to open then indicate to read file
with open('data.json','r') as json_file:

    #Control flow statement for loaded data object
    loaded_data = json.load(json_file)

#print function to display data on the terminal with loaded_data
print("Sucessfully able to read data.json")
print(loaded_data)

#loaded data with key to altenate the value (Modifying the JSON data)
loaded_data['age'] = 25
loaded_data['interest'].append('napping')

#need a with statement to write to the json file
with open('data.json','w') as json_file:
    
    #pass loaded_data into the arguement to override it along with other two arguments (line 18)
    json.dump(loaded_data, json_file, indent=4)

#To clarify to use that data has been added
print('Modified data written to data.json')