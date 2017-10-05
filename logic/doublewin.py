import json
import csv

class DoubleWin():
	
	TEAM_NAME = 0
	TEAM_BITMAP = 1
	TEAM_POINT = 2
	UPPER_BRACKET = 1
	POINT_MASK = 16
	
	def _init_(self, list):
		#get team list
		self.__teamList = list
		#get mask for caculate upper bracket
		seed = list[-1]
		self.__mask = seed[DoubleWin.TEAM_BITMAP]
		self.__resultList = None
		self.__turnsDict = []
		i = 2
		j = 1
		while i <= self.__mask:
			self.__turnsDict[i] = j
			j += 1
			i = i << 1
		
	
	def addWin(self, winner, winp, loser, losp):
		#second member in every team will be set to be 2 after first initailization , 
		#and the first member is the name of that team. 
		for team in self.__teamList:
			if team[DoubleWin.TEAM_NAME] == winner:
				#if a team wins a total bo, set a bit signal
				temp = team[DoubleWin.TEAM_BITMAP] * 2
				team[DoubleWin.TEAM_BITMAP] |= temp
				#point high 4 bits stand for lose games, and low 4 bits stand for win games
				team[DoubleWin.TEAM_POINT].append(winp)
			elif team[DoubleWin.TEAM_NAME] == loser:
				#if it lose one game, set lower bracket bit on ---- last bit stand for lower bracket
				temp = team[DoubleWin.TEAM_BITMAP] | DoubleWin.UPPER_BRACKET
				team[DoubleWin.TEAM_POINT].append(losp)
			
	def end(self):
		return self.__teamList
		
	def endAndGen(self):
		#generate schedlue
		resultList = []
		for value in range(1,self.__mask):
			bracket = []
			for team in self.__teamList:
				if team[DoubleWin.TEAM_BITMAP] == value:
					bracket.append(team)
			resultList.append(bracket)
		self.__resultList = resultList
		return resultList
		
	def storeInJSON(self, fileName):
		if self.__resultList == None:
			return False
		resuilt = self.endAndGen()
		with open(fileName, "w") as outStream:
			json.dump(outStream, resuilt)
		return True
	def storeInCSV(self, fileName):
		if self.__resultList == None:
			return False
		data = []
		header = ["team", "turn", "win", "winrate"]
		data.append(header)
		dict = self.__turnsDict
		for li in self.__resultList:
			row = []
			row.append(li[DoubleWin.TEAM_NAME])
			bitmap = li[DoubleWin.TEAM_BITMAP]
			mask = bitmap & self.__mask
			bracket = bitmap & DoubleWin.UPPER_BRACKET
			if bracket == DoubleWin.UPPER_BRACKET:
				turn = "upper bracket" + str(self.__turnsDict[mask])
			else:
				turn = "lower bracket" + str(self.__turnsDict[mask])
			row.append(turn)
			
			ponits = li[DoubleWin.TEAM_POINT]
			point = 0 
			loss = 0
			for p in ponits:
				lp = p >> 8
				lp &= mask
				p &= mask
				point += p
				loss += lp
			row.append(point)
			plus = point + loss
			winrate = loss / plus
			row.append(winrate)
			data.append(row)
		with open(fileName, "w") as outStream:
			w = csv.reader(outStream)
			w.writerows(data)
			
		
		
		