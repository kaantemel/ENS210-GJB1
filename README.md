# ENS210 Term Project

## 1. Purpose
  The aim of this project is to identify the most conserved domains of the GJB1
  protein in order to determine the most conserved residues, on which pathogenic
  mutations can occur, and model possible mutations on the protein. 

## 2. Project Structure
  ### 2.1 Report And Proposal
  Detailed description can be found in the An Analysis of Gap Junction Beta-1 Protein File
  and detailed description of the proposal can be found in Proposal.md
  ### 2.2 Scripts
    aligndropping.py -> Drops duplicate alignments
    outgroupfinder.py -> Finds outgroup to be rerooted with PPM
    helper.py -> Contains helping functions 
    shannonentropycalculator.py -> Calculates Shannon entropy for aligned sequences
    rcodesforgraphs.R -> Script to create graph from R
  ### 2.3 Sequences and Aligments
  * Blast
    MSA_blast.fasta -> homologs that found from blast
    blast_aligned_dropped_duplicated.clustal -> alignment of dropped duplications clustal version
    blast_aligned_dropped_duplicated.fasta -> alignment of dropped duplications fasta version
  * Mafft
    abnormal_85.fasta -> Sequences that found with Python script (abnormal ones)
    abnormal_85_mafft_aligned.fasta -> Sequences that found with Python script aligned (abnormal ones)
    normal_883.fasta -> Sequences that found with Python script (normal ones)
    normal_883_mafft_aligned.fasta -> Sequences that found with Python script aligned (normal ones)
  ### 2.4 Trees
    bigTree_colored.nwk -> Maximum likelihood tree of 974 sequence that found with colored according to normal abnormal and other
    painted_85purple_883magenta_6orange.png -> Visualized bigTree_colored.nwk
    rerooted_painted.png -> Visualized bigTree_colored.nwk with outgroup
    smalltree.nwk -> Maximum likelihood tree with mammals, birds, lizards, turtles and amphibians 
    smalltree.nwk.pdf -> Visualized smalltree.nwk

## 3. Methods - Tools
  * UniProt -> To find sequence for GJB1 protein
  * BLAST --> To find sequences of homologs
  * MSAViewer --> To obtain multiple sequence alignment of the Blast query.
  * MAFFT --> To align homolog sequences
  * MEGA --> To create maximum likelihood tree
  * FigTree --> To visualize tree that created with MEGA
  * Python --> To create algorithms for unique problems
  * R (ggplot) --> To create graphs for data that found with Python
  * Meta SNP --> To find disease probabilities of spesific mutations
  * GenBank --> To find sequences of different species that have GJB1 protein
  


