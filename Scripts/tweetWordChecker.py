#Script used to parse a given users tweets and return a frequency chart for words used in the past day
import yaml
import datetime
import json
def main(author):
    todaysDate = datetime.datetime.now()
    todaysDate = todaysDate.strftime("%Y-%m-%d")
    fileName = "Data/" + author + todaysDate + ".yaml"
    print("This is the main function")
    allTweets = gatherTweets("Elon")
    tweetNum = 1
    tweetsParsed = {}
    for tweet in allTweets:
        tweetName = author + "-Tweet-" + str(tweetNum)
        tweetNum += 1
        tweetInfo = parseTweet(tweet)
        newTweetInfo = {tweetName : tweetInfo}
        tweetsParsed.update(newTweetInfo)
    FinalData = aggregateData(tweetsParsed)
    saveData(fileName, FinalData)
def parseTweet(tweet):
    #Method to parse a given tween and return a dict containing the word and its frequency in the tweet
    ignoreList = ['a', 'of', 'the', 'is', 'at', 'or', 'to', 'on']
    seperatorList = [';', ',', ':', ".", '/', "?", "."]
    print(tweet)
    #remove characters that cause issues such as ’
    if "’" in tweet:
        tweet = tweet.replace("’", "")
    for seperator in seperatorList:
        if seperator in tweet:
            tweet = tweet.replace(seperator, " ")
    tweetAsWords = tweet.split(" ")
    #remove all common words that likely contain no relevance
    for word in tweetAsWords:
        if word in ignoreList:
            tweetAsWords.remove(word)


    #initialize frequency dict
    frequencyDict = {}
    #create a dict containing a word and its frequency in the tweet
    for word in tweetAsWords:
        if word not in frequencyDict and not word in seperatorList and not '' == word:
            frequencyDict.update({word : 1})
        else:
            if word in frequencyDict:
                frequencyDict[word] = frequencyDict[word] + 1
    
    return frequencyDict

def saveData(fileName, tweetsDict):
    with open (fileName, "a") as f:
        f.write(yaml.safe_dump(tweetsDict))
        f.close()

def gatherTweets(username):
    #place holder to gather tweets as strings
    tweets = []
    tweet1 = 'Once again, I’d like to offer this platform to anyone on the left. You will get equal treatment.'
    tweet2 = 'Falcon 9 launches 52 @Starlink satellites to orbit from Florida'
    tweets.append(tweet1)
    tweets.append(tweet2)
    return tweets

def aggregateData(tweetsParsed):
    CombineTweetDict = {}
    for tweet in tweetsParsed:
        wordFrequency = tweetsParsed[tweet]
        for word in wordFrequency:
            if word not in CombineTweetDict:
                CombineTweetDict.update({word : 1})
            else:
                CombineTweetDict[word] = CombineTweetDict[word] + 1
    return CombineTweetDict
main("ElonMusk")