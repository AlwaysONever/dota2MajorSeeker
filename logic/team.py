import json

class team():
	POS_CARRY = 1
	POS_MID = 2
	POS_OFFLINE = 4
	POS_SUPPORT = 8
	POS_HARDSUP = 16
	POS_STANDIN = 0
	OFF_CARRY = 0
	OFF_MID = 1
	OFF_OFFLINE = 2
	OFF_SUPPORT = 3
	OFF_HARDSUP = 4
	OFF_STANDIN = 5
	
	def _init_(self, teamList):
		if not isinstance(teamList, list)
			return None
		self.__players[POS_CARRY] = teamList[OFF_CARRY]
		self.__players[POS_MID] = teamList[OFF_MID]
		self.__players[POS_OFFLINE] = teamList[OFF_OFFLINE]
		self.__players[POS_SUPPORT] = teamList[OFF_SUPPORT]
		self.__players[POS_HARDSUP] = teamList[OFF_HARDSUP]
		stand = ""
		for li in teamList[OFF_STANDIN:]:
			stand.append(li)
		self.__players[POS_STANDIN] = stand
	
	def loadGameJSON(self, fileName):
		with open(fileName) as outStream:
			self.__gameDict = json.load(outStream)
	
	def addGame(self, gameDict):
	
	
	def playerAdd(self, playerRef):
	
	def getStyle(self):
	
	def genStyle(self):
	
	def getWinRate(self):
	
	def getMajorPonit(self):
	
	def addMajorPonit(self, ponit):
	
	def storeInJSON(self, fileName):
	
	def storeInCSV(self, fileName):
	
	def getDict(self):
	
	
		