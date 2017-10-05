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
		if not isinstance(teamList, list):
			return None
		self.__players = {team.POS_CARRY: teamList[team.OFF_CARRY], team.POS_MID: teamList[team.OFF_MID],
						  team.POS_OFFLINE: teamList[team.OFF_OFFLINE], team.POS_SUPPORT: teamList[team.OFF_SUPPORT],
						  team.POS_HARDSUP: teamList[team.OFF_HARDSUP]}
		stand = []
		for li in teamList[team.OFF_STANDIN:]:
			stand.append(li)
		self.__players[team.POS_STANDIN] = stand
	
	def loadGameJSON(self, fileName):
		with open(fileName) as outStream:
			self.__gameDict = json.load(outStream)
	
	def addGame(self, gameDict):
		#get win or lose status
		winStatus = [gameDict["id"], gameDict["win"]]
		self.__gameDict["winStatus"].append(winStatus)
		if gameDict["win"] == "win":
			self.__gameDict["won"] += 1
		#get hero status
		self.__gameDict["heros"].append(gameDict["heros"])
		self.__gameDict["time"].append(gameDict["time"])
		self.__gameDict["date"].append(gameDict["date"])
		self.__gameDict["KDA"].append(gameDict["KDA"])
		self.__gameDict["XPM"].append(gameDict["XPM"])
		self.__gameDict["GPM"].append(gameDict["GPM"])
			
	def playerAdd(self, playerPos, playDict):
		self.__players[playerPos].addGame(playDict)
		
	def getStyle(self):
		return self.__gameDict["style"]
		
	def genStyle(self):
		
	def getWinRate(self):
		
	def getMajorPonit(self):
	
	def addMajorPonit(self, ponit):
	
	def storeInJSON(self, fileName):
	
	def storeInCSV(self, fileName):
	
	def getDict(self):
	
	
		