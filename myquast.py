from Bio import SeqIO
from Bio.Sequencing import Ace

def myquast(contig_file):

    contigs = []#["ATTTATT","TACGAGAG","ATTGGGC","GGAGAGAGAGGAGAGGAGA","GGA"]
    with open(contig_file,"r") as f:
        for rec in SeqIO.parse(f, "fasta"):
            s = rec.seq
            contigs.append(s)


    # get contig stats
    l = len(contigs)

    total_l = 0
    contig_lengths = [0]*l

    for i in range(l):
       contig_lengths[i] = len(contigs[i])
       total_l += len(contigs[i])
    longest_contig = max(contig_lengths)

    #n50
    contig_lengths.sort()
    c = 0
    h = 0
    while c < total_l/2:
        n50 = contig_lengths[h]
        c += contig_lengths[h]
        h +=1




    #report
    #print("N50", n50)
    #print("amount of contigs ", l)
    #print("total length ", total_l)
    #print("longest contig ",longest_contig)


    fil = open("ContigsReport.txt", "w")
    fil.write("N50  ")
    fil.write(str(n50))
    fil.write("\namount of contigs  ")
    fil.write(str(l))
    fil.write("\ntotal length  ")
    fil.write(str(total_l))
    fil.write("\nlongest contig  ")
    fil.write(str(longest_contig))
    fil.close()


