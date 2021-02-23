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
    '''
    Parse json object using the entered key
    '''
    for key in read_file(file_name):
        print(key)
    choose_key = input("Choose key:")

    if choose_key in read_file(file_name):
        if type(read_file(file_name)[choose_key]) != list and\
            type(read_file(file_name)[choose_key]) != dict:
            return read_file(file_name).get(choose_key)
    
    res_lst = []
    if choose_key in read_file(file_name):
        if type(read_file(file_name)[choose_key]) == dict:
            while len(res_lst) < 1:
                choose_next_key = choose_key
                A = read_file(file_name)[choose_next_key]
                print([res for res in A])
                choose_next_key = input("Choose next key:")

                if type(A[choose_next_key]) == list:
                    print("It's a list")
                    for i in A[choose_next_key]:
                        print(i)
                    get_lst_elem = input('Choose list element index (must be integer): ')
                    if type(A[choose_next_key][int(get_lst_elem)-1]) == dict:
                        print([key for key in A[choose_next_key][int(get_lst_elem)-1]])
                        choose_from_list = input('Choose key: ')
                        res_lst.append(A[choose_next_key][int(get_lst_elem)-1][choose_from_list])
                    if type(A[choose_next_key][int(get_lst_elem)-1]) == list:
                        print("It's a list")
                        res_lst.append([elem for elem in A[choose_next_key][int(get_lst_elem)-1]])
                    else:
                        res_lst.append(A[choose_next_key][int(get_lst_elem)-1])
                        
                if type(A[choose_next_key]) != list and type(A[choose_next_key]) != dict:
                    res_lst.append(A[choose_next_key])
            return res_lst
    return "Key not in file"