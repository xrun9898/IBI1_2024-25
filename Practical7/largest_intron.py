import re
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
intron = re.findall(r'GT.*?AG',seq)
if intron:
    longest_intron = max(intron, key=len)
    print("The largest intron is:", longest_intron)
    print("Length:", len(longest_intron))
else:
    print("No intron found.")