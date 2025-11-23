#!/usr/bin/env python3
# @Author: Farhad Yusifov
# @Email: farhadyusifov@protonmail.com
# @Date: 2025-11-23

# @Description: 


from Bio.Seq import Seq, MutableSeq


my_seq = Seq("ACGTACGT")
my_mutableseq = MutableSeq("ACGTACGT")

print("Original Seq:", my_seq)
print("Original MutableSeq:", my_mutableseq)

# Modifying MutableSeq
my_mutableseq[0] = "T"
print("Modified MutableSeq:", my_mutableseq)
