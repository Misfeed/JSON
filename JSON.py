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

#Writing a JSON file/ With statement with open function with two arguements, w = write
with open('data.json','w') as json_file:
    
    #Three arguements: data, the open file, set the indentation for data structure
    json.dump(data,json_file,indent=4)
    
print('Data has been written to data.json')