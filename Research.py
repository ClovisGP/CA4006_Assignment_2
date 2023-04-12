from typing import List
from Config import withDrawResponse

class Research:
    _members: List[int]
    _fund: int
    _deadLine: int
    _title: str
    _log : List[str] = []
    _nameList: List[str] = []

    def __init__(self, nameList, memberList, money, deadLine, title, idAsker, currentDay: int):
        self._members = memberList
        self._fund = money
        self._deadLine = deadLine
        self._title = title
        self._nameList = nameList
        self._log.append('Created by ' + self._nameList[int(idAsker)] + "on the day " + str(currentDay) + ".")
    
    def addMember(self, newId: str, requester: str, currentDay: int):
        if int(newId) not in self._members:
            self._members.append(int(newId))
            self._log.append('The researcher \"' + self._nameList[int(newId)] + '\" was added by \"' + self._nameList[int(requester)] + "\" on the day " + str(currentDay) + ".")
            print('The researcher \"' + self._nameList[int(newId)] + '\" was added to the research \"' + self._title + '\" by \"' + self._nameList[int(requester)] + "\" on the day " + str(currentDay) + ".")

    def removeMember(self, targetedId: str, requester: str, currentDay: int):
        if int(targetedId) in self._members:
            self._members.remove(int(targetedId))
            self._log.append('The researcher \"' + self._nameList[int(targetedId)] + '\" was removed by \"' + self._nameList[int(requester)] + "\" on the day " + str(currentDay) + ".")
            print('The researcher \"' + self._nameList[int(targetedId)]  + '\" was removed from the research \"' + self._title + '\" by \"' + self._nameList[int(requester)] + "\" on the day " + str(currentDay) + ".")

    def withdrawMoney(self, amount: int, requester: str, currentDay: int):
        if int(requester) not in self._members:
            return withDrawResponse.NOT_A_MEMBER.value
        if self._fund < 1:
            return withDrawResponse.EMPTY_FUND.value
        self._fund -= amount
        self._log.append('The researcher \"' + self._nameList[int(requester)] + '\" has withdraw ' + str(amount) + ', the fund is now of ' + str(self._fund) + ' on the day ' + str(currentDay) + '.')
        print('The researcher \"' + self._nameList[int(requester)] + '\" has  withdraw ' + str(amount) + ', from the research \"' + self._title + '\", the fund is now of ' + str(self._fund) + ' on the day ' + str(currentDay) + '.')
        return withDrawResponse.TAKE_THE_REST.value if self._fund <= 0 else withDrawResponse.NORMAL_WITHDRAW.value