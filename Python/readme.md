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
### Booleans and Conditionals

Using booleans for branching logic

#### Booleans

Python has a type of variable called *bool*. It has two possible values: *True* and *False*.

``# 1 in the lesson3.py exercise``

Rather than putting *True* or *False* directly in our code, we usually get boolean values from **boolean operators**. These are operators that answer yes/no questions. We'll go through some of these operators below.

#### Comparison Operations

| Operation | Description | Operation | Description |
|----| ---- | ---- | ---- |
| a == b | *a* equal to *b* | a != b | *a* not equal to *b* |
| a < b | *a* less then *b* | a > b | *a* greater then *b* |
| a <= b | *a* less then or equal to *b* | a >= b| *a*  greater then or equal to *b* |


``# 2 in the lesson3.py exercise``

Comparisons frequently work like you'd hope


``# 3 in the lesson3.py exercise``

But sometimes they can be tricky


``# 4 in the lesson3.py exercise``

Comparison operators can be combined with the arithmetic operators we've already seen to express a virtually limitless range of mathematical tests. For example, we can check if a number is odd by checking that the modulus with 2 returns 1:


``# 5 in the lesson3.py exercise``

Remember to use == instead of = when making comparisons. If you write n == 2 you are asking about the value of n. When you write n = 2 you are changing the value of n.

#### Combining Boolean Values

You can combine boolean values using the standard concepts of "and", "or", and "not". In fact, the words to do this are: *and*, *or*, and *not*.

With these, we can make our *can_run_for_president* function more accurate.


``# 6 in the lesson3.py exercise``

Quick, can you guess the value of this expression?


``# 7 in the lesson3.py exercise``

To answer this, you'd need to figure out the order of operations.

For example, and is evaluated before or. That's why the first expression above is *True*. If we evaluated it from left to right, we would have calculated *True* or *True* first (which is *True*), and then taken the and of that result with *False*, giving a final value of *False*.

You could try to memorize the order of precedence, but a safer bet is to just use liberal parentheses. Not only does this help prevent bugs, it makes your intentions clearer to anyone who reads your code.

For example, consider the following expression:

    prepared_for_weather = have_umbrella **or** rain_level < 5 **and** have_hood **or not** rain_level > 0 **and** is_workday

I'm trying to say that I'm safe from today's weather....

* if I have an umbrella...
* or if the rain isn't too heavy and I have a hood...
* otherwise, I'm still fine unless it's raining and it's a workday

But not only is my Python code hard to read, it has a bug. We can address both problems by adding some parentheses:

    prepared_for_weather = have_umbrella **or** (rain_level < 5 **and** have_hood) **or not** (rain_level > 0 **and** is_workday)

You can add even more parentheses if you think it helps readability:

    prepared_for_weather = have_umbrella **or** ((rain_level < 5) **and** have_hood) **or** (**not** (rain_level > 0 **and** is_workday))

