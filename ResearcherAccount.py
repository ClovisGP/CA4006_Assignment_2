from typing import List
from Research import Research

class ResearcherAccount:
    _idLink: int
    _listResearchs: List[Research] = []

    def __init__(self, idLink):
        self._idLink = idLink

    def addResearch(self, newResearchTitle: Research):
        self._listResearchs.append(newResearchTitle)
    
    def removeResearch(self, researchTitle: Research):
        self._listResearchs.remove(researchTitle)
    
    def getOneResearch(self, titleTargeted = '') -> Research:
        if len(self._listResearchs) == 0:
            return None
        if titleTargeted is '':
            return self._listResearchs[0]
        for current in self._listResearchs:
            if current._title == titleTargeted:
                return current
        return None
