from enum import Enum
import random

class Config:
    dayDuration = 1

"""
# Protocols of requests #

## Request of a researcher to a fundingAgency for a research proposal
request => id;subject;description;fund
    id          - id of the researcher
    subject     - is the title of the research
    description - is the description of the research
    fund        - is the asked fund to this research

## Response of a fundingAgency to a researcher for a research proposal
request => id;result
    id          - id of the fundingAgency
    result      - is a ProposalResponse

## Request of the fundingAgency to the University for the creation of a research Account
request => id;idMember;subject;fund;deadLine
    id          - id of the fundingAgency
    idMember    - is the id of the researcher who has make the proposal
    subject     - is the title of the research
    fund        - is the asked fund to this research
    deadLine    - is the day when the research is finished

## Request from a researcher to a University
request => id;operation;argument;title
    id          - id of the researcher
    operation   - is a OperationOnResearch
    argument    - can be a amount of fund to withdraw or a id or empty
    title       - is the title of the research, can be empty

## Response of a University to a researcher for a requested operation
request => id;result
    id          - id of the University
    result      - is a withDrawResponse

## TimeKeeper to University or to FundingAgency 
Request => id;days
    id          - id of the TimeKeeper
    days        - days number

"""

class ProposalResponse(Enum):
    Approved = 0
    Refused = 1

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

class TypeOfEntities(Enum):
    RESEARCHER = 0
    UNIVERSITY = 1
    FUNDING_AGENCY = 2


""" Name générations """

universityName = [
        "Manatees University",
        "Hello my World",
        "Wait we are an University",
        "Dublin City University",
        "Centre Henry Muler",
    ]
fundingAgencyName = [
        "Silicon Voulou Agency", # It the silicon valley agency but in Wish version 
        "We love Science",
        "Glados Agency",
        "SCIENCE",
        "A DRAGON, RUN agency",
    ]

ResearcherFirstName = [
        "Martin",
        "Clovis",
        "This guy",
        "The horse",
        "The oster",
        "The man",
        "The woman",
        "The truck",
        "Tom",
        "The manatee",
    ]

ResearcherSecondName = [
        " who is stuck in the washing-machine",
        " Nook",
        " who is ugly",
        " who stinks",
        " who seems like an oster",
        " who seems dead",
        " who seems human",
        " who is stuck in the door",
        " Mice",
        " who is very shy",
    ]
def createName(Type: TypeOfEntities) -> str:
    if Type == TypeOfEntities.RESEARCHER:
        return ResearcherFirstName[random.randrange(0, 9)] + ResearcherSecondName[random.randrange(0, 9)]
    elif Type == TypeOfEntities.UNIVERSITY:
        return universityName[random.randrange(0, 4)]
    elif Type == TypeOfEntities.FUNDING_AGENCY:
        return fundingAgencyName[random.randrange(0, 4)]


firstPart = [
        "Number of Drunk Irish",
        "Number of French revolutions",
        "Number of muffins eaten by Martin",
        "Number of bailey's bottles drank by Gaelle",
        "Number of rhum's bottles drank by Clovis",
        "Percentage of Londis's spice box's paid",
        "Percentage of students who know the C language",
        "Percentage of DCU Hampstead rooms happy residents",
        "Percentage days where Clovis had hot water",
        "Percentage of \'I haven't slept enough.\'",
        "Percentage of \'I am hungry.\'",
        "Percentage people who say \'Hello\'",
        "Percentage people who say \'Pain au chocolat\'",
        "Number of happy osters",
        "Number of Cactus throw by Clovis at his roommates when they did not clean the kitchen"
    ]
secondPart = [
        " in 1969",
        " in the twenty-first century",
        " on the 5 May 1789",
        " in Dublin",
        " in Europe",
        " in the CA4006 module",
        " in the population of manatees",
        " during the Great Depression",
        " during the great war",
        " during the good mornings in Vietnam",
        " in the populations of DCU students",
        " in 2023",
        " during my birthday. It is the 18th april",
        " in \'yeah, I\'m tired\' moments",
        " during the cycle of reproduction of a fly"
    ]

def createSubject() -> str:
    return firstPart[random.randrange(0, 14)] + secondPart[random.randrange(0, 14)]

    
    

    




"""
Do you know the story of an optimistic guy?
As he fell from an huge building, he said on each floor "Jusqu'ici, tout va bien" (translation: "so far all is well") while laughing.
Clovis GILLES 2023
"""