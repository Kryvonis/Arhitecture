import pickle


class PickleSerializer:
    @staticmethod
    def load_matches(filename='matches.pickle'):
        """
        Load objects from file
        :param filename:
        :return:
        """
        with open(filename, 'rb') as f:
            matches = pickle.load(f)
            return matches

    @staticmethod
    def save_matches(matches, filename='matches.pickle'):
        """
        Save objects to file
        :param matches:
        :param filename:
        :return:
        """
        with open(filename, 'wb') as f:
            pickle.dump(matches, f)
