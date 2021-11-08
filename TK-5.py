def get_list_sqrt(received_list):
    result_list = []
    for element in received_list:
        new_element = element ** 0.5
        result_list.append(new_element)
    return result_list
