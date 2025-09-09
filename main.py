"""
Simple DNA Sequence Analysis Tool
Author: Abubakar Saeed
Description:
    A demo bioinformatics script to analyze DNA sequences.
    - Reads FASTA file
    - Calculates basic statistics (length, GC content)
    - Finds simple open reading frames (ORFs)
"""

from typing import Dict, List

# Function to read a FASTA file
def read_fasta(file_path: str) -> Dict[str, str]:
    sequences = {}
    seq_id = ""
    seq_data = []
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if seq_id:
                    sequences[seq_id] = "".join(seq_data)
                    seq_data = []
                seq_id = line[1:]
            else:
                seq_data.append(line.upper())
        if seq_id:
            sequences[seq_id] = "".join(seq_data)
    return sequences


# Function to calculate GC content
def gc_content(seq: str) -> float:
    g = seq.count("G")
    c = seq.count("C")
    return round((g + c) / len(seq) * 100, 2) if len(seq) > 0 else 0.0


# Function to find simple ORFs (start codon = ATG, stop codons = TAA, TAG, TGA)
def find_orfs(seq: str) -> List[str]:
    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]
    orfs = []
    for i in range(len(seq) - 2):
        codon = seq[i:i+3]
        if codon == start_codon:
            for j in range(i+3, len(seq)-2, 3):
                stop_codon = seq[j:j+3]
                if stop_codon in stop_codons:
                    orfs.append(seq[i:j+3])
                    break
    return orfs


# Main demo
if __name__ == "__main__":
    fasta_file = "example.fasta"  # Replace with your FASTA file
    sequences = read_fasta(fasta_file)

    for seq_id, seq in sequences.items():
        print(f"\nSequence ID: {seq_id}")
        print(f"Length: {len(seq)} bp")
        print(f"GC Content: {gc_content(seq)}%")
        orfs = find_orfs(seq)
        print(f"Number of ORFs found: {len(orfs)}")
        if orfs:
            print(f"First ORF (length {len(orfs[0])}): {orfs[0][:60]}...")
