from abc import ABCMeta, abstractmethod

class Musician():
    def __init__(self, name, instrument):
        __metaclass__ = ABCMeta
        self.name = name
        self.instrument = instrument
        # self.created_instances.append(self)

    @abstractmethod
    def __str__(self):
        pass

    def __repr__(self):
        return "{} instance".format(self.__class__.__name__)

    def get_instrument(self):
        return self.instrument
    
    @abstractmethod
    def play_solo(self):
        pass

class Guitarist(Musician):
    def __init__(self, name, solo="playing Europe"):
        Musician.__init__(self, name, "guitar")
        # super(Musician, self).__init__(name, "guitar")
        self.solo = solo

    def __str__(self):
        return "I'm a guitarist"
    
    def play_solo(self):
        return self.solo

class Bassist(Musician):
    def __init__(self, name, solo="playing My Generation"):
        Musician.__init__(self, name, "bass")
        self.solo = solo

    def __str__(self):
        return "I'm a bassist"
    
    def play_solo(self):
        return self.solo

class Drummer(Musician):
    def __init__(self, name, solo="playing Rush"):
        Musician.__init__(self, name, "drum")
        self.solo = solo

    def __str__(self):
        return "I'm a drummer"

    def play_solo(self):
        return self.solo

class Band():

    created_instances = []

    def __init__(self, name, members):
        if type(name) is not str:
            raise TypeError("name attribute must be a str")
        if type(members) is not list or len(members) == 0:
            raise TypeError("members attribute must be a list with at least one element")
        for member in members:
            if not isinstance(member, Musician):
                raise TypeError("members attribute must be a list of Musicians")
        self.name = name
        self.members = members
        Band.created_instances.append(self)

    def __str__(self):
        return "The {} band with members: ".format(self.name) + ', '.join([member.name for member in self.members])

    def __repr__(self):
        return "{} instance".format(self.__class__.__name__)
    
    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
        return solos

    @classmethod
    def to_list(cls):
        return cls.created_instances



    



    

        