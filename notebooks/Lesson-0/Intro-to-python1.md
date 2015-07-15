#A short Introduction to Python Part 1


##Notebooks
In front of you right now is a python notebook, it contains two different types of text. The first is plain text, which is what you are reading, it does not do anything besides be displayed. The second is code, the next cell is one containing python code, the code is run on the computer and can have many different effects such as doing math, creating images or displaying text. The code is run by something called an interpreter. The interpreter, translates code, that humans can read into machine language that the computer can understand.

[1]#This cell contains python code, it is printing the result of adding two numbers
[1]print(2 + 3)

That was a simple example of code, the first line was what is called a comment, in python comments are indicated with  the number sign #, they make the rest of line be ignore by the interpreter. The second line has two different functions, the first is `print()`, which takes the end result of what is within the brackets and displays it, the second is addition. Addition is a math operation that does exactly what you expect it adds numbers, it can also add other things but we will get into that later. Code cells have <font color=darkblue>In [1]:</font> next to them and their outputs written directly below.

Try changing the numbers or the symbol and rerunning the cell. The symbols for subtraction, multiplication and division are `-`, `*`, and `/` respectively. You can edit a cell by clinking it and run it by either pressing shift+enter or by pressing the run button at the top of the window. If you see an error (e.g. <font color=red>SyntaxError</font>) when you run, it means the interpreter could not understand what you wanted.


Now that you know how to do some math, lets look at words. A sequence of of character is called a string, strings are how computers deal with text as writing can be represented as a sequence of characters , spaces and punctuation. In python strings are created by surrounding the characters in using `'` or double `"` quotation marks, e.g. `"This is a string"`. You can print string just like you can print numbers.

[2]print("This is a string with double quotes")
[2]print('This is a string with single quotes')

As you can seePython automatically puts each newly printed string on a new line. Try playing with printing strings, see what happens if you add them together, or if you do not include a quotation mark.


##Types


Strings and numbers in Python are both what are called objects. In fact everything in Python is an object, `print()` is an object as is `'this object'`, but not all objects are the same they are categorized into different types. String (`str`) is a type of object, meaning they have different attributes than functions (`builtin_function_or_method`) like `print()`. Numbers are actually a few different types, the two you will encounter are integers (`int`) and floating point numbers (`float`). Ints are integers like those from math, they are not fractions and can be negative or positive. Floats are like the real numbers from math, they can be negative or positive and can be any value fraction or whole. Unfortunately floats are not perfectly precise and small rounding errors occur when they are used for math, so they can be tricky to use and generally ints are preferable.

The function `type()` will tell you the type of an object, here it is a on a few different ones.

[3]type('string' + "another string")
[4]type(2)
[5]type(print)

In the above code there are no `print()` statements, in fact if that was run in the notebook there would not be anything outputted. The notebook tells you that by putting <font color=red>Out[4]:</font> next to the output.


##Exceptions

Types also determine what functions work with which objects. In Python adding an int to a string does not make sense and creates an error called exceptions in python.

[6]1 + '1' #Notice the quotation marks

The above cell block produces a lot of text because the interpreter is telling you everything it know about the exception. Usually though the last line is the most important in this case it tells you exactly what went wrong: <font color=red> TypeError: unsupported operand type(s) for +: 'int' and 'str'</font> i.e. addition is not supported between integers (`int`) and strings (`str`). When ever people  writing code they make mistakes and exceptions are a way of handling them. They occur to prevent anything bad from happening and are a very useful for finding bugs.


##Variables


Instead of displaying the results of an operation immediately it can be stored in a variable. Variables are names given by the programmer to objects. This assignment is done with the single equals symbol `=`. Python has something called dynamic typing which means that you can assign objects to variables however you want.

[6]x = 2
[6]y = 'This is a variable'
[6]longVariableName = x + 2
[6]typeOfX = type(x)

Notice how there are no outputs from this cell, all the objects have been assigned variables there is nothing to display. Instead they are stored and we can print them later or use them for something else.

[7]print(typeOfX)
[7]print(longVariableName)
[7]xPlus10 = x + 10
[7]print(xPlus10)
