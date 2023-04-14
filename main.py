from Researcher import Researcher
from FundingAgency import FundingAgency
from University import University
from TimeKeeper import TimeKeeper
from ComEntity import ComEntity
from typing import List
from Config import createName
from Config import TypeOfEntities
import random

def setUp(listThreads, nameList, idListFundingAgency, idListUniversity, idListResearcher):
    index: int = 0

    for comp in range(2):
        nameList.append(createName(TypeOfEntities.FUNDING_AGENCY))
        tmpFund = 10 ** random.randrange(6, 10)
        listThreads.append(FundingAgency(index, nameList, idListUniversity, idListResearcher, tmpFund, int(tmpFund * (0.01 * random.randrange(1, 3))), int(tmpFund * (0.01 * random.randrange(25, 40)))))
        idListFundingAgency.append(index)
        index += 1

    for comp in range(1):
        nameList.append(createName(TypeOfEntities.UNIVERSITY))
        listThreads.append(University(index, nameList, idListFundingAgency, idListResearcher))
        idListUniversity.append(index)
        index += 1

    for comp in range(3):
        nameList.append(createName(TypeOfEntities.RESEARCHER))
        listThreads.append(Researcher(index, nameList, idListFundingAgency, idListUniversity))
        idListResearcher.append(index)
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
        exit(0)
    