We can also split it over multiple lines to emphasize the 3-part structure described above:


    prepared_for_weather = (
        have_umbrella
        or ((rain_level < 5) and have_hood)
        or (not (rain_level > 0 and is_workday))


#### Conditionals
Booleans are most useful when combined with conditional statements, using the keywords *if*, *elif*, and *else*.

Conditional statements, often referred to as if-then statements, let you control what pieces of code are run based on the value of some Boolean condition. Here's an example:


``# 8 in the lesson3.py exercise``

The *if* and *else* keywords are often used in other languages; its more unique keyword is *elif*, a contraction of "else if". In these conditional clauses, *elif* and *else* blocks are optional; additionally, you can include as many *elif* statements as you would like.

Note especially the use of colons (:) and whitespace to denote separate blocks of code. This is similar to what happens when we define a function - the function header ends with : , and the following line is indented with 4 spaces. All subsequent indented lines belong to the body of the function, until we encounter an unindented line, ending the function definition.


``# 9 in the lesson3.py exercise``

#### Boolean conversion

We've seen *int( )*, which turns things into ints, and *float( )*, which turns things into floats, so you might not be surprised to hear that Python has a *bool( )* function which turns things into bools.


``# 10 in the lesson3.py exercise``

We can use non-boolean objects in *if* conditions and other places where a boolean would be expected. Python will implicitly treat them as their corresponding boolean value:


``# 11 in the lesson3.py exercise``




## Lesson 4
### Lists

Lists and the things you can do with them. Includes indexing, slicing and mutating

#### Lists

Lists in Python represent ordered sequences of values. Here is an example of how to create them:

``# 1 in the lesson4.py exercise``

We can put other types of things in lists:

``# 2 in the lesson4.py exercise``

We can even make a list of lists:

``# 3 in the lesson4.py exercise``

A list can contain a mix of different types of variables:

``# 4 in the lesson4.py exercise``

#### Indexing

You can access individual list elements with square brackets.

Which planet is closest to the sun? Python uses zero-based indexing, so the first element has index 0.

``# 5 in the lesson4.py exercise``

What's the next closest planet?

``# 6 in the lesson4.py exercise``

Which planet is furthest from the sun?

Elements at the end of the list can be accessed with negative numbers, starting from -1:

``# 7 in the lesson4.py exercise``

``# 8 in the lesson4.py exercise``

#### Slicing
What are the first three planets? We can answer this question using slicing:

``# 9 in the lesson4.py exercise``

*planets[0:3]* is our way of asking for the elements of *planets* starting from index 0 and continuing up to but not including index 3.

The starting and ending indices are both optional. If I leave out the start index, it's assumed to be 0. So I could rewrite the expression above as:

``# 10 in the lesson4.py exercise``

If I leave out the end index, it's assumed to be the length of the list.

``# 11 in the lesson4.py exercise``

i.e. the expression above means "give me all the planets from index 3 onward".

We can also use negative indices when slicing:

``# 12 in the lesson4.py exercise``

``# 13 in the lesson4.py exercise``

#### Changing lists
Lists are "mutable", meaning they can be modified "in place".

One way to modify a list is to assign to an index or slice expression.

For example, let's say we want to rename Mars:

``# 14 in the lesson4.py exercise``

Hm, that's quite a mouthful. Let's compensate by shortening the names of the first 3 planets.

``# 15 in the lesson4.py exercise``

#### List functions
Python has several useful functions for working with lists.

*len* gives the length of a list:

``# 16 in the lesson4.py exercise``

*sorted* returns a sorted version of a list:

``# 17 in the lesson4.py exercise``

*sum* does what you might expect:

``# 18 in the lesson4.py exercise``

We've previously used the *min* and *max* to get the minimum or maximum of several arguments. But we can also pass in a single list argument.

``# 19 in the lesson4.py exercise``

#### Interlude: objects
I've used the term 'object' a lot so far - you may have even read that everything in Python is an object. What does that mean?

In short, objects carry some things around with them. You access that stuff using Python's dot syntax.

For example, numbers in Python carry around an associated variable called *imag* representing their imaginary part. (You'll probably never need to use this unless you're doing some very weird math.)

``# 20 in the lesson4.py exercise``

The things an object carries around can also include functions. A function attached to an object is called a **method**. (Non-function things attached to an object, such as *imag*, are called attributes).

For example, numbers have a method called *bit_length*. Again, we access it using dot syntax:

``# 21 in the lesson4.py exercise``

To actually call it, we add parentheses:

``# 22 in the lesson4.py exercise``

>**Aside**: You've actually been calling methods already if you've been doing the exercises. In the exercise notebooks *q1*, *q2*, *q3*, etc. are all objects which have methods called *check*, *hint*, and *solution*.

In the same way that we can pass functions to the *help* function (e.g. *help(max)*), we can also pass in methods:

``# 23 in the lesson4.py exercise``

The examples above were utterly obscure. None of the types of objects we've looked at so far (numbers, functions, booleans) have attributes or methods you're likely ever to use.

But it turns out that lists have several methods which you'll use all the time.

#### List methods
*list.append* modifies a list by adding an item to the end:

``# 24 in the lesson4.py exercise``

Why does the cell above have no output? Let's check the documentation by calling *help(planets.append)*.

>**Aside**: *append* is a method carried around by all objects of type list, not just *planets*, so we also could have called *help(list.append)*. However, if we try to call *help(append)*, Python will complain that no variable exists called "append". The "append" name only exists within lists - it doesn't exist as a standalone name like builtin functions such as *max* or *len*.

``# 25 in the lesson4.py exercise``

The -> *None* part is telling us that *list.append* doesn't return anything. But if we check the value of *planets*, we can see that the method call modified the value of *planets*:

``# 26 in the lesson4.py exercise``

*list.pop* removes and returns the last element of a list:

``# 27 in the lesson4.py exercise``

``# 28 in the lesson4.py exercise``

#### Searching lists
Where does Earth fall in the order of planets? We can get its index using the *list.index* method.

``# 29 in the lesson4.py exercise``

It comes third (i.e. at index 2 - 0 indexing!).

At what index does Pluto occur?

``# 30 in the lesson4.py exercise``

Oh, that's right...

To avoid unpleasant surprises like this, we can use the *in* operator to determine whether a list contains a particular value:

``# 31 in the lesson4.py exercise``

``# 32 in the lesson4.py exercise``

There are a few more interesting list methods we haven't covered. If you want to learn about all the methods and attributes attached to a particular object, we can call *help( )* on the object itself. For example, *help(planets)* will tell us about all the list methods:

``# 33 in the lesson4.py exercise``

Lists have lots of methods with weird-looking names like *__eq__* and *__iadd__*. Don't worry too much about these for now. (You'll probably never call such methods directly. But they get called behind the scenes when we use syntax like indexing or comparison operators.) The most interesting methods are toward the bottom of the list (*append*, *clear*, *copy*, etc.).


