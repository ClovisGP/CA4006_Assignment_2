from enum import Enum

class Config:
    proposalApproved = "Approved"
    proposalRefused = "Refused"


"""Request from a researcher to a University"""

"""id of the researcher;operation;argument which is optional;title which is optional"""

class OperationOnResearch(Enum):
    WITHDRAW_MONEY = 0
    ADD_MEMBER = 1
    REMOVE_MEMBER = 2
    CANCEL_RESEARCH = 3


class withDrawResponse(Enum):
    NOT_A_MEMBER = 0
    TAKE_THE_REST = 1
    NORMAL_WITHDRAW = 2
    EMPTY_FUND = 3