import time
import datetime as dt
import dataclasses as datac

@datac.dataclass
class FunctionEnchancers:
    def timeDelta(func):
        '''This method returns the amount of time it took to execute the function.'''
        def wrapper(*a, **k):
            t0 = time.time()
            fx = func(*a, **k)
            t = time.time()
            dt = t - t0
            print(dt)
            return fx
        return wrapper

    def deprecFunction(func):
        def wrapper(*a, **k):
            print('This method / function is depreciated.')
            choice = str(input('The results may be inacurate. Do you want to contiue? (Y/N) ')).upper()
            if choice == 'Y':
                fx = func(*a, **k)
                return fx
            else: return None
        return wrapper

    def underDevFunction(func):
        def wrapper(*a, **k):
            print('This method / function is under development.')
            choice = str(input('The results may be inacurate. Do you want to contiue? (Y/N) ')).upper()
            if choice == 'Y':
                fx = func(*a, **k)
                return fx
            else: return None
        return wrapper

    #to be fixed
    def retryFunction(func):
        def wrapper(*a, **k):
            for c in range(0, 5):
                try:
                    fx = func(*a, **k)
                    return fx
                except Exception as e:
                    print(f'{c + 1}: An error has occurred. Please try again later.')
                    last_exception = e
            return last_exception
        return wrapper
        
    def logFunction(func):
        log = []
        def wrapper(*a, **k):
            moment = dt.datetime.now()
            log.append(moment)
            fx = func(*a, **k)
            for args in a:
                log.append(args)
            for kwargs in k:
                log.append(kwargs)
            return f'Executed at: {log[0]}. Arguments: {log[1:]}. Return: {fx}.'
        return wrapper
    
    def cacheFunciton(func):
        cache = {}
        def wrapper(*a):
            if a in cache:
                return cache[a]
            fx = func(*a)
            cache[a] = fx
            return fx
        return wrapper

@datac.dataclass
class Validators:

    def strValidator(func):
        def wrapper(*a: str, **k: str):
            validation_pos = all(isinstance(arg, str) for arg in a)
            validation_named = all(isinstance(kwarg, str) for kwarg in k)
            if validation_pos and validation_named:
                print('Parameters Type OK.')
                time.sleep(2)
                fx = func(*a, **k)
                return fx
            else:
                return 'Wrong Type of parameters. They should be strings.'
        return wrapper
    
    def intValidator(func):
        def wrapper(*a: int, **k: int):
            validation_pos = all(arg.is_integer() for arg in a)
            validation_named = all(kwarg.is_integer() for kwarg in k)
            if validation_pos and validation_named:
                print('Parameters are Ok.')
                time.sleep(2)
                fx = func(*a, **k)
                return fx
            else:
                return 'Wrong Type of parameters. They should be ints.'
        return wrapper
    
    def floatValidator(func):
        def isfloat(value: str) -> bool:
            if isinstance(value, bool):
                return False
            try:
                float_value = float(value)
                return float_value != int(float_value)
            except ValueError:
                return False
        def wrapper(*a: float, **k: float):
            validation_pos = all(isfloat(arg) for arg in a)
            validation_named = all(isfloat(kwarg) for kwarg in k)
            if validation_pos and validation_named:
                print('Parameters are Ok.')
                time.sleep(2)
                fx = func(*a, **k)
                return fx
            else:
                return 'Wrong Type of parameters. They should be floats.'
        return wrapper
    
    def boolValidator(func):
        def isBool(value: bool) -> bool:
            try:
                bool(value)
                return True
            except ValueError:
                return False         
        def wrapper(*a: bool, **k: bool):
            validation_pos = all(isBool(arg) for arg in a)
            validation_named = all(isBool(kwarg) for kwarg in k)
            if validation_pos and validation_named:
                print('Parameters are Ok.')
                time.sleep(2)
                fx = func(*a, **k)
                return fx
            else:
                return 'Wrong Type of parameters. They should be bools.'
        return wrapper