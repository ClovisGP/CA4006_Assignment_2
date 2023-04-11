from ComEntity import ComEntity
from Config import Config
from typing import List

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
        if response[1] == Config.proposalApproved:
            print('The proposal of the researcher ', self._id, " is approved by " + response[0])
            self._isBusy = True
        else:
            print('The proposal of the researcher ', self._id, " is refused by " + response[0])

    def behaviour(self):
        if not self._isBusy:
            self.makeResearchProposal()