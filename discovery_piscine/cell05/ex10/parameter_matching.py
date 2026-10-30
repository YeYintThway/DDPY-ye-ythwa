#!/usr/bin/env python3
import sys

if len(sys.argv) == 2:
   word = input("what was the parameter?\n")
   if word == sys.argv[1]:
      print("Good Job!")
   else:
      print("Nope, sorry...")
else:
   print("none")