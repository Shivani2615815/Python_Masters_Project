# Run pip install import-ipynb
# Use: python test_part2.py
#Alternatively use: pytest

#importing modules
import import_ipynb
import pytest
from part2 import common_seq, no_seq
from Bio import SeqIO

#this function checks if common_seq function from part2 module performs the operation correctly by comparing expected output with actual output.
def test_common_seq():
    output_file = "test_part2_output.txt"
    top_n = 3
    #the expected output is computed manually
    expect = {'GGGACTTTCC': 1, 'GGGAATTTCC': 1, 'GGGAAATTCC': 1} 
    output = common_seq("test_part2_output.txt")

    assert output == expect
    
test_common_seq()

#this function checks if no_seq function from part2 module performs the operation correctly by comparing expected output with actual output.
def test_no_seq():
    input_file = "test_part2_input.fasta"
    output_file = "test_part2_output.txt"
    expect = 1
    output = no_seq("test_part2_input.fasta","test_part2_output.txt")
    
    assert output == expect
    
test_no_seq()