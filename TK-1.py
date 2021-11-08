def get_list_from_console_input(elements_amount):
    result_list = []
    for element_index in range(elements_amount):
        result_list += [float(input('Enter ' + str(element_index+1) + ' value: '))]
    return result_list
