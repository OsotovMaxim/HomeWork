
# coding: utf-8

# In[ ]:

import os

def start(path):
    list_buffer = []
    while True:
        print('Введите строку:')
        find_files_name = input()
        if len(list_buffer) == 0:
            list_buffer = os.listdir(path)
        list_buffer = [el for el in list_buffer if find_files_name.lower() in el.lower()]
        for el in list_buffer:
            print('{}\n'.format(el))
        print('Total: {}'.format(len(list_buffer)))

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath('__file__'))

if __name__ == '__main__':
    path_name = os.path.join(current_dir, migrations)
    start(path_name)
    # ваша логика
    pass

