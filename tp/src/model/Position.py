class Position:

    def __init__(self, positionNS: int, positionOE: int):
        assert positionNS >= 0, "la position Nord-Sud doit être positive"
        self.positionNS = positionNS
        assert positionOE >= 0, "la position Ouest-Est doit être positive"
        self.positionOE = positionOE

