# Course Python on Kaggle

## Lesson 1
This course covers the key Python skills you’ll need so you can start using Python for data science.

We'll start with a brief overview of Python syntax, variable assignment, and arithmetic operators. If you have previous Python experience, you can skip straight to the hands-on exercise.

### Hello, Python
Python was named for the British comedy troupe Monty Python, so we'll make our first Python program a homage to their skit about Spam).

Just for fun, try reading over the code below and predicting what it's going to do when run. (If you have no idea, that's fine!)

Then click the "output" button to see the results of our program.

``# 1 in the lesson1.py exercise``

There's a lot to unpack here! This silly program demonstrates many important aspects of what Python code looks like and how it works. Let's review the code from top to bottom.

``# 2 in the lesson1.py exercise``

**Variable assignment:** Here we create a variable called spam_amount and assign it the value of 0 using =, which is called the assignment operator.

**Note:** If you've programmed in certain other languages (like Java or C++), you might be noticing some things Python doesn't require us to do here:

- we don't need to "declare" spam_amount before assigning to it
- we don't need to tell Python what type of value spam_amount is going to refer to. In fact, we can even go on to reassign spam_amount to refer to a different sort of thing like a string or a boolean.

``# 3 in the lesson1.py exercise``

**Function calls:** print is a Python function that displays the value passed to it on the screen. We call functions by putting parentheses after their name, and putting the inputs (or arguments) to the function in those parentheses.

``# 4 in the lesson1.py exercise``

The first line above is a **comment**. In Python, comments begin with the # symbol.

Next we see an example of reassignment. Reassigning the value of an existing variable looks just the same as creating a variable - it still uses the = assignment operator.

In this case, the value we're assigning to spam_amount involves some simple arithmetic on its previous value. When it encounters this line, Python evaluates the expression on the right-hand-side of the = (0 + 4 = 4), and then assigns that value to the variable on the left-hand-side.

``# 5 in the lesson1.py exercise``

We won't talk much about "conditionals" until later, but, even if you've never coded before, you can probably guess what this does. Python is prized for its readability and the simplicity.

Note how we indicated which code belongs to the if. "But I don't want ANY spam!" is only supposed to be printed if spam_amount is positive. But the later code (like print(viking_song)) should be executed no matter what. How do we (and Python) know that?

The colon (:) at the end of the if line indicates that a new **code block** is starting. Subsequent lines which are indented are part of that code block.

>**Note:** If you've coded before, you might know that some other languages use {curly braces} to mark the beginning and end of code blocks. Python's use of meaningful whitespace can be surprising to programmers who are accustomed to other languages, but in practice it can lead to more consistent and readable code than languages that do not enforce indentation of code blocks.

he later lines dealing with viking_song are not indented with an extra 4 spaces, so they're not a part of the if's code block. We'll see more examples of indented code blocks later when we define functions and using loops.

This code snippet is also our first sighting of a **string** in Python:

``"But I don't want ANY spam!"``

