#!/usr/bin/env python3
# @Author: Farhad Yusifov
# @Email: farhadyusifov@protonmail.com
# @Date: 2025-11-23

# @Description: Working with sequence records using Biopython.


from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord


#help(SeqRecord)
simple_record = Seq("AGCTTAGCTA")
seq_record = SeqRecord(simple_record)
seq_record.id = "Seq1"
seq_record.description = "This is a simple DNA sequence."

print("Sequence ID:", seq_record.id)