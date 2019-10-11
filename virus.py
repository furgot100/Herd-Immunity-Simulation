class Virus(object):
    '''Properties and attributes of the virus used in Simulation.'''

    def __init__(self, name, repro_rate, mortality_rate):
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate


def test_virus_instantiation():
    '''Check to make sure that the virus instantiator is working.'''
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3

def test_black_death_instantiation():
    virus= Virus("Black Death", 1, 0.6)
    assert virus.name == "Black Death"
    assert virus.repro_rate == 1
    assert virus.mortality_rate == 0.6

def test_anthrax_instantiation():
    virus = Virus("Anthrax", 6.5, 0.2)
    assert virus.name == "Anthrax"
    assert virus.repro_rate == 6.5
    assert virus.mortality_rate == 0.2

