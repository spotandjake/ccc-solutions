#include<stdio.h>

int main() {
  int filterLevel = 1000000000; // 10^9
  int testNumbers[filterLevel];
  int i = 0;
  for (int i = 0; i < filterLevel; i++) {
    testNumbers[i] = 0;
  }
  for (int i = 0; i < filterLevel; i++) {
    i += testNumbers[i];
  }
  printf("%i", i);
};