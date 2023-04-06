from Researcher import Researcher
from FundingAgency import FundingAgency

import os

if __name__ == '__main__':
    try:
        receiver = FundingAgency(0, 1000000, 10000, 50000)
        sender = Researcher(0)

        sender.start()
        receiver.start()

        sender.join()
        receiver.join()
    except KeyboardInterrupt:
        os.exit()
    