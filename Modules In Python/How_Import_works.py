"""
import pandas as pd
karoge to .pandas karne ki jaga sirn pd kare.
"""

# external module konsi file mai se kaha se aa raha hai kais pata kare:
import sys
print(sys.path)

# How to import content one file to another file:
import how_Import_works_2  # import file which u want to add
print(how_Import_works_2.a)  # . ke age import wale file ka nam de
how_Import_works_2.function_printing_Jock()  # printing function in importing file

# IMP: Kisi bhi file ka name modules ko match na kare asa nam mad do.