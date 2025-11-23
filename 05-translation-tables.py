#!/usr/bin/env python3
# @Author: Farhad Yusifov
# @Email: farhadyusifov@protonmail.com
# @Date: 2025-11-21

# @Description: 

from Bio.Data import CodonTable


standard_table = CodonTable.unambiguous_dna_by_name["Standard"]
mito_table = CodonTable.unambiguous_dna_by_name["Vertebrate Mitochondrial"]
bac_table = CodonTable.unambiguous_dna_by_name["Bacterial"]

print(standard_table)
print(mito_table)
print(bac_table)
