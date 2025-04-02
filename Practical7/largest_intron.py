'''import re  
Define the gene sequence  
Define the regex pattern to find GT followed by any sequence of nucleotides and ending with AG  
Find all matches in the sequence  
Get the lengths of all the identified introns  
Determine the largest intron length  
'''
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
import re  
pattern = r'GT(.*?)AG'   
matches = re.findall(pattern, seq)    
intron_lengths = [len(match) for match in matches]  
if intron_lengths:  
    largest_intron_length = max(intron_lengths)  
    print(f'the length of the largest intron is: {largest_intron_length}')  
else:  
    print('no introns found')  