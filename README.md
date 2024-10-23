# pyDevHelper - Python Utility Decorators

This repository contains two main modules of Python decorators, `FunctionEnchancers` and `Validators`. These modules provide utility and validation functions that can enhance or verify the behavior of other functions.

## Table of Contents

- [Function Enchancers](#function-enchancers)
  - [timeDelta](#timedelta)
  - [deprecFunction](#deprecfunction)
  - [underDevFunction](#underdevfunction)
  - [retryFunction](#retryfunction)
  - [logFunction](#logfunction)
  - [cacheFunction](#cachefunction)
- [Validators](#validators)
  - [strValidator](#strvalidator)
  - [intValidator](#intvalidator)
  - [floatValidator](#floatvalidator)
  - [boolValidator](#boolvalidator)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Function Enchancers

This module contains decorators that enhance the functionality of a function by adding extra features like execution time measurement, automatic retries, caching, and more.

### timeDelta

```python
@FunctionEnchancers.timeDelta
def my_function():
    # Your code here
This decorator measures the time taken for the function to execute and prints the duration in seconds.
```
### deprecFunction
```python
@FunctionEnchancers.deprecFunction
def my_function():
    # Your code here
This decorator warns that the function is deprecated and prompts the user to decide whether to continue, indicating that the results may be inaccurate.
```
### underDevFunction
```python
@FunctionEnchancers.underDevFunction
def my_function():
    # Your code here
Similar to deprecFunction, this decorator informs the user that the function is under development and asks whether they wish to proceed.
```
### retryFunction
```python
@FunctionEnchancers.retryFunction
def my_function():
    # Your code here
This decorator attempts to execute the function up to 5 times in case an exception is raised. If all attempts fail, the last exception is returned.
```
### logFunction
```python
@FunctionEnchancers.logFunction
def my_function():
    # Your code here
This decorator logs the date and time of the function execution, along with the arguments passed, and returns a log containing these details.
```
### cacheFunction
```python
@FunctionEnchancers.cacheFunction
def my_function():
    # Your code here
This decorator implements caching for the function results. If the function is called again with the same parameters, the cached value is returned instead of recalculating the result.
```
## Validators
This module contains validator decorators that check if the parameters of a function meet specific type requirements, such as str, int, float, or bool.

### strValidator
```python
@Validators.strValidator
def my_function(*args, **kwargs):
    # Your code here
This decorator ensures that all parameters are strings. If not, it returns an error message.
```
### intValidator
```python
@Validators.intValidator
def my_function(*args, **kwargs):
    # Your code here
This decorator validates that all parameters are integers.
```
### floatValidator
```python
@Validators.floatValidator
def my_function(*args, **kwargs):
    # Your code here
This decorator checks if the parameters are floats. Booleans and integers are treated as invalid.
```
### boolValidator
```python
@Validators.boolValidator
def my_function(*args, **kwargs):
    # Your code here
This decorator verifies that all parameters are booleans (True or False).
```

## Installation
To use these decorators in your Python project, follow these steps:

Clone this repository:
```bash
git clone https://github.com/your-username/pyDevHelper.git
```
Import the FunctionEnchancers and Validators modules into your project:
```python
from pyDevHelper import FunctionEnchancers, Validators
```

Usage
Apply the decorators to the functions you want to enhance or validate.
Check the example section to understand how to use each decorator.
Example Usage:
```python
from pyDevHelper import FunctionEnchancers, Validators

@FunctionEnchancers.timeDelta
def my_function(x):
    return x * 2

print(my_function(10))
```
Contributing
Contributions are welcome! If you have any ideas or fixes, feel free to open a pull request or issue.

License
This project is licensed under the MIT License.
