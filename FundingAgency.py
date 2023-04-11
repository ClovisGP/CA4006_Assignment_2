from ComEntity import ComEntity
from Config import Config

class FundingAgency(ComEntity):
    _basedAmount: int = 0
    _minFunding: int = 0
    _maxFunding: int = 0

    def __init__(self, id, basedAmount, minFunding, maxFunding):
        super().__init__(id)
        self._basedAmount = basedAmount
        self._minFunding = minFunding
        self._maxFunding = maxFunding

    def callback(self, ch, method, properties, body):
        print(str(body, encoding="utf-8"))
        arrayBody = str(body).strip('\'').split(';')
        if not arrayBody[3]:
            self.sendMsg(str('default'+'Rsvp'), Config.proposalRefused)
        amountAsked = int(arrayBody[3])
        if amountAsked >= self._minFunding and amountAsked <= self._maxFunding and self._basedAmount - amountAsked > 0:
            self.sendMsg(str('default'+'Rsvp'), Config.proposalApproved)
            self._basedAmount = self._basedAmount - amountAsked
        else:
            self.sendMsg(str('default'+'Rsvp'), Config.proposalRefused)
        

    def behaviour(self) -> None:
        self.receiveMsg()