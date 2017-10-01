import json

class DoubleWin():
	
	TEAM_NAME = 0
	TEAM_BITMAP = 1
	
	def _init_(self, list):
		#get team list
		self.__teamList = list
		#get mask for caculate upper bracket
		seed = list[-1]
		self.__mask = seed[TEAM_BITMAP]
	
	def addWin(self, winner, loser):
		#second member in every team will be set to be 2 after first initailization , 
		#and the first member is the name of that team. 
		for team in self.__teamList:
			if team[TEAM_NAME] == winner:
				#if a team wins a total bo, set a bit signal
				temp = team[TEAM_BITMAP] * 2
				team[TEAM_BITMAP] |= temp
			else if team[TEAM_NAME] == loser:
				#if it lose one game, set lower bracket bit on ---- last bit stand for lower bracket
				temp = team[TEAM_BITMAP] | 1
			
	def end(self):
		return self.__teamList
		
	def endAndGen(self):
		#generate schedlue
		resultList = ""
		for value in values(1:self.__mask):
			bracket = ""
			for team in self.__teamList:
				if team[TEAM_BITMAP] == value:
					bracket.append(team)
			resultList.append(bracket)
		return resultList
		
	def endAndGenAndStoreInJSON(self, fileName):
		resuilt = self.endAndGen(self)
		with open(fileName, "a") as outStream:
			json.dump(outStream, resuilt)
		
		