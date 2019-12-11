from contextlib import contextmanager


'''
Even if I return from within a with-statement, the __exit__() code still executes. The return value could be modified by the __exit__() code if I
wanted, presumably because of @contextmanager
'''

@contextmanager
def my_context_manager(my_list):
    print("Entered context")
    my_list.append("item")
    yield my_list
    my_list.append('another thing')
    print("Exited context")


def use_context_manager():
    my_list = [56]
    with my_context_manager(my_list) as l:
        print(l) # [56, 'item']
        return l
        # This does not execute, but the __exit__() code does
        #print(l)


if __name__ == "__main__":
    a_list = use_context_manager()
    print('val was: ' + str(a_list))