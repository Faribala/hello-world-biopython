#!/usr/bin/env python3
# @Author: Farhad Yusifov
# @Email: farhadyusifov@protonmail.com
# @Date: 2025-11-21

# @Description: 


from Bio import SeqIO
from Bio.SeqUtils import gc_fraction


for record in SeqIO.parse("ls_orchid.fasta", "fasta"):
    print("ID:", record.id)
    print("Sequence:", repr(record.seq))
    print("Sequence Length:", len(record.seq))
    print("GC Content:", gc_fraction(record.seq)*100)
    print("Translated Sequence:", repr(record.seq.translate(to_stop=True)))
    # Please check to see the correct translation table to be implemented.