from goodclass import Time
import random

def rand_list_test(length, index):
    Time.add('Pre-list')
    rand_list = []
    for i in range(1,length):
        rand_list.append(random.random())
    Time.add('Post-list')
    delta = Time.delta('Pre-list', 'Post-list')
    Time.print_time(delta)

    for i in range(1,index):
        var = rand_list[random.randint(0,length)]

    Time.add('Post-index-list')
    delta = Time.delta('Post-list','Post-index-list')
    Time.print_time(delta)

# rand_list_test(40000000, 1000000)                  # Fer eftir lengh O(n) línulegt (að búa til listann) Hitt skiptir ekki máli (fer bara eftir því hversu oft það er gert)

def in_list_test(item, list_lenght):
    the_list = list(range(list_lenght))
    Time.add('Pre-in-list')
    if item in the_list:
        print('Init')
    else:
        print('Notinit')
    Time.add('Post-in-list')
    delta = Time.delta('Pre-in-list','Post-in-list')
    Time.print_time(delta)

# in_list_test(45000000/8,100000000)                # Fer eftir stærð item O(n) línulegt

def dict_checker(length):
    a_dict = {}
    for i in range(length):
        a_dict[random.random] = random.random()
    Time.add('Pre-Dict')
    for i in range(100000):
        if 21 in a_dict:
            print('init')
        
    Time.add('Post-Dict')
    delta = Time.delta('Pre-Dict', 'Post-Dict')
    Time.print_time(delta)

# dict_checker(100000000)                             # UUUUUU