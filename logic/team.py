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

    def _init_(self, team_list, file_name):
        if not isinstance(team_list, list):
            return None
        self.__players = {team.POS_CARRY: team_list[team.OFF_CARRY], team.POS_MID: team_list[team.OFF_MID],
                          team.POS_OFFLINE: team_list[team.OFF_OFFLINE], team.POS_SUPPORT: team_list[team.OFF_SUPPORT],
                          team.POS_HARDSUP: team_list[team.OFF_HARDSUP]}
        stand = []
        for li in team_list[team.OFF_STANDIN:]:
            stand.append(li)
        self.__players[team.POS_STANDIN] = stand

        self.__gameDict = {"games": 0, "won": 0, "majorPoint": 0}
        with open(file_name, "r") as out:
            self.__gameDict = json.load(out)

    def gen_game_dict(self, fileName):
        game_dict = {"games":0, "won":0, "majorPoint":0}
        with open(fileName, "w") as outStream:
            json.dump()

    def add_game(self, gameDict):
        # get win or lose status
        winStatus = [gameDict["id"], gameDict["win"]]
        self.__gameDict["winStatus"].append(winStatus)
        if gameDict["win"] == "win":
            self.__gameDict["won"] += 1
        # get hero status
        self.__gameDict["heroes"].append(gameDict["heroes"])
        self.__gameDict["time"].append(gameDict["time"])
        self.__gameDict["date"].append(gameDict["date"])
        self.__gameDict["KDA"].append(gameDict["KDA"])
        self.__gameDict["XPM"].append(gameDict["XPM"])
        self.__gameDict["GPM"].append(gameDict["GPM"])
        self.__gameDict["games"] += 1

    def player_add(self, player_pos, play_dict):
        self.__players[player_pos].addGame(play_dict)

    def get_style(self):
        return self.__gameDict["style"]

    def gen_style(self):
        return None

    def get_win_rate(self):
        if self.__gameDict["games"] == 0:
            return 0
        return self.__gameDict["won"] / self.__gameDict["games"]

    def get_major_point(self):
        self.__gameDict["majorPoint"] = self.__players[team.POS_HARDSUP].getMP() \
                                        + self.__players[team.POS_CARRY].getMP() + self.__players[
                                            team.POS_OFFLINE].getMP() \
                                        + self.__players[team.POS_MID].getMP() + self.__players[
                                            team.POS_SUPPORT].getMP()
        return self.__gameDict["majorPoint"]

    def add_major_point(self, ponit):
        for player in self.__gameDict["majorPoint"].keys():
            self.__gameDict[player].addMP(ponit)

    def store_in_json(self, fileName):
        with open(fileName, "w") as out:
            json.dump(self.__gameDict, out)

    def store_in_csv(self, file_name):
        data = []
        header = ["id", "win", "heroes", "time", "date", "K", "D",
                  "A", "GPM", "XPM"]
        data.append(header)

        for i in range(0, self.__gameDict["games"]):
            row = [self.__gameDict["id"][i], self.__gameDict["win"][i], self.__gameDict["heroes"][i],
                   self.__gameDict["time"][i], self.__gameDict["date"][i], self.__gameDict["K"][i][0],
                   self.__gameDict["D"][i][1], self.__gameDict["A"][i][2], self.__gameDict["GPM"][i],
                   self.__gameDict["XPM"][i]]
            data.append(row)
        with open(file_name, "w") as out:
            w = csv.writer(out)
            w.writerows(data)

    def get_dict(self):
        return self.__gameDicts
