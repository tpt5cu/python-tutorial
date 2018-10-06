# https://stackoverflow.com/questions/291978/short-description-of-the-scoping-rules#

global_var= "I'm a global variable"


class CoolClass:

    m_attribute = "I'm a mutable class attribute."

    def __init__(self, x=0, f_num=0, string="empty"):
        self.x = x
        self.f_num = f_num
        self.string = string

    def method1(self):
        obj = CoolClass()
        print(vars(obj))

    def loop_scope(self):
        """Python loops (and control structure, etc.) do not create a new scope. Functions DO create a scope. A loop
        inside of a function is in the same scope as the surrounding function.
        """
        self.x = 5
        """x as a local variable does NOT exist yet. It's just a coincidence that the instance object also has
        an attribute called 'x'
        """
        # print("x is: " + str(id(x)))
        x = 100
        print("outr x is: " + str(id(x)) + ", " + str(x))
        for x in range(x, 110):
            print("loop x is: " + str(id(x)) + ", " + str(x))
            # Each time x is assigned in the loop, it becomes an entirely new object.
            x = -2
        # 'x' at this point is the last x = -2 assignment in the for loop.
        print("outr x is: " + str(id(x)) + ", " + str(x))


    def method3(self):
        local_var = 3


def create_instance_in_class():
    my_obj = CoolClass()
    my_obj.method1()


def view_loop():
    obj = CoolClass()
    obj.loop_scope()


if __name__ == "__main__":
    # create_instance_in_class()
    view_loop()
