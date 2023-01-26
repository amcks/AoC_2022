Generator Functions: Follow-up
=========

As a brief follow-up to the usage of generator functions for importing input files, which was explored in day 3, the solution shown in *day_5_1.py* highlights an additional versatility. Although the generator functions *yield*s single-line generator objects of the input file for every pass of the function, the application in the scripts here shows that the generator function can be called in an initial loop for the processing of an early chunk of the input data, following which, the loop can be broken, and once the generator function is called again via a different loop, it will resume the yielded output right after the last line called by the initial loop. Additionally, lines (or ranges of lines) can be purged/flushed using the *next* command, as in:

~~~python
next(input_gen)
~~~

Another variation to the use of generator functions can be seen in *day_5_2.py*. As evident, the implementation of a generator object does not necessitate the explicit definition of a standalone generator function; The generator object can be created in a single line, making use of list comprehension. Similar operations that were done in the previous implementation of generator functions can be seamlessly done in the generator expression version as well. The usage is as follows:

~~~python
input_gen = (line for line in open(r'./input_5'))
~~~
