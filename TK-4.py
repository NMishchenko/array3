def get_list_multiplied_by_avg(received_list):
    result_list = []
    list_avg = sum(received_list)/len(received_list)
    for element in received_list:
        new_element = element*list_avg
        result_list.append(new_element)
    return result_list