#### Tuples
Tuples are almost exactly the same as lists. They differ in just two ways.

**1:** The syntax for creating them uses parentheses instead of square brackets

``# 34 in the lesson4.py exercise``

``# 35 in the lesson4.py exercise``

**2:** They cannot be modified (they are _immutable_).

``# 36 in the lesson4.py exercise``

Tuples are often used for functions that have multiple return values.

For example, the *as_integer_ratio( )* method of float objects returns a numerator and a denominator in the form of a tuple:

``# 37 in the lesson4.py exercise``

These multiple return values can be individually assigned as follows:

``# 38 in the lesson4.py exercise``

Finally we have some insight into the classic Stupid Python Trick™ for swapping two variables!

``# 39 in the lesson4.py exercise``








## Lesson 5
### Loops and List Comprehensions

#### Loops

Python has a type of variable called *bool*. It has two possible values: *True* and *False*.

``# 1 in the lesson5.py exercise``

``# 5 in the lesson4.py exercise``

``# 6 in the lesson4.py exercise``

``# 7 in the lesson4.py exercise``

``# 8 in the lesson4.py exercise``

``# 9 in the lesson4.py exercise``

``# 10 in the lesson4.py exercise``

``# 11 in the lesson4.py exercise``

``# 12 in the lesson4.py exercise``

``# 13 in the lesson4.py exercise``

``# 14 in the lesson4.py exercise``

``# 15 in the lesson4.py exercise``

``# 16 in the lesson4.py exercise``

``# 17 in the lesson4.py exercise``

``# 18 in the lesson4.py exercise``

``# 19 in the lesson4.py exercise``

``# 20 in the lesson4.py exercise``

``# 21 in the lesson4.py exercise``

``# 22 in the lesson4.py exercise``

``# 23 in the lesson4.py exercise``

``# 24 in the lesson4.py exercise``

``# 25 in the lesson4.py exercise``

``# 26 in the lesson4.py exercise``

``# 27 in the lesson4.py exercise``

``# 28 in the lesson4.py exercise``

``# 29 in the lesson4.py exercise``

