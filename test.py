from pyDevHelper import decorators as dc


#@dc.FunctionEnchancers.logFunction
def add(x: float, y: float):
    return x + y


@dc.Validators.boolValidator
def retrn(x: bool):
    return x

print(add(2,3))

'''string = 'nome'


@dc.Validator.strValidator
def nome(var) -> str:
    return print(var)

nome(string)'''
