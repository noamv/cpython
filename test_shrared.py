from threading import Thread
from time import sleep


def logic(l, x, y):
    my_list = []
    print('owner of mylist is ' + str(get_owner(my_list)))

    print('owner of list that shared from main:', get_owner(l))
    print('inserting to list that shared from main...')
    l.insert(0, 1)
    print('owner of list that shared from main:', get_owner(l))
    """
    for i in range(x, y):
        sleep(0.01)
        l.append(i)
    """


def main():
    my_list = []
    print('start')
    print('owner of list from main:', get_owner(my_list))
    th1 = Thread(target=logic, args=(my_list, 100, 200))
    th1.start()
    th2 = Thread(target=logic, args=(my_list, 100, 200))
    th2.start()    


if __name__ == '__main__':
    main()