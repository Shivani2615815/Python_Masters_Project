Follow the step by step execution as:

Part 1->
Step 1:Use 'RelA.fasta' as input and run the command python part1.py <fasta_file> <CONSENSUS>(Example: python part1.py RelA.fasta GGGRNWYYCC) in the terminal. A .txt file 'part1_output.txt' with list of Input sequences, Sequence id, Description and TFBS sequences will be the output.

Step2: Use'test_file_part1.txt' as input and run python test_part1.py in the terminal. (Alternatively use: pytest)
The execution should complete without any error and pytest should give "Passed".


Part 2->
Step 1: Open part2.ipynb and run chunk (a). Use 'part1.output.txt' as input and then run common_seq("part1_output.txt"). A dictionary with top 10 consensus conforming sequence with the number of occurrence will be the output. {'sequence' : 'count', ….}

Step 2: Run chunk (b) of part2.ipynb and use'RelA.fasta' and 'part1.output.txt' as input. Execute no_seq("RelA.fasta","part1_output.txt"). The output is an integer which is the number of sequence that does not have any consensus conforming sequence.

Step 3: Execute plot1() and plot 2() functions (chunk (c) and chunk (d)) to view plots explaining the outputs.

Step 4: Use 'test_part2_input.fasta' and 'test_part2_output.txt' and execute python test_part2.py (Run pip install import-ipynb if needed) in the terminal. (Alternatively use: pytest)The execution should complete without any error and pytest should give "Passed".


Part 3->
Step 1: Read part3.pdf
