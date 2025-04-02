import re  

file = open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r")  
newFile = open("tata_genes.fa", "w")  

gene_pattern = re.compile(r'>.*?gene:(\S+).*?') 
sequence_pattern = re.compile(r'[^>].*?\n')    

current_header = ""  
current_sequence = ""  
  
for line in file:  
    line = line.strip()  
     
    if line.startswith('>'):   
        if current_header and current_sequence:  
            if re.search(r'TATA[TA]A[TA]', current_sequence):  
                newFile.write(current_header + "\n")  
                for i in range(0, len(current_sequence), 100):  
                    newFile.write(current_sequence[i:i+100] + "\n")  
        match = gene_pattern.search(line)  
        if match:  
            current_header = f">gene:{match.group(1)}"   
        current_sequence = ""  
    else:  
        current_sequence += line  
  
if current_header and current_sequence:  
    if re.search(r'TATA[TA]A[TA]', current_sequence):    
        newFile.write(current_header + "\n")  
    
        for i in range(0, len(current_sequence), 100):  
            newFile.write(current_sequence[i:i+100] + "\n")    

file.close()  
newFile.close()  
print("finish")  