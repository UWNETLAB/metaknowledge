#A short Introduction to Python Part 2


##Functions


In the last lesson we looked at creating variables and saw how to create them from nothing

[1]x=1

or from other variables

[2]y=x
[3]print(x)
[3]print(y)

You can do the same with functions, but first we need to define what a functions is. A function is an object that contains some computation they do this computation on their inputs of which they can have any number including 0 and produce a single output. Mathematical functions are what Python's functions are based on and you can think of them like those, for example the function `min()` takes in any number of objects an returns the smallest, for numbers smallest is the smallest number for strings it is the first alphabetically. The inputs are all the objects inside the brackets and have commas between them.

[4]type(min)
[5]min(1,2,3,4)
[6]min('a','aa','b')

We can of course assign a variable to `min()` since `min()` is an object.

[5]OurMinVariable = min
[5]type(OurMinVariable)
[6]OurMinVariable(-1,-2,-3)

Some functions do not have any inputs and some do not have an output that is worth recording, for example `print()`. What do you think the output of print is?

[7]printsOutput = print("Printing")
[8]print(printsOutput)
[8]print(type(printsOutput))

`printsOutput` has the type `NoneType`. `NoneType` is Python's way of indicting that there is nothing there, if you create your own function and do not define what it outputs it will produce `None` as well. This raised a question though `print()` does output something, it prints things on the screen. Printing on a screen is what is called a side effect, the effect does not appear in the same place as the output. Mathematical functions do not have side effects they are something note even all programing languages have.

We also can define our own functions just like we can create our one variables. To do that first we write `def` then the name of our function then in brackets with commas between them the names of all our variables followed by colon

`def ourFunction(variableOne, variableTwo):`

below that we write them computation indented by some number of spaces or tabs

`    returnVariable = variableOne + variableTwo`

Finally if we want to return something we write `return` then a space then what we wish to return

`    return returnVariable`

Altogether this gives us

[9]def ourFunction(variableOne, variableTwo):
[9]    returnVariable = variableOne + variableTwo
[9]    return returnVariable
[9]ourFunction(10, 20)

We now have a function called ourFunction that adds the two objects it is given. Try changing what it does or adding a third input.
