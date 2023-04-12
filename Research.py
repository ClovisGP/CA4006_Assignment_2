from typing import List
from Config import withDrawResponse

class Research:
    _members: List[int]
    _fund: int
    _deadLine: int
    _title: str
    _log : List[str] = []

    def __init__(self, memberList, money, deadLine, title, idAsker):
        self._members = memberList
        self._fund = money
        self._deadLine = deadLine
        self._title = title
        self._log.append('Created by ' + str(idAsker))
    
    def addMember(self, newId: str, requester: str):
        if int(newId) not in self._members:
            self._members.append(int(newId))
            self._log.append('The researcher ' + newId + ' was added by ' + requester)
            print('The researcher ' + newId + ' was added to the research ' + self._title + ' by ' + requester)

    def removeMember(self, targetedId: str, requester: str):
        if int(targetedId) in self._members:
            self._members.remove(int(targetedId))
            self._log.append('The researcher ' + targetedId + ' was removed by ' + requester)
            print('The researcher ' + targetedId + ' was removed from the research ' + self._title + ' by ' + requester)

    def withdrawMoney(self, amount: int, requester: str):
        if int(requester) not in self._members:
            return withDrawResponse.NOT_A_MEMBER.value
        if self._fund < 1:
            return withDrawResponse.EMPTY_FUND.value
        self._fund -= amount
        self._log.append('The researcher ' + requester + ' has  withdraw ' + str(amount) + 'the fund is now of ' + str(self._fund))
        print('The researcher ' + requester + ' has  withdraw ' + str(amount) + ' from the research ' + self._title + ' the fund is now of ' + str(self._fund))
        return withDrawResponse.TAKE_THE_REST.value if self._fund <= 0 else withDrawResponse.NORMAL_WITHDRAW.value