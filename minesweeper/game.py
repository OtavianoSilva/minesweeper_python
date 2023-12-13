class Game:
    def __init__(self, time:object, dificulty:str, user: object, win: bool) -> None:
        self.time = time
        self.dificulty = dificulty
        self.user = user
        self.win = win