from ComEntity import ComEntity

class FundingAgency(ComEntity):
    _basedAmount = 0
    _minFunding = 0
    _maxFunding = 0

    def __init__(self, id, basedAmount, minFunding, maxFunding):
        super().__init__(id)
        self._basedAmount = basedAmount
        self._minFunding = minFunding
        self._maxFunding = maxFunding

    def callback(self, ch, method, properties, body):
        print("It the received body => ", body)

    def run(self, queueName = 'default') -> None:
        self.receiveMsg(queueName)