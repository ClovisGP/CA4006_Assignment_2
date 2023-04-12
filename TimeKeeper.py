from ComEntity import ComEntity
from typing import List
from Config import Config
import time

class TimeKeeper(ComEntity):
    _days: int = 0
    _listTargetedId: List[int]
    _idListUniversity: List[int]

    def __init__(self, id, idListFundingAgency, idListUniversity):
        super().__init__(id)
        self._idListFundingAgency = idListFundingAgency
        self._idListUniversity = idListUniversity
    
    def sendDays(self):
        for targetedId in self._idListFundingAgency:
            self.sendMsg(str(targetedId), str(self._id) + ';' + str(self._days))
        for targetedId in self._idListUniversity:
            self.sendMsg(str(targetedId), str(self._id) + ';' + str(self._days))

    def behaviour(self):
        while (1):
            time.sleep(Config.dayDuration)
            self.sendDays()
            self._days += 1
            