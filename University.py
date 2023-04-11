from ComEntity import ComEntity
from Research import Research
from typing import List

class University(ComEntity):
  _idListFundingAgency: List[int]
  _researchsInProgress: List[int] = []

  def __init__(self, id, idListFundingAgency):
    super().__init__(id)
    self._idListFundingAgency = idListFundingAgency

  def response(self, body):
    request = body.strip('\'').split(';')
    if int(request[0]) in self._idListFundingAgency:
      self._researchsInProgress.append(Research([int(request[1])],int(request[3]), request[4], request[2], request[0]))
      print('The university ', str(self._id), ' has register a new research')
          
  def behaviour(self) -> None:
      while (1):
          self.response(self.receiveResponse())