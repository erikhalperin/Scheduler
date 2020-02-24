import itertools


class Subject:
    __id_generator = itertools.count(0, 1)

    @staticmethod
    def get_all_subjects():
        return ['Eng1', 'Eng2', 'Eng3', 'Eng4', 'Alg1', 'Alg2', 'Geo', 'PreC',
                'Phys', 'Chem', 'SciE', 'Bio', 'Civ1', 'Civ2', 'Civ3', 'Civ4']

    def __init__(self, name: str):
        self.name = name
        self.id = next(self.__id_generator)
