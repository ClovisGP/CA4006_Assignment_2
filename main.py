from Researcher import Researcher
from FundingAgency import FundingAgency
from University import University
from TimeKeeper import TimeKeeper
from ComEntity import ComEntity
from typing import List
from Config import createName
from Config import TypeOfEntities
import os

def setUp(listThreads, nameList, idListFundingAgency, idListUniversity, idListResearcher):
    index: int = 0

    comp = 0
    while comp in range(1):
        nameList.append(createName(TypeOfEntities.FUNDING_AGENCY))
        listThreads.append(FundingAgency(index, nameList, idListUniversity, idListResearcher, 100000, 10000, 50000))
        idListFundingAgency.append(index)
        comp += 1
        index += 1
    comp = 0
    while comp in range(1):
        nameList.append(createName(TypeOfEntities.UNIVERSITY))
        listThreads.append(University(index, nameList, idListFundingAgency, idListResearcher))
        idListUniversity.append(index)
        comp += 1
        index += 1
    comp = 0
    while comp in range(3):
        nameList.append(createName(TypeOfEntities.RESEARCHER))
        listThreads.append(Researcher(index, nameList, idListFundingAgency, idListUniversity))
        idListResearcher.append(index)
        comp += 1
        index += 1
    listThreads.append(TimeKeeper(index, idListFundingAgency, idListUniversity))


if __name__ == '__main__':
    try:
        listThreads: List[ComEntity] = []
        nameList: List[str] = []
        idListFundingAgency = []
        idListUniversity = []
        idListResearcher = []

        setUp(listThreads,nameList, idListFundingAgency, idListUniversity, idListResearcher)
        for thread in listThreads:
            thread.setUp()
            thread.start()

    except KeyboardInterrupt:
        os.exit()
    