from datetime import datetime

def in_time_decorator_func(firstTime, secondTime):
    def out_decorator_func(func):
        def decorate_func(*args, **kargs):
            maxTime = firstTime
            minTime = secondTime
            if firstTime < secondTime:
                maxTime = secondTime
                minTime = firstTime
            now = datetime.now()
            if now > minTime and now < maxTime:
                print('in time!')
            func()
        return decorate_func
    return out_decorator_func

@in_time_decorator_func(firstTime=datetime(2018,8,29, 0), secondTime=datetime(2018,9,29,23))
def foo():
    print('foo')

if __name__=='__main__':
    foo()