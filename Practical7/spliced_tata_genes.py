import re

file = open("tata_genes.fa", "r") 
name=''
while name != 'GTAG' or name != 'GCAG' or name != 'ATAC':
    name = input('input GTAG, GCAG or ATAC ')
newFile = open(f"{name} spliced_genes.fa", "w")

current_header = ""  
current_sequence = ""   

for line in file:  
    line = line.strip()
    if line.startswith('>'):  
        if current_header and current_sequence:  
            match = re.findall(r'TATA[TA]A[TA]', current_sequence)  
            count = str(len(match))    
            newFile.write(current_header +" " + count + "\n")       
            newFile.write(current_sequence + "\n" )  
        current_header = line
        current_sequence = ""  
    else:   
        current_sequence += line  

if current_header and current_sequence:  
    match = re.findall(r'TATA[TA]A[TA]', current_sequence)  
    count = str(len(match))    
    newFile.write(current_header + " " + count + "\n")       
    newFile.write(current_sequence + "\n")   

file.close()  
newFile.close()  
print("finish")  