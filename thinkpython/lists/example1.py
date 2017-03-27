def nested_sum(list):
    total=0
    for item in list:
        if type(item)==int:
            total=total+item
        else:
            list_total=list(item)
            total=total+list_total
    return total

