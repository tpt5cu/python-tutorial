# https://stackoverflow.com/questions/3798835/understanding-get-and-set-and-python-descriptors


class HandWaveMethod(object):
    '''This is a non-data descriptor'''

    # TODO: can I implement a method using a non-data descriptor

    #def __get__(self, instance, owner):
    #    return self

    def __call__(self, to):
        return 'The wind waves to {}'.format(to)



class Flag(object):

    hand_wave = HandWaveMethod()

    def __init__(self, country):
        self._country = country

    def wind_wave(self):
        '''
        Recall that methods are shorthand syntax for non-data descriptors
        - Methods get their first implicit argument (e.g. self or cls) from their __get__ method
        '''
        return 'The {} flag waves in the wind'.format(self._country)


    


def wave_flag():
    f = Flag('USA')
    print(f.wind_wave()) # The USA flag waves in the wind
    print(f.hand_wave('teachers'))


if __name__ == '__main__':
    wave_flag()