import re

splice_combinations=['GTAG','GCAG','ATAC']
splice_input=input(f'enter splice combination {splice_combinations[:]}').strip().upper()
while splice_input not in splice_combinations: 
    print('invalid input. try again')
    splice_input=input(f'enter splice combination {splice_combinations[:]}').strip().upper()
output_filename=f'{splice_input}_spliced_genes.fa'

with open('Practical7/tata_genes.fa', 'r') as infile, open(output_filename, 'w') as outfile:
    current_gene=[]
    current_sequence=[]
    tata_pattern=re.compile(r'TATA[AT]A[AT]')
    gene_name_pattern=re.compile(r'gene:(\S+)')
    splice_pattern=re.compile(fr'{splice_input[:2]}.*?{splice_input[-2:]}')

    for line in infile: 
        if gene_name_pattern.search(line):
            if current_gene and current_sequence:
                full_sequence=''.join(seq.strip() for seq in current_sequence)
                if splice_pattern.search(full_sequence):
                    splice_seq=splice_pattern.findall(full_sequence)
                    tata_box_number=0
                    for i in splice_seq:
                        if tata_pattern.search(i):
                            tata_box_seq=tata_pattern.findall(i)
                            tata_box_number+=len(tata_box_seq)
                            outfile.write(f'>{current_gene[0]}, the number of instances of TATA box is {tata_box_number} \n')
                            outfile.writelines(current_sequence)                 
            current_gene=gene_name_pattern.findall(line)
            current_sequence=[]

        else:
            current_sequence.append(line) 

    if current_gene and current_sequence:
        full_sequence=''.join(line.strip() for line in current_sequence)
        if splice_pattern.search(full_sequence):
            splice_seq=splice_pattern.findall(full_sequence)
            for i in splice_seq:
                if tata_pattern.search(i):
                    tata_box_seq=tata_pattern.findall(i)
                    tata_box_number+=len(tata_box_seq)
            outfile.write(f'>{current_gene[0]}, the number of instances of TATA box is {tata_box_number} \n')
            outfile.writelines(current_sequence)