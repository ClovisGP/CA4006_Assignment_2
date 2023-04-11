from typing import List
from enum import Enum

class withDrawResponse(Enum):
    NOT_A_MEMBER = 0
    TAKE_THE_REST = 1
    NORMAL_WITHDRAW = 2
    EMPTY_FUND = 3

class Research:
    _members: List[int]
    _fund: int
    _endTime: str
    _title: str
    _log : List[str] = []

    def __init__(self, memberList, money, endTime, title, idAsker):
        self._members = memberList
        self._fund = money
        self._endTime = endTime
        self._title = title
        self._log.append('Created by ' + str(idAsker))
    
    def addMember(self, newId: str, requester: str):
        if int(newId) not in self._members:
            self._members.append(int(newId))
            self._log.append('The researcher ' + newId + ' was added to the researsh ' + self._title + ' by ' + requester)

    def removeMember(self, targetedId: str, requester: str):
        if int(targetedId) in self._members:
            self._members.remove(int(targetedId))
            self._log.append('The researcher ' + targetedId + ' was removed from the researsh ' + self._title + ' by ' + requester)

    def withdrawMoney(self, amount: str, requester: str):
        if int(requester) not in self._members:
            return withDrawResponse.NOT_A_MEMBER
        if self._fund < 1:
            return withDrawResponse.EMPTY_FUND
        self._fund -= amount
        self._log.append('The researcher ' + requester + ' has  withdraw ' + amount + 'the fund is now of ' + str(self._fund))
        return withDrawResponse.TAKE_THE_REST if self._fund <= 0 else withDrawResponse.NORMAL_WITHDRAW