#!/usr/bin/env python3
# @Author: Farhad Yusifov
# @Email: farhadyusifov@protonmail.com
# @Date: 2025-11-21

# @Description: parsing FASTA file containing sequences using Biopython.


from Bio import SeqIO


for record in SeqIO.parse("C:\\Users\\alnot\\Desktop\\NCBI _DATA\\ls_orchid.fasta", "fasta"):
    print("ID:", record.id)
    print("Sequence:", repr(record.seq))
    print("Sequence Length:", len(record.seq))
