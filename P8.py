def read_codons(fname):
    d = {}
    with open(fname, 'r') as f:
        for line in f:
            k, v = line.strip().split('=')
            d[k] = v
    return d

def codon(codon_table, gene):
    cod_tab = read_codons(codon_table)

    # Read the gene sequence file
    with open(gene, 'r') as f:
        lines = f.readlines()
    
    # Skip the first line (URL) and concatenate the rest of the lines
    dna = ''.join(line.strip() for line in lines[1:])

    # Translate each 3-letter set in DNA sequence to an amino acid
    polypep = []
    for i in range(0, len(dna) - 2, 3):
        codon = dna[i:i+3]
        if codon in cod_tab:
            polypep.append(cod_tab[codon])
        else:
            polypep.append('?')  # Handle unknown codons

    return polypep

if __name__ == '__main__':
    res = codon('codons.txt', 'homo_sapiens_mitochondrion.txt')
    print(res)
    print(len(res))
