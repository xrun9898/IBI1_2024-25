def find_restriction_sites(dnaSequence, recognitionSequence):  

    cut_sites = []  
  
    dna_length = len(dnaSequence)  
    recog_length = len(recognitionSequence)  
    for n in dnaSequence:
        if n !="A" and n !="C" and n !="G" and n !="T":
            return "There is an error in the dna sequence."
    for n in recognitionSequence:
        if n !="A" and n !="C" and n !="G" and n !="T":
            return "There is an error in the recognition sequence."
    for i in range(dna_length - recog_length + 1):    
        if dnaSequence[i:i + recog_length] == recognitionSequence:  
            cut_sites.append(i)  
    if cut_sites == [] :
        return "can't find restriction site"
    return cut_sites  

dna_sequence = "ACGTACGTGACGTACG"  
recognition_sequence = "ACGT"  
result = find_restriction_sites(dna_sequence, recognition_sequence)  
print("Restriction endonuclease cleavage site:", result)  
dnaSequence =input("input dna sequence") 
recognitionSequence = input("input recognition sequence")
result = find_restriction_sites(dnaSequence, recognitionSequence)  
print("Restriction endonuclease cleavage site:", result)  
