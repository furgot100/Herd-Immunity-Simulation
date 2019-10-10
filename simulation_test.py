from simulation import Simulation
from virus import Virus
from person import Person

def test_create_pop():
    anthrax = Virus("Anthrax", 6.5, 0.2)
    anthrax_sim = Simulation(100,20,40,anthrax)
    initial_infected = (anthrax.repro_rate * 100) - 1
    anthrax_sim._create_population(initial_infected)

def test_infection():
    anthrax = ("Anthrax", 6.5, 0.2)
    anthrax_sim = Simulation(100,20,40, anthrax)
    infected_person = Person(id,True,False,anthrax)
    uninfected = Person(id,True,False, None)
    anthrax_sim.interaction(infected_person,uninfected)


test_infection()




