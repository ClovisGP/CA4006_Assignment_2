from ComEntity import ComEntity
from Research import Research
from ResearcherAccount import ResearcherAccount
from Config import OperationOnResearch
from Config import withDrawResponse
from typing import List

class University(ComEntity):
	_idListFundingAgency: List[int]
	_listAccount: List[ResearcherAccount] = []
	_researchsInProgress: List[int] = []

	def __init__(self, id, idListFundingAgency, idListResearcher):
		super().__init__(id)
		self._idListFundingAgency = idListFundingAgency
		for currentId in idListResearcher:
			self._listAccount.append(ResearcherAccount(currentId))

	def findAccount(self, idResearched: int):
		for currentId in self._listAccount:
			if currentId._idLink == idResearched:
				return currentId
		return None

	def deleteResearch(self, researchTargeted: Research):
		print("The research => " + researchTargeted._title + " is finished")
		members = researchTargeted._members.copy()
		for memberId in members:
			self.findAccount(memberId).removeResearch(researchTargeted)
		self._researchsInProgress.remove(researchTargeted)
		del researchTargeted
  
	def researchCreation(self, request):
		tmp = Research([int(request[1])],int(request[3]), request[4], request[2], request[0])
		self._researchsInProgress.append(tmp)
		self.findAccount(int(request[1])).addResearch(tmp)
		print('The university ' + str(self._id) + ' has register a new research asking by ' + request[0])

	def researcherRequestManagement(self, request, account):
		print(request)
		research = account.getOneResearch() # I wanted to make a beautiful ternary but python don't like me
		if len(request) > 3:
			research = account.getOneResearch(request[3])
		if research == None:
			self.sendMsg(request[0], str(self._id) + ';' + str(withDrawResponse.NOT_A_MEMBER.value))# It is the same behaviour
			return None
		operationRequested = int(request[1])
		if operationRequested == OperationOnResearch.WITHDRAW_MONEY.value:
			result = research.withdrawMoney(int(request[2]), request[0])
			self.sendMsg(request[0], str(self._id) + ';' + str(result))
			if result == withDrawResponse.EMPTY_FUND.value or result == withDrawResponse.TAKE_THE_REST.value:
				self.deleteResearch(research)
		elif operationRequested == OperationOnResearch.ADD_MEMBER.value:
			research.addMember(int(request[2]), request[0])
			self.findAccount(int(request[2])).addResearch(research)
		elif operationRequested == OperationOnResearch.REMOVE_MEMBER.value:
			research.removeMember(int(request[2]), request[0])
			self.findAccount(int(request[2])).removeResearch(research)
		elif operationRequested == OperationOnResearch.CANCEL_RESEARCH.value:
			self.deleteResearch(research)

	def response(self, body):
		request = body.strip('\'').split(';')
		idRequest = int(request[0])
		if idRequest in self._idListFundingAgency:
			self.researchCreation(request)
		else:
			account = self.findAccount(idRequest)
			if account == None: # Not a researcher
				return None
			self.researcherRequestManagement(request, account)
    
	def behaviour(self) -> None:
		while (1):
			self.response(self.receiveResponse())