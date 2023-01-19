Generator Functions: Follow-up
=========

As a brief follow-up to the usage of generator functions for importing input files, which was explored in day 3, the solution for day 5's puzzle highlights an additional versatility. Although the generator functions *yield*s single-line generator objects of the input file for every pass of the function, the application in the scripts here shows that the generator function can be called in an initial loop for the processing of an early chunk of the input data, following which, the loop can be broken, and once the generator function is called again via a different loop, it will resume the yielded output right after the last line called by the initial loop. Additionally, lines (or ranges of lines) can be purged/flushed using the *next* command, as in:

~~~python
next(input_gen)
~~~
