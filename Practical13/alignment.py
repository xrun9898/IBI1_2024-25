from Bio import SeqIO
import blosum as bl

def load_seq(file):
    return str(next(SeqIO.parse(file, 'fasta')).seq)

human_seq = load_seq('C:/Users/Xutianrun/Desktop/IBI1_2024-25/Practical13/human.fasta')
mouse_seq = load_seq('C:/Users/Xutianrun/Desktop/IBI1_2024-25/Practical13/mouse.fasta')
random_seq = load_seq('C:/Users/Xutianrun/Desktop/IBI1_2024-25/Practical13/random.fasta')

blosum62 = bl.BLOSUM(62)
def calculate_score(seq1, seq2):
    id= 0
    scores = 0
    for a1, a2 in zip(seq1, seq2 ):
        score =blosum62[a1][a2]
        scores+= score
        if a1 == a2:
            id +=1
    
    id_persent= (id/222)*100
    return scores, id_persent
score1, id1 =calculate_score(human_seq,mouse_seq)
score2, id2 =calculate_score(human_seq,random_seq)
score3, id3 =calculate_score(random_seq,mouse_seq)



print(f'The Hamming distance between human and mouse SOD2 sequences is: {score1}, and the percentage of identical amino acids is: {id1}%')
print(f'The Hamming distance between human SOD2 sequence and random sequence is: {score2}, and the percentage of identical amino acids is: {id2}%')
print(f'The Hamming distance between mouse SOD2 sequence and random sequence is: {score3}, and the percentage of identical amino acids is: {id3}%')