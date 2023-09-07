def dict_reverse(**kwargs):
    dict_new = {}
    for key,value in kwargs.items():
        if isinstance (value, (list, dict, set, bytearray)):
           dict_new[str(value)] = key
        else:
            dict_new[value] = key
    return dict_new
    

print(dict_reverse(name='Alex', age=18, hobby=['fishing', 'soccer'],))