``# 30 in the lesson4.py exercise``

``# 31 in the lesson4.py exercise``

``# 32 in the lesson4.py exercise``

``# 33 in the lesson4.py exercise``

``# 34 in the lesson4.py exercise``

``# 35 in the lesson4.py exercise``

``# 36 in the lesson4.py exercise``

``# 37 in the lesson4.py exercise``

``# 38 in the lesson4.py exercise``

``# 39 in the lesson4.py exercise``



## Lesson 6
### Strings and Dictionaries

#### Strings

Python has a type of variable called *bool*. It has two possible values: *True* and *False*.

``# 1 in the lesson6.py exercise``

``# 5 in the lesson4.py exercise``

``# 6 in the lesson4.py exercise``

``# 7 in the lesson4.py exercise``

``# 8 in the lesson4.py exercise``

``# 9 in the lesson4.py exercise``

``# 10 in the lesson4.py exercise``

``# 11 in the lesson4.py exercise``

``# 12 in the lesson4.py exercise``

``# 13 in the lesson4.py exercise``

``# 14 in the lesson4.py exercise``

``# 15 in the lesson4.py exercise``

``# 16 in the lesson4.py exercise``

``# 17 in the lesson4.py exercise``

``# 18 in the lesson4.py exercise``

``# 19 in the lesson4.py exercise``

``# 20 in the lesson4.py exercise``

``# 21 in the lesson4.py exercise``

``# 22 in the lesson4.py exercise``

``# 23 in the lesson4.py exercise``

``# 24 in the lesson4.py exercise``

``# 25 in the lesson4.py exercise``

``# 26 in the lesson4.py exercise``

``# 27 in the lesson4.py exercise``

``# 28 in the lesson4.py exercise``

``# 29 in the lesson4.py exercise``

``# 30 in the lesson4.py exercise``

``# 31 in the lesson4.py exercise``

``# 32 in the lesson4.py exercise``

``# 33 in the lesson4.py exercise``

``# 34 in the lesson4.py exercise``

``# 35 in the lesson4.py exercise``

``# 36 in the lesson4.py exercise``

``# 37 in the lesson4.py exercise``

``# 38 in the lesson4.py exercise``

``# 39 in the lesson4.py exercise``


## Lesson 7
### Working with External Libraries

#### Booleans

Python has a type of variable called *bool*. It has two possible values: *True* and *False*.

``# 1 in the lesson7.py exercise``

``# 5 in the lesson4.py exercise``

``# 6 in the lesson4.py exercise``

``# 7 in the lesson4.py exercise``

``# 8 in the lesson4.py exercise``

``# 9 in the lesson4.py exercise``

``# 10 in the lesson4.py exercise``

``# 11 in the lesson4.py exercise``

``# 12 in the lesson4.py exercise``

``# 13 in the lesson4.py exercise``

``# 14 in the lesson4.py exercise``

``# 15 in the lesson4.py exercise``

``# 16 in the lesson4.py exercise``

``# 17 in the lesson4.py exercise``

``# 18 in the lesson4.py exercise``

``# 19 in the lesson4.py exercise``

``# 20 in the lesson4.py exercise``

``# 21 in the lesson4.py exercise``

``# 22 in the lesson4.py exercise``

``# 23 in the lesson4.py exercise``

``# 24 in the lesson4.py exercise``

``# 25 in the lesson4.py exercise``

``# 26 in the lesson4.py exercise``

``# 27 in the lesson4.py exercise``

``# 28 in the lesson4.py exercise``

``# 29 in the lesson4.py exercise``

``# 30 in the lesson4.py exercise``

``# 31 in the lesson4.py exercise``

``# 32 in the lesson4.py exercise``

``# 33 in the lesson4.py exercise``

``# 34 in the lesson4.py exercise``

``# 35 in the lesson4.py exercise``

``# 36 in the lesson4.py exercise``

``# 37 in the lesson4.py exercise``

``# 38 in the lesson4.py exercise``

``# 39 in the lesson4.py exercise``
