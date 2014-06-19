import nltk
from nltk.tag.stanford import POSTagger
st = POSTagger('stanford-postagger-2014-01-04/models/english-bidirectional-distsim.tagger','stanford-postagger-2014-01-04/stanford-postagger.jar')
sentence="I am Abhishek Jindal.Don't whether that is good or bad." 
taggedSentence= st.tag(nltk.word_tokenize(sentence))
print taggedSentence