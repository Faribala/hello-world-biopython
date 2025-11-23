#!/usr/bin/env python3
# @Author: Farhad Yusifov
# @Email: farhadyusifov@protonmail.com
# @Date: 2025-11-21

# @Description: This is an example of a null sequence.


from Bio.Seq import Seq


myseq = Seq(None, length=8)
print("Sequence Length:", len(myseq))
