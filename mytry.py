import bayes
import feedparser
listOPosts, listClasses = bayes.loadDataSet()
myVocabList = bayes.createVocabList(listOPosts)

# print(myVocabList)

# print(bayes.setOfWords2Vec(myVocabList, listOPosts[0]))

# trainMat =[]
# for postinDoc in listOPosts:
#     trainMat.append(bayes.setOfWords2Vec(myVocabList, postinDoc))
# p0v, p1v, pAb = bayes.trainNB0(trainMat, listClasses)
# print(p0v)
# print(p1v)
# print(pAb)

# bayes.testingNB()

# bayes.spamTest()

ny = feedparser.parse('http://newyork/craigslist.org/stp/index.rss')
sf = feedparser.parse('http://sfbay/craigslist.org/stp/index.rss')
vocabList, pSF, pNY = bayes.localWords(ny,sf)