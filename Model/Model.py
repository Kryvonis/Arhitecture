class Model:
    def __init__(self, team_one="", team_two="", res_one=0, res_two=0, date=""):
        self._team_one = team_one
        self._team_two = team_two
        self._res_one = res_one
        self._res_two = res_two
        self._date = date

    def __str__(self):
        return "{},{},{},{},{}".format(self._team_one, self._team_two, self._res_one, self._res_two, self._date)

    def __repr__(self):
        return "Game({},{},{},{},{})".format(self._team_one, self._team_two, self._res_one, self._res_two, self._date)

    def __eq__(self, other):
        if isinstance(other,Model):
            return self._team_one == other._team_one and \
                   self._team_two == other._team_two and \
                   self._res_one == other._res_one and \
                   self._res_two == other._res_two and \
                   self._date == other._date
        return False

    def __lt__(self, other):
        if isinstance(other,Model):
            return self._team_one < other._team_one and \
                   self._team_two < other._team_two and \
                   self._res_one < other._res_one and \
                   self._res_two < other._res_two and \
                   self._date < other._date
        return False

    def __hash__(self):
        return hash(self._date)
