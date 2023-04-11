from ComEntity import ComEntity
from Config import Config
from Config import OperationOnResearch
from Config import withDrawResponse
from typing import List
import time
import random

class Researcher(ComEntity):

    _isBusy = False
    _idListUniversity: List[int]
    _idListFundingAgency: List[int]

    def __init__(self, id, idListFundingAgency, idListUniversity):
        super().__init__(id)
        self._idListUniversity = idListUniversity
        self._idListFundingAgency = idListFundingAgency

    def makeResearchProposal(self):
        requestMsg = str(self._id) + ';Research of ' + str(self._id) + ';It a research about the percentage of drunk person in Dublin after 14pm;' + str(10000)
        self.sendMsg(str(self._idListFundingAgency[0]), requestMsg)

        response = self.receiveResponse().strip('\'').split(';')
        if int(response[0]) == self._idListFundingAgency[0]:
            if response[1] == Config.proposalApproved:
                print('The proposal of the researcher ', self._id, " is approved by " + response[0])
                self._isBusy = True
            else:
                print('The proposal of the researcher ', self._id, " is refused by " + response[0])
    
    def workingOnResearch(self):
        operationChosen = OperationOnResearch.WITHDRAW_MONEY.value#random.choice(list(OperationOnResearch))
        requestMsg = str(self._id) + ';' + str(operationChosen) + ';' + str(random.randrange(1000, 10000))
        self.sendMsg(str(self._idListUniversity[0]), requestMsg)

        response = self.receiveResponse().strip('\'').split(';')
        if int(response[0]) == self._idListUniversity[0]:
            if int(response[1]) == withDrawResponse.EMPTY_FUND.value or int(response[1]) == withDrawResponse.TAKE_THE_REST.value or int(response[1]) == withDrawResponse.NOT_A_MEMBER.value:
                print('The researcher ', self._id, " is no longer working on one of his research")
                self._isBusy = False

    def behaviour(self):
        while (1):
            if self._isBusy == False:
                self.makeResearchProposal()
            else:
                self.workingOnResearch()
            time.sleep(1)