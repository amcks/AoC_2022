Multiple Solutions for Day 3
==============

Unlike the previous days, my solution(s) for day 3 consists of multiple files. Firstly, the first and second part of the puzzles are split into two files, named *day_3_1.py* and *day_3_2.py*, respectively.

Additionally, **Three** different solution files are available for the second part of day 3's puzzle. The reason behind this is that this puzzle was used as a tool to benchmark the performance of reading **small** text files in Python either directly, as in:

~~~python
with open(file_path, "r") as f:
    input = f.readlines()
~~~

compared to the same code in which the files were opened using a python generator function that actually yields the generator object in a line-by-line manner, as in:

~~~python
def gen_read(file_path):
    for line in open(file_path, "r"):
        yield line
~~~

Theoretically, reading the files using a generator function should be much more memory efficient, as only chunks of the generator object is extracted out of the function at a time, especially when compared to the use of the Python *.readlines()* method, which takes the entire input and stores it into, say, a list.

However, as it turns out, the sppedup is not significant for small files sizes, such as the one used in this day 3 puzzle (Text file with ~300 short lines). The more explicit *.readlines()* method was, in fact, either very slightly faster, or performs comparably to the generator function variants for this scale of input data.


In this directory, the variants are named as such:
* day_3_2_control.py --- Control case using the *.readlines()* method
* day_3_2_alt.py --- Solution that uses line-by-line generator function
* day_3_2.py --- Solution that uses the *.readlines()* contained **inside** a generator function
