import functools


'''
While keeping state on functions seems like a confusing and evil idea, I can think of at least one real-world usage: spys! Stateful decorators are
nothing special, they just take advantage of the fact that:
- Python functions have had a __dict__ attribute since 2.1 (who knew)

An iteration on this concept is using a class as a decorator
'''


def track_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print('{} has been called {} times'.format(func.__name__, wrapper.call_count))
        return func(*args, **kwargs)
    wrapper.call_count = 0
    print(type(wrapper.__dict__)) # <type 'dict'>
    return wrapper


@track_calls
def spend_cash():
    print('I\'m spending that $$$')


if __name__ == '__main__':
    spend_cash()
    spend_cash()
    spend_cash()