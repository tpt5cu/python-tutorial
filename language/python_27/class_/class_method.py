# https://stackoverflow.com/questions/12179271/meaning-of-classmethod-and-staticmethod-for-beginner


class Orange(object):
    family = 'Rutaceae'
    genus = 'Citrus'

    def __init__(self, species):
        self._species = species
    
    def peel(self):
        print('Peeled the {} orange'.format(self._species))

    @classmethod
    def state_biological_classification(cls):
        print('The orange is in the family {} and the genus {}'.format(cls.family, cls.genus))


def examine_bound_methods():
    '''
    A class method is bound to a class object, even when the class method is accessed through a __dict__. This must be because the decorator modifies
    the function when the function is first created
    '''
    o = Orange('Mandarin')
    # <bound method type.state_biological_classification of <class '__main__.Orange'>>
    print(o.state_biological_classification) 
    # <class '__main__.Orange'>
    print(o.state_biological_classification.__self__) 
    # <bound method type.state_biological_classification of <class '__main__.Orange'>>
    print(Orange.state_biological_classification) 
    # <classmethod object at ...>
    print(Orange.__dict__['state_biological_classification'])
    # <bound method Orange.peel of <__main__.Orange object at ...>>
    print(o.peel) 
    # <__main__.Orange object at ...>
    print(o.peel.__self__) 


if __name__ == '__main__':
    examine_bound_methods()