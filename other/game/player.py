class player:
    def __init__(self):
        self.player_name = ""
        self.player_level = 0
        self.player_cash = 0
        self.company_name = ""
        self.company_level = 0

    def init_player(self, name, level, companyName, companyLevel, cash):
        self.player_name = name
        self.player_level = int(level)
        self.company_name = companyName
        self.company_level = int(companyLevel)
        self.player_cash = int(cash)

    def get_player_name(self): return self.player_name
    def get_player_level(self): return str(self.player_level)
    def get_player_cash(self): return str(self.player_cash)
    def get_company_name(self): return self.company_name
    def get_company_level(self): return str(self.company_level)

    def set_name(self, name): self.player_name = name
    def set_level(self, level): self.player_level = int(level)
    def set_cash(self, cash): self.player_level = int(cash)
    def set_company_name(self, companyName): self.company_name = companyName
    def set_company_level(self, companyLevel): self.company_level = int(companyLevel)