# Multidocument Summarization using SumBasic
Multidocument summarization using the SumBasic implementation. Uses Python3 and nltk.

The SumBasic algorithm is outlined in the following paper: 
Ani Nenkova and Lucy Vanderwende. The Impact of Frequency on Summarization. Microsoft Research,
Redmond, Washington, Tech. Rep. MSR-TR-2005-101. 2005. <https://www.cs.bgu.ac.il/~elhadad/nlp09/sumbasic.pdf>

SumBasic is a multidocument summarization method that determines a frequency distribution of words over every document,
determines the average probability of each sentence based on its word composition, and takes the best scoring sentence of 
the most frequent word until the desired summary length has been reached. A nonredundancy step every iteration updates the
probability of the most frequent word by multiplying it by itself and updating the assigned weights of the sentences
correspondingly.

The variations implemented were:
1. orig: The original version, including the non-redundancy update of the word scores.
2. best_avg: A version of the system that picks the sentence that has the highest average probability
in Step 2, skipping Step 3.
3. simplified: A simplified version of the system that holds the word scores constant and does not
incorporate the non-redundancy update.
4. leading, which takes the leading sentences of one of the articles, up until the word length limit is reached.

Each cluster of testing articles is stored in the docs/ folder. Each file follows docA-B.txt convention, where A is an
positive integer corresponding to the cluster number, and B is another positive integer corresponding to
the article number within that cluster. The testing clusters used were on articles about GM's plant closure in Oshawa, NASA InSight's
first photo taken on Mars, Paul Manafort's alleged secret meeting with Julian Assange, and Zuckerberg's no-show at an international 
committee meeting dedicated to privacy in the UK.

## Usage
`python3 sumbasic.py <method_name> <file_n>*` where <method_name> is one of orig, best_avg, simplified, or leading, and <file_n>* 
is a regex expression of the file path of the cluster, e.g. `docs/doc1-*.txt`.
