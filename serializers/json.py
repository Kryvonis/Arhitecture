import json

from model.Model import Model


class MatchEncoder(json.JSONEncoder):
    """
    Json encoder for Match object
    """

    def default(self, o):
        if isinstance(o, Model):
            return {"team1": o._team_one,
                    "team2": o._team_two,
                    "res1": o._res_one,
                    "res2": o._res_two,
                    "date": o._date
                    }
        return json.JSONEncoder


class JsonSerializer:
    @staticmethod
    def load_matches(filename='matches.json'):
        """
        Load objects from file
        :param filename:
        :return:
        """
        with open(filename, 'rt') as f:
            list_of_matches = json.load(f)
            matches = []
            for m in list_of_matches:
                matches.append(Model(m["team1"], m["team2"],
                                     m["res1"], m["res2"], m["date"]))
            return matches

    @staticmethod
    def save_matches(matches, filename='matches.json'):
        """
        Save objects to file
        :param matches:
        :param filename:
        :return:
        """
        with open(filename, 'wt') as f:
            json.dump(matches, f, cls=MatchEncoder, indent=4)
