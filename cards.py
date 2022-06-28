import random


class Cards():
    def __init__(self,zhuyin):
        import json
        import random

        with open("data/characterData.json", "r", encoding="utf8") as file:
            self.masterList = json.load(file)
        # Create a list of Characters
        self.charList = []
        for key in self.masterList:
            self.charList.append(key)

        self.currentCard = self.getRandom()
        self.userInputString = ""

        self.zhuyin = []
        for item in zhuyin:
            self.zhuyin.append(zhuyin[item])

        #Build Zhuyin Data


        with open("data/pinyinToZhuyin.txt", mode="r", encoding="utf8") as file:
            raw = file.readlines()

        zhuyinDict = {}
        for item in raw:

            item = item.replace("\n", "")
            rawData = item.split("\t", 6)
            zhuyin = [rawData[0], rawData[3]]
            zhuyinDict.update({rawData[3]: rawData[0]})

            pinyinList = []
            for key in zhuyinDict:
                pinyinList.append(key)
            pinyinList.sort(key=len)
            pinyinList.reverse()

        print(zhuyinDict)

        self.zhuyinList = ["ㄅ", "ㄆ", "ㄇ", "ㄈ",
                      "ㄉ", "ㄊ", "ㄋ", "ㄌ",
                      "ㄍ", "ㄎ", "ㄏ", "ㄐ", "ㄑ",
                      "ㄒ", "ㄓ", "ㄔ", "ㄕ", "ㄖ",
                      "ㄗ", "ㄘ", "ㄙ", "ㄧ", "ㄨ", "ㄩ",
                      "ㄚ", "ㄛ", "ㄜ", "ㄝ", "ㄞ",
                      "ㄟ", "ㄠ", "ㄡ", "ㄢ", "ㄣ",
                      "ㄤ", "ㄥ", "ㄦ"]

        self.zhuyinToPinyinDict = {v: k for k, v in zhuyinDict.items()}

        self.deck = 0 # Denotes which dect to use
                        # 0 undecided
                        # 1 zhuyin
                        # 2 Character Cards
        self.index = 0

        self.random = False





#################################
# Fix For spaces in DataBase
#####################################
        for key in self.masterList:
            zhuyin = self.masterList[key]["Zhuyin"]
            if zhuyin.__contains__(" "):
                self.masterList[key]["Zhuyin"]=  self.masterList[key]["Zhuyin"].replace(" ","")



    def printData(self):
        print(self.masterList)

    def search(self,search):
        for key in self.masterList:
            query = self.masterList[key]["Pinyin"]
            if query.__contains__(search):
                return key


    def shuffleCards(self):
        random.shuffle(self.charList)
        self.index = 0


    def getNextCard(self):
        self.userInputString = ""
        self.index = self.index + 1
        if self.deck == 2:
            try:
                card = self.charList[self.index]
            except IndexError:
                self.index = 0
                card = self.charList[self.index]

            zhuyin = self.masterList[card]["Zhuyin"]
            self.currentCard = [card, zhuyin]
            return self.currentCard





    def getRandom(self):
        card = random.choice(self.charList)
        zhuyin = self.masterList[card]["Zhuyin"]
        self.currentCard = [card,zhuyin]
        print(self.currentCard)
        self.userInputString = ""
        return self.currentCard

    def getNext(self):
        for i in range(len(self.charList)):
            if self.currentCard[0] == self.charList[i]:
                try:
                    card = self.charList[i + 1]
                    zhuyin = self.masterList[card]["Zhuyin"]
                    self.currentCard = [card, zhuyin]
                    return self.currentCard
                except IndexError:
                    card = self.charList[0]
                    zhuyin = self.masterList[card]["Zhuyin"]
                    self.currentCard = [card, zhuyin]
                    return self.currentCard

    def userInput(self,keyPressed):
        index = len(self.userInputString)
        zhuyin = self.currentCard[1]
        try:
            if keyPressed == zhuyin[index]:
                print("here")
                self.userInputString = self.userInputString + zhuyin[index]
                print(self.userInputString)
                return self.userInputString
        except IndexError:
            return self.userInputString

    def checkCard(self):
        if self.userInputString == self.currentCard[1]:
            return True
        else:
            return False

    def getNextZhuyin(self):
        if self.random == False:
            try:
                zhuyin = self.zhuyinList[self.index + 1]
                self.index = self.index + 1
            except IndexError:
                self.index = 0
                zhuyin = self.zhuyinList[self.index]

            pinyin = self.zhuyinToPinyinDict[zhuyin]

            card = [pinyin,zhuyin]
            return card
        else:
            self.index = random.randint(0,len(self.zhuyinList)-1)
            zhuyin = self.zhuyinList[self.index]
            pinyin = self.zhuyinToPinyinDict[zhuyin]
            card = [pinyin, zhuyin]
            return card

    def setFirstZhuyin(self):
        if self.random == False:
            self.index = 0
            zhuyin = self.zhuyin[self.index]
            pinyin = self.zhuyinToPinyinDict[zhuyin]
            card = [pinyin, zhuyin]
            return card
        else:
            self.index = random.randint(0,len(self.zhuyinList) - 1)
            zhuyin = self.zhuyinList[self.index]
            pinyin = self.zhuyinToPinyinDict[zhuyin]
            card = [pinyin, zhuyin]
            return card

    def getCurrentZhuyinCard(self):
        return self.zhuyinList[self.index]

    def userInputZhuyin(self, keyPressed):
        zhuyin = self.zhuyinList[self.index]
        if keyPressed ==  zhuyin:
            self.userInputString = zhuyin
            return self.userInputString

    def checkZhuyinCard(self):
        if self.userInputString == self.zhuyinList[self.index]:
            return True
        else:
            return False

            # index = len(self.userInputString)
            # zhuyin = self.currentCard[1]
            # try:
            #     if keyPressed == zhuyin[index]:
            #         print("here")
            #         self.userInputString = self.userInputString + zhuyin[index]
            #         print(self.userInputString)
            #         return self.userInputString
            # except IndexError:
            #     return self.userInputString

        # for i in range(len(self.charList)):
        #     if self.currentCard[0] == self.charList[i]:
        #         try:
        #             card = self.charList[i + 1]
        #             zhuyin = self.masterList[card]["Zhuyin"]
        #             self.currentCard = [card, zhuyin]
        #             return self.currentCard
        #         except IndexError:
        #             card = self.charList[0]
        #             zhuyin = self.masterList[card]["Zhuyin"]
        #             self.currentCard = [card, zhuyin]
        #             return self.currentCard
        #

