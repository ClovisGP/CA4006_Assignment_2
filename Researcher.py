from ComEntity import ComEntity

class Researcher(ComEntity):
    def run(self) -> None:
        self.sendMsg('default', 'Hello Hello')