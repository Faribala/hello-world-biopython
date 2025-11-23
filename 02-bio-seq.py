#!/usr/bin/env python3
# @Author: Farhad Yusifov
# @Email: farhadyusifov@protonmail.com
# @Date: 2025-11-21

# @Description: A simple script to demonstrate the use of Biopython for basic sequence manipulation.


from Bio.Seq import Seq


myseq = Seq("AGTACACTGGT")
print("Sequence:", myseq)

myseq.reverse_complement()
print("Reverse Complement:", myseq.reverse_complement())

#changing to lowercase.
print(myseq.lower())

# converting Seq object to string. Print does this automatically.
print(str(myseq))

