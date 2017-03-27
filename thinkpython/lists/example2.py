def capitalize_all(t):
    res=[]
    for s in t:
        res.append(s.capitalize())
    return res
def capitalize_nested(list):
    final_list=[]
    for item in list:
        if type(item)==str:
            final_list.append(capitalize_all(item))
        else:
            final_list.append(capitalize-nested(item))
    return final_list
