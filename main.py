from Researcher import Researcher
from FundingAgency import FundingAgency
from University import University
from typing import List
import os

if __name__ == '__main__':
    try:
        idListFundingAgency = [0]
        idListUniversity = [1]
        idListResearcher = [2]

        listResearcher: List[Researcher] = []
        for currentId in idListResearcher:
            listResearcher.append(Researcher(currentId, idListFundingAgency, idListUniversity))
        fundingAgency = FundingAgency(idListFundingAgency[0], idListUniversity, 100000, 10000, 50000)
        university = University(idListUniversity[0], idListFundingAgency, idListResearcher)

        university.start()
        fundingAgency.start()
        for researcher in listResearcher:
            researcher.start()

    except KeyboardInterrupt:
        os.exit()
    