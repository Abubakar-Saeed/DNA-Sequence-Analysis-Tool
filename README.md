# 🧬 DNA Sequence Analysis Tool  

A simple Python demo project for bioinformatics, designed to analyze DNA sequences from FASTA files.  

This tool performs:  
- ✅ Reading DNA sequences from FASTA format  
- ✅ Calculating sequence length and GC content  
- ✅ Finding simple open reading frames (ORFs)  

---

## 📂 Example FASTA file  

```fasta
>seq1
ATGCGTATCGATCGATCGATCGGCTAGCTAGCTAA
>seq2
ATGCCCGGGTTTAAACCCGGGTTTATGTAG
```

#  🚀 Usage

Clone the repository:
git clone https://github.com/yourusername/dna-sequence-analysis.git
cd dna-sequence-analysis

Run the script:

python dna_analysis.py
Example Output:

Sequence ID: seq1
Length: 34 bp
GC Content: 50.0%
Number of ORFs found: 1
First ORF (length 33): ATGCGTATCGATCGATCGATCGGCTAGCTAGC...

Sequence ID: seq2
Length: 29 bp
GC Content: 55.17%
Number of ORFs found: 1
First ORF (length 6): ATGCCC...

# 📘 Project Structure
dna-sequence-analysis/

│── dna_analysis.py       # Main script
│── example.fasta         # Example FASTA file
│── README.md             # Documentation

# 🎯 Future Work
Translation of DNA → protein sequences
Integration with BLAST for sequence similarity search
Visualization of GC content along the genome
# 👨‍💻 Author

Abubakar Saeed
Bachelor’s in Computer Science (Final Year)
Research interests: AI, Machine Learning, and Bioinformatics

