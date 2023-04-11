from ComEntity import ComEntity
from Config import Config
from typing import List

class FundingAgency(ComEntity):
    _basedAmount: int = 0
    _minFunding: int = 0
    _maxFunding: int = 0
    _idListUniversity: List[int]

    def __init__(self, id, idListUniversity, basedAmount, minFunding, maxFunding):
        super().__init__(id)
        self._basedAmount = basedAmount
        self._minFunding = minFunding
        self._maxFunding = maxFunding
        self._idListUniversity = idListUniversity

    def analyse(self, body):
        arrayBody = body.strip('\'').split(';')
        if not arrayBody[3]:
            self.sendMsg(arrayBody[0], str(self._id) + ';' + Config.proposalRefused)
        amountAsked = int(arrayBody[3])
        if amountAsked >= self._minFunding and amountAsked <= self._maxFunding and self._basedAmount - amountAsked > 0:
            self.sendMsg(arrayBody[0], str(self._id) + ';' + Config.proposalApproved)
            self.sendMsg(str(self._idListUniversity[0]), str(self._id) + ';' + arrayBody[0] + ';' + arrayBody[1] + ';' + arrayBody[3] + ';' + "None")
            self._basedAmount = self._basedAmount - amountAsked
        else:
            self.sendMsg(arrayBody[0], str(self._id) + ';' + Config.proposalRefused)
        

    def behaviour(self) -> None:
        while (1):
            self.analyse(self.receiveResponse())