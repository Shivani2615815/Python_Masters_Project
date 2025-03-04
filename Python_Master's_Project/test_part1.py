# Use: python test_part1.py
#Alternatively use: pytest

#importing modules
import pytest
from part1 import find_tfbs, script_op
from Bio import SeqIO

def test_find_tfbs():
    """
    This function checks if find_tfbs function from part1 
    module performs the tfbs search correctly by comparing 
    expected output with actual output.
    """
    sequence = 'GGGAGTTTCCGGGAATTCCC'
    consensus = 'GGGRNWYY'   
    #the expected output is computed manually
    expect = ['GGGAGTTT', 'GGGAATTC'] 
    output = find_tfbs(sequence, consensus)
    assert output == expect
test_find_tfbs()

def test_script_op():
    """
    This function checks if script_op function from part1 
    module performs reading and writing into file 
    correctly by comparing expected output with actual 
    output.
    """
    expect = open("test_file_part1.txt").readlines()
    script_op("RelA.fasta",'GGGRNWYYCC')
    output = open("part1_output.txt").readlines()
    assert output == expect
test_script_op()

def test_tsv(op_file):
    """
    This function checks if the output generated from part1 script
    consists of tab separated values.
    """
    try:
        with open(op_file, 'r') as file:
            lines = file.readlines()
            assert any('\t' not in n for n in lines)
    except FileNotFoundError:
        return False
@pytest.fixture
def op_file():
    return "part1_output.txt"