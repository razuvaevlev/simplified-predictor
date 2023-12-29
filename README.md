#  Simplified Java variable predictor

![Static Badge](https://img.shields.io/badge/Python-3.9-blue) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-green.svg)](https://www.gnu.org/licenses/gpl-3.0)
> _Python script to predict possible variable values in Simplified Java code_
## Simplified Java
Simplified Java file always contains only the definition of a single class, **Main**, which contains the definition of a single 
method, "**method**". The first line of the method always contains the declaration of the **integer variable x**, the last line 
displays the value to the console. The rest of the body consists of if statements and assignments to the variable x of 
integer values.<br />

Example:
```java
public class Main {
    public static void method(boolean... conditions) {
        int x;
        x = 1;
        if (conditions[0]) {
            x = 2;
            if (conditions[1]) {
                x = 3;
            }
            x = 4;
            if (conditions[2]) {
                x = 5;
            }
        }
        if (conditions[3]) {
            x = 6;
        }
        System.out.println(x);
    }
}
```
## Installation
```sh
git clone https://github.com/razuvaevlev/simplified-predictor.git
cd simplified-predictor
```
## Usage
```
usage: predict.py [-h] file

Simplified Java variables predictor

positional arguments:
  file        Source Java file

optional arguments:
  -h, --help  show this help message and exit
```
## Example
```
$ python3 predict.py Test.Java
6 5 4 1
```