from ComEntity import ComEntity
from Config import Config

class Researcher(ComEntity):

    _isBusy = False

    def makeResearchProposal(self):
        requestMsg = str(self._id) + '; Research of ' + str(self._id) + ';It a research about the percentage of drunk person in Dublin after 14pm;' + str(10000)
        self.sendMsg('default', bytearray(requestMsg, 'UTF-8'))

        response = str(self.receiveResponse(str('default'+'Rsvp'))).strip('\'')
        print(response)
        if response == Config.proposalApproved:
            print('The proposal of the researcher ', self._id, " is approved by....")
            self._isBusy = True
        else:
            print('The proposal of the researcher ', self._id, " is refused by....")

    def behaviour(self):
        if not self._isBusy:
            self.makeResearchProposal()