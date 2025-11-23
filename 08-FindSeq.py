#!/usr/bin/env python3
# @Author: Farhad Yusifov
# @Email: farhadyusifov@protonmail.com
# @Date: 2025-11-23

# @Description: How to find a subsequence in a given sequence.


from Bio.Seq import Seq, MutableSeq


seq = Seq("AGCTTAGCTA")
subseq = Seq("TAG")
index = seq.find(subseq)
print(f"Subsequence {subseq} found at index: {index}")

seq.index(subseq)
print(f"Subsequence {subseq} found at index using index(): {seq.index(subseq)}")
