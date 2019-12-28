# Python-Fuzzer

### Author
Emanuel Aracena Beriguete

### Description
A Python-based fuzzer that generates input to test for potential faults.
The program takes an input file, feeds the process input based on options selected, then returns a log into the directory showing all the
cases where the program produced an error or crashed.

### Usage
```
python3 fuzzer.py EXECUTABLE NUMBER_OF_TESTS
```

To run with an executable "a.out", type:
```
python3 fuzzer.py a.out 10
```

Results are printed to terminal as well as saved in a text file with a timestamp.
