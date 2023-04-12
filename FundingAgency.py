from ComEntity import ComEntity
from Config import ProposalResponse
from typing import List
import random

class FundingAgency(ComEntity):
    _basedAmount: int = 0
    _minFunding: int = 0
    _maxFunding: int = 0
    _idListUniversity: List[int]
    _idListResearcher: List[int]
    _days: int = 0

    def __init__(self, id, idListUniversity, idListResearcher, basedAmount, minFunding, maxFunding):
        super().__init__(id)
        self._basedAmount = basedAmount
        self._minFunding = minFunding
        self._maxFunding = maxFunding
        self._idListUniversity = idListUniversity
        self._idListResearcher = idListResearcher

    def proposalBehaviour(self, request):
        if not request[3]:
            self.sendMsg(request[0], str(self._id) + ';' + str(ProposalResponse.Refused.value))
        amountAsked = int(request[3])
        if amountAsked >= self._minFunding and amountAsked <= self._maxFunding and self._basedAmount - amountAsked > 0:
            self.sendMsg(request[0], str(self._id) + ';' + str(ProposalResponse.Approved.value))
            self.sendMsg(str(self._idListUniversity[0]), str(self._id) + ';' + request[0] + ';' + request[1] + ';' + request[3] + ';' + str(self._days + random.randrange(50, 365)))
            print("The university " + str(self._id) + "has approved the research " + request[1] + "of the research " + request[0] + "ont the day "+ str(self._days))
            self._basedAmount = self._basedAmount - amountAsked
        else:
            self.sendMsg(request[0], str(self._id) + ';' + str(ProposalResponse.Refused.value))

    def analyse(self, body):
        request = body.strip('\'').split(';')
        if int(request[0]) in self._idListResearcher:
            self.proposalBehaviour(request)
        elif int(request[0]) in self._idListUniversity:
            pass
        else:
            self._days = int(request[1])
        
        

    def behaviour(self) -> None:
        while (1):
            self.analyse(self.receiveResponse())