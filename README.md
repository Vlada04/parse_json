Module created for parsing a JSON object (file). The module contain a function to provide access to various parts of the JSON object. The user is asked to enter the dictionary key whose meaning he wants to view.
The user sees the first keys from which he selects and receives the key value, if the value type is not a list and not a dictionary, if the value of the key is a dictionary then the user receives the next keys from which he selects.
If the value type is a list, the user is warned that the value of the key he entered is a list and the program displays all the elements of the list
if the first key entered by the user is absent in the json file the user receives the message "Key is not in file"
