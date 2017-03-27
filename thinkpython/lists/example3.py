def cumulative_sum(list):
    sum_list=[]
    count=0
    for num in list:
        num= num+count
        sum_list.append(num)
        count=num
    return sum_list

