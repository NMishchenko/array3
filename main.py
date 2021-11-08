import importlib

from TK_2 import get_min_max_from_list
from TK_3 import get_list_divided_by_avg
from TK_4 import get_list_multiplied_by_avg

TK_1 = importlib.import_module('TK-1')
TK_5 = importlib.import_module('TK-5')

if __name__ == '__main__':
    print('Branch TK-1: ' + str(TK_1.get_list_from_console_input(10)))
    print('Branch TK-2: ' + str(get_min_max_from_list([1,2,3,4,5])))
    print('Branch TK-3: ' + str(get_list_divided_by_avg([1,2,3,4,5])))
    print('Branch TK-4: ' + str(get_list_multiplied_by_avg([1,2,3,4,5])))
    print('Branch TK-5: ' + str(TK_5.get_list_sqrt([4,9,16,25,36])))
