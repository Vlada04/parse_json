import json

def read_file(file_name):
    '''
    Read file
    >>> print(type(read_file()))
    <class 'dict'>
    '''
    with open(file_name, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data

def parsing_json_object(file_name):
    for key in read_file(file_name):
        print(key)
    first_key = input("Choose key:")

    if first_key in read_file(file_name):
        if type(read_file(file_name)[first_key]) != list and type(read_file(file_name)[first_key]) != dict:
            return read_file(file_name).get(first_key)

        if type(read_file(file_name)[first_key]) == list:
            print("It's a list:")
            for sets in read_file(file_name)[first_key]:
                print(sets)
                print(' ')
            choose_from_list = input("Choose element number(must be integer): ")

            print([key for key in read_file(file_name)[first_key][int(choose_from_list)-1]])
            second_choise = input('Choose key: ')
            return read_file(file_name)[first_key][int(choose_from_list)-1].get(second_choise)


    else:
        return "Key not in file"

print(parsing_json_object("kved.json"))