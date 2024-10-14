from pyDevHelper import decorators as dc


@dc.Validators.strValidator
def add(x: float, y: float):
    return x + y


@dc.FunctionEnchancers.retryFunction
def example_function(x):
    if x < 5:
        raise ValueError("x is too small!")
    return x

print(example_function(3))

'''string = 'nome'


@dc.Validator.strValidator
def nome(var) -> str:
    return print(var)

nome(string)'''