Strings can be marked either by double or single quotation marks. (But because this particular string contains a single-quote character, we might confuse Python by trying to surround it with single-quotes, unless we're careful.)

``# 6 in the lesson1.py exercise``

The * operator can be used to multiply two numbers (3 * 3 evaluates to 9), but we can also multiply a string by a number, to get a version that's been repeated that many times. Python offers a number of cheeky little time-saving tricks like this where operators like * and + have a different meaning depending on what kind of thing they're applied to. (The technical term for this is operator overloading.)

#### Numbers and arithmetic in Python

We've already seen an example of a variable containing a number above:

``# 7 in the lesson1.py exercise``

"Number" is a fine informal name for the kind of thing, but if we wanted to be more technical, we could ask Python how it would describe the type of thing that spam_amount is:

``# 8 in the lesson1.py exercise``

It's an int - short for integer. There's another sort of number we commonly encounter in Python:

``# 9 in the lesson1.py exercise``

A float is a number with a decimal place - very useful for representing things like weights or proportions.

type( ) is the second built-in function we've seen (after print( )), and it's another good one to remember. It's very useful to be able to ask Python "what kind of thing is this?".

A natural thing to want to do with numbers is perform arithmetic. We've seen the + operator for addition, and the * operator for multiplication. Python also has us covered for the rest of the basic buttons on your calculator:

| Operator | Name | Description |
|-------|------|------|
| a + b | Addiction | Sum of *a* and *b* |
| a - b | Subtraction | Difference of *a* and *b* |
| a * b | Multiplication | Product of *a* and *b* |
| a / b | True Division | Quotient of *a* and *b* |
| a // b | Floor Division | Quotient of *a* and *b*, removing fractional parts |
| a % b | Modulus | Integer remainder after division of *a* and *b* |
| a ** b | Exponentiation |  *a* raised to the power of *b* |
| -a | Negation | The negative of *a* |

One interesting observation here is that, whereas your calculator probably just has one button for division, Python can do two kinds. "True division" is basically what your calculator does:

``# 10 in the lesson1.py exercise``

It always gives us a float.

The // operator gives us a result that's rounded down to the next integer.

``# 11 in the lesson1.py exercise``

Can you think of where this would be useful? You'll see an example soon in the coding challenges.

##### Order of operations
The arithmetic we learned in primary school has conventions about the order in which operations are evaluated. Some remember these by a mnemonic such as **PEMDAS** - **P**arentheses, **E**xponents, **M**ultiplication/**D**ivision , **A**ddition/**S**ubtraction.

Python follows similar rules about which calculations to perform first. They're mostly pretty intuitive.

``# 12 in the lesson1.py exercise``

``# 13 in the lesson1.py exercise``

Sometimes the default order of operations isn't what we want:

``# 14 in the lesson1.py exercise``

Parentheses are useful here. You can add them to force Python to evaluate sub-expressions in whatever order you want.

``# 15 in the lesson1.py exercise``

##### Builtin functions for working with numbers

*min* and *max* return the minimum and maximum of their arguments, respectively...

``# 16 in the lesson1.py exercise``

*abs* returns the absolute value of an argument:

``# 17 in the lesson1.py exercise``

In addition to being the names of Python's two main numerical types, int and float can also be called as functions which convert their arguments to the corresponding type:

``# 18 in the lesson1.py exercise``


## Lesson 2

### Functions and Getting Help
Calling functions and defining our own, and using Python's builtin documentation

You've already seen and used functions such as *print* and *abs*. But Python has many more functions, and defining your own functions is a big part of python programming.

In this lesson, you will learn more about using and defining functions.

### Getting Help
You saw the *abs* function in the previous tutorial, but what if you've forgotten what it does?

The *help( )* function is possibly the most important Python function you can learn. If you can remember how to use *help( )*, you hold the key to understanding most other functions.

Here is an example:

``# 1 in the lesson2.py exercise``

*help( )* displays two things:

1. the header of that function *round*(*number*, *ndigits*=None). In this case, this tells us that *round( )* takes an argument we can describe as *number*. Additionally, we can optionally give a separate argument which could be described as *ndigits*.
2. A brief English description of what the function does.

**Common pitfall:** when you're looking up a function, remember to pass in the name of the function itself, and not the result of calling that function.

What happens if we invoke help on a call to the function round()? Unhide the output of the cell below to see.

``# 2 in the lesson2.py exercise``

Python evaluates an expression like this from the inside out. First it calculates the value of round(-2.01), then it provides help on the output of that expression.

(And it turns out to have a lot to say about integers! After we talk later about objects, methods, and attributes in Python, the help output above will make more sense.)

round is a very simple function with a short docstring. help shines even more when dealing with more complex, configurable functions like print. Don't worry if the following output looks inscrutable... for now, just see if you can pick anything new out from this help.

``# 3 in the lesson2.py exercise``

If you were looking for it, you might learn that print can take an argument called sep, and that this describes what we put between all the other arguments when we print them.

### Defining functions

Builtin functions are great, but we can only get so far with them before we need to start defining our own functions. Below is a simple example.

``# 4 in the lesson2.py exercise``

This creates a function called *least_difference*, which takes three arguments, *a*, *b*, and *c*.

Functions start with a header introduced by the *def* keyword. The indented block of code following the *:* is run when the function is called.

*return* is another keyword uniquely associated with functions. When Python encounters a *return* statement, it exits the function immediately, and passes the value on the right hand side to the calling context.

Is it clear what *least_difference( )* does from the source code? If we're not sure, we can always try it out on a few examples:

``# 5 in the lesson2.py exercise``

Or maybe the *help( )* function can tell us something about it.

``# 6 in the lesson2.py exercise``

Python isn't smart enough to read my code and turn it into a nice English description. However, when I write a function, I can provide a description in what's called the *docstring*.

#### Docstrings

``# 7 in the lesson2.py exercise``

The docstring is a triple-quoted string (which may span multiple lines) that comes immediately after the header of a function. When we call *help( )* on a function, it shows the docstring.

``# 8 in the lesson2.py exercise``

>**Aside:** The last two lines of the docstring are an example function call and result. (The >>> is a reference to the command prompt used in Python interactive shells.) Python doesn't run the example call - it's just there for the benefit of the reader. The convention of including 1 or more example calls in a function's docstring is far from universally observed, but it can be very effective at helping someone understand your function. For a real-world example, see this docstring for the numpy function *np.eye*.

Good programmers use docstrings unless they expect to throw away the code soon after it's used (which is rare). So, you should start writing docstrings, too!

### Functions that don't return
What would happen if we didn't include the *return* keyword in our function?

``# 9 in the lesson2.py exercise``

Python allows us to define such functions. The result of calling them is the special value None. (This is similar to the concept of "null" in other languages.)

Without a *return* statement, *least_difference* is completely pointless, but a function with side effects may do something useful without returning anything. We've already seen two examples of this: *print( )* and *help( )* don't return anything. We only call them for their side effects (putting some text on the screen). Other examples of useful side effects include writing to a file, or modifying an input.


``# 10 in the lesson2.py exercise``

### Default arguments

When we called *help(print)*, we saw that the print function has several optional arguments. For example, we can specify a value for *sep* to put some special string in between our printed arguments:

``# 11 in the lesson2.py exercise``

But if we don't specify a value, *sep* is treated as having a default value of ' ' (a single space).


``# 12 in the lesson2.py exercise``

Adding optional arguments with default values to the functions we define turns out to be pretty easy:

``# 13 in the lesson2.py exercise``

### Functions Applied to Functions

Here's something that's powerful, though it can feel very abstract at first. You can supply functions as arguments to other functions. Some example may make this clearer:

``# 14 in the lesson2.py exercise``

Functions that operate on other functions are called "higher-order functions." You probably won't write your own for a little while. But there are higher-order functions built into Python that you might find useful to call.

Here's an interesting example using the max function.

By default, *max* returns the largest of its arguments. But if we pass in a function using the optional *key* argument, it returns the argument *x* that maximizes *key(x)* (aka the 'argmax').

``# 15 in the lesson2.py exercise``


## Lesson 3
