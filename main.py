from Researcher import Researcher
from FundingAgency import FundingAgency
from University import University
from typing import List
import os

if __name__ == '__main__':
    try:
        idListFundingAgency = [0]
        idListUniversity = [1]
        idListResearcher = [2, 3, 4, 5]
        sender = Researcher(idListResearcher[0], idListFundingAgency, idListUniversity)
        sender2 = Researcher(idListResearcher[1], idListFundingAgency, idListUniversity)
        sender3 = Researcher(idListResearcher[2], idListFundingAgency, idListUniversity)
        sender4 = Researcher(idListResearcher[3], idListFundingAgency, idListUniversity)
        fundingAgency = FundingAgency(idListFundingAgency[0], idListUniversity, 100000, 10000, 50000)
        university = University(idListUniversity[0], idListFundingAgency)

        sender.start()
        sender2.start()
        sender3.start()
        sender4.start()
        fundingAgency.start()
        university.start()

    except KeyboardInterrupt:
        os.exit()
    