# Twitter Message Train & Classification by Weka

## Program Description
This program used gensim, Word2Vec and Weka to evaluate twitter message was relevant or irrelevant.
### Requirements
* Generate vectors using Word2Vec as features. You may employ any library supporting Word2Vec, such as Gensim (https://radimrehurek.com/gensim/models/word2vec.html);
* Use Support Vector Machines (SVM) algorithm for classification. You may employ any library implementing the SVM algorithm, such as Weka (http://www.cs.waikato.ac.nz/ml/weka/).
Description of the attached files:


* source code (Python and/or Java);
* README with instructions how to run the code;
* report consisting of 990 lines, where:
    - First line is formatted as follows: `True positives: \tFalse positives: \tTrue negatives: \tFalse negatives: \n`
    - Second line is formatted as follows: `Precision: \tRecall: \tF1-score: \n`
    - All other 988 lines are formatted as follows (without <> symbols): `<tweet's id>\t<label computed for a given tweet from the evaluation dataset>\n`

## How to Run the Program
1. You need IDE to run the Java and Python.
2. You will need to install Gensim
    - `sudo pip install --upgrade gensim`
3. Download Weka.
4. Download Word2Vec.
5. Run "getVector.py" to get arff file.
6. Run "Classify.java" to classify the file.

### Sample output

```
True positives: 0.895749	False positives: 0.076226	True negatives: 0.923774	False negatives: 0.104251
Precision: 0.933080	Recall: 0.895749	F1-score: 0.906193
543410294513340417	relevant
543754183866724352	relevant
544846763840921600	relevant
543603391755460609	relevant
......
```
