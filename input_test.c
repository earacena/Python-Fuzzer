// Name of file: input_test.c
// Data created: August 23, 2019
// Description:  Simple C program that takes input and displays input given.
//               Written as test for pfuzz.py by Emanuel Aracena

#include<stdio.h>

void read_input_and_print() {
  char name[10];

  printf("What is your name?: ");
  scanf("%s", name);
  printf("Your name is %s.\n", name);
}

int main() {

  read_input_and_print();
  
  return 0;
}
