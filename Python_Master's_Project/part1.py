# This script finds all present TFBs which comply with a user-specified consensus.
# Use: python part1.py <fasta_file> <consensus> 
# Example: python part1.py RelA.fasta GGGRNWYYCC

#Help on functions: pydoc part1.find_tfbs and  pydoc part1.script_op

# Import all the modules
import sys
from Bio import SeqIO

# The IUPAC nucleic acid notation in a dictionary
notation = {'A': ['A'],
            'C': ['C'],
            'G': ['G'],
            'T': ['T'],
            'U': ['U'],
            'R': ['A','G'],
            'Y': ['C','T'],
            'S': ['G','C'],
            'W': ['A','T'],
            'K': ['G','T'],
            'M': ['A','C'],
            'B' : ['C', 'G', 'T'],
            'D' : ['A', 'G', 'T'],
            'H' : ['A', 'C', 'T'],
            'V' : ['A', 'C', 'G'],
            'N' : ['A', 'C', 'G', 'T'],
            '.': ['gap'],
            '-': ['gap']}

def find_tfbs(sequence, consensus):
    """
    This function finds all the Transcription Factor Binding Sites(tfbs) in a given DNA sequence matching the user entered consensus as per IUPAC notations.
    
    Args:
        sequence (string): The DNA sequence to search TFBS.
        consensus (string) : The short template sequence to check matches in DNA.
            
    Returns:
        A list of Transcription Factor Binding Sites(tfbs)
            
    Raises:
        ValueError if consensus sequence contains invalid characters.

    Example:
        >find_tfbs('GGGAGTTTCCGGGAATTCCC', 'GGGRNWYY') 
        output = ['GGGAGTTT', 'GGGAATTC']           
    """
    # Create a dictionary to put the output
    TFBs = []
    #Convert to upper case
    consensus = consensus.upper()

    #Checkpoint for the users to give correct input
    for con_char in consensus:
        if con_char not in notation and con_char not in ['.', '-']:
            raise ValueError(f"Invalid consensus'{con_char}'!")
            
    # Loop through the sequence to find nucleic acid stretches
    for i in range(len(sequence)-len(consensus)+1):
        substring = sequence[i:i+len(consensus)]
        #loop through consensus to check for matches  
        substring_match = True
        for j in range(len(consensus)):
            #checking character by character
            con_char = consensus[j] 
            substr_char = substring[j]
            #consider gaps
            if con_char == '.' or con_char == '-':
                continue
            #check the condition as per the IUPAC notation
            if con_char not in notation:
                if substr_char != con_char:
                    substring_match = False
                    break
            else:
                if substr_char not in notation[con_char]:
                    substring_match = False
                    break
        #add the nucleotides to list when there is a match
        if substring_match:
            TFBs.append(substring)          
    return TFBs
    
def script_op(fasta_file, consensus):
    """
    This function reads a .fasta file line by line to retrieve sequences, carries out tfbs search (pydoc(find_tfbs)) both in forward and reverse complementary DNA sequences and returns a .txt file with all the tfbs.
    
    Args:
        fasta_file (.fasta): Fasta file containing the DNA sequences.
        consensus (string) : The template to check matches.
            
    Returns:
        A .txt file with all the Transcription Factor Binding Sites(tfbs) found in forward and reverse complement of the DNA sequence with the id.

    Example:
        > script_op("RelA.fasta",'GGGRNWYYCC')
        output = part1_output.txt         
    """
    # Read multiple sequences from file using Biopython
    output = open("part1_output.txt", "w")
    output.write("Read the output as:Input_Sequence->Seq_ID->Description->TFBS_Match_Seq\n\n")
    output.write("Input_Sequence\tSeq_ID\tDescription\tTFBS_Match_Seq\n")
    for seq_input in SeqIO.parse(fasta_file, "fasta"):
        seq_id = seq_input.id
        forward = seq_input.seq
        # Get the reverse complement using Biopython
        reverse = forward.reverse_complement()
        # Add the tfbs of both strands to lists
        forward_list = find_tfbs(forward, consensus)
        reverse_list = find_tfbs(reverse, consensus)

        #write the output into a text file in structured way
        count = 0
        for f in forward_list:
            count += 1
            output.write(f"{forward}\t{seq_id}\tForward_TBFS_{count}\t{f}\n")
        for r in reverse_list:
            count += 1
            output.write(f"{reverse}\t{seq_id}\tReverse_TBFS_{count}\t{r}\n")
    output.close()
           
if __name__ == "__main__":
    try:
        fasta_file = sys.argv[1]
        consensus = sys.argv[2]
    except IndexError:
        print("Provide both a fasta file with DNA sequences and a consensus sequence")
    script_op(fasta_file, str(consensus))
