from ComEntity import ComEntity
from Config import OperationOnResearch
from Config import withDrawResponse
from Config import createSubject
from Config import ProposalResponse
from typing import List
import time
import random

class Researcher(ComEntity):

    _isBusy = False
    _idListUniversity: List[int]
    _idListFundingAgency: List[int]
    _nameList: List[str] = []

    def __init__(self, id, nameList, idListFundingAgency, idListUniversity):
        super().__init__(id)
        self._idListUniversity = idListUniversity
        self._idListFundingAgency = idListFundingAgency
        self._nameList = nameList

    def makeResearchProposal(self):
        subject = createSubject()
        fund = str((10 ** random.randrange(4, 7)) * random.randrange(1, 8))
        requestMsg = str(self._id) + ';' + subject + ';It a research about the ' + subject + ';' + fund
        for idFA in self._idListFundingAgency:
            self.sendMsg(str(idFA), requestMsg)

            response = self.receiveResponse().strip('\'').split(';')
            if int(response[0]) in self._idListFundingAgency: # Probalility of bug here
                if int(response[1]) == ProposalResponse.Approved.value:
                    return True
        return False
    
    def workingOnResearch(self):
        operationChosen = OperationOnResearch.WITHDRAW_MONEY.value#random.choice(list(OperationOnResearch))
        requestMsg = str(self._id) + ';' + str(operationChosen) + ';' + str(random.randrange(100, 5001))
        self.sendMsg(str(self._idListUniversity[0]), requestMsg)

        response = self.receiveResponse().strip('\'').split(';')
        if int(response[0]) == self._idListUniversity[0]:
            if int(response[1]) == withDrawResponse.EMPTY_FUND.value or int(response[1]) == withDrawResponse.TAKE_THE_REST.value or int(response[1]) == withDrawResponse.NOT_A_MEMBER.value:
                print('The researcher \"' + self._nameList[self._id] + "\" is no longer working on one of his research")
                self._isBusy = False

    def behaviour(self):
        if self._isBusy == False:
            self._isBusy = self.makeResearchProposal()
        else:
            self.workingOnResearch()
        time.sleep(random.randrange(1, 7))