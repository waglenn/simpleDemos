import random

class LetterData:
    def __init__(self, letter):
        self.count = 1
        self.letter = letter
        self.next = {}

    def increment(self):
        self.count += 1

    def addNext(self, nextLetter):
        if nextLetter in self.next:
            self.next[nextLetter].increment()
        else:
            self.next[nextLetter] = LetterData(nextLetter)

    def getCount(self):
        return self.count

    def getCountList(self):
        countList = []
        for letter, data in self.next.items():
            countList.append( [letter, data.getCount()] )

        return countList

def weightedChoice(countList):
    sumOfWeights = 0
    for letter, count in countList:
        sumOfWeights += count
    randChoice = random.randint(0, sumOfWeights - 1)
    for letter, count in countList:
        if randChoice < count:
            return letter
        else:
            randChoice -= count
    return ""


def testLetterData():
    passed = True
    ld = LetterData("$")
    testData = ["a","b","c","d",
                "e","f","g","h",
                "A","B","C","D",
                "A","A","A","A",
                "b","b","b","b"]
    for letter in testData:
       ld.addNext(letter)
   
    cl = ld.getCountList()

    for letter, count in cl:
        print("letter '%c', count %d" % (letter, count))
        expected = testData.count(letter) 
        if count == 0:
            print("Got '%c' but that wasn't in the test data" % (letter))
            passed = False
        elif expected != count:
            print("Expected %d '%c' but got %d" % (expected,
                                                   letter,
                                                   count))
            passed = False
    return passed

def testWeightedChoice():
    testData = ["a","b","c","d",
                "e","f","g","h",
                "A","B","C","D",
                "A","A","A","A",
                "b","b","b","b"]
    testResults = []
    ld = LetterData("$")
    for letter in testData:
        ld.addNext(letter)

    cl = ld.getCountList()

    for i in range(len(testData)):
        testResults.append(weightedChoice(cl))

    print("Weighted random result counts:")
    uniqueData = []
    [uniqueData.append(x) for x in testData if x not in uniqueData]
    for x in uniqueData:
        print("letter %c, count %d" % (x, testResults.count(x)))
    return len(testData) == len(testResults)
    

if __name__ == "__main__":
    passed = testLetterData()
    print("letter data test passed: %s" % (str(passed)))
    testWeightedChoice()    
    print("weighted choice test passed: %s" % (str(passed)))
