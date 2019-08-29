from threading import Thread
from time import sleep


def logic(l, x, y):
    my_list = []
    print('owner of mylist is ' + str(get_owner(my_list)))
    """
    for i in range(x, y):
        sleep(0.01)
        l.append(i)
    """


def main():
    my_list = []
    print('start')
    import pdb; pdb.set_trace()
    th1 = Thread(target=logic, args=(my_list, 100, 200))
    th1.start()
    th2 = Thread(target=logic, args=(my_list, 100, 200))
    th2.start()    


if __name__ == '__main__':
    main()