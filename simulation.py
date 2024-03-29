import random, sys
random.seed(42)
import math
from random import uniform
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    ''' Main class that will run the herd immunity simulation program.
    Expects initialization parameters passed as command line arguments when file is run.

    Simulates the spread of a virus through a given population.  The percentage of the
    population that are vaccinated, the size of the population, and the amount of initially
    infected people in a population are all variables that can be set when the program is run.
    '''
    def __init__(self, pop_size, vacc_percentage,virus, initial_infected=1):
        ''' Logger object logger records all events during the simulation.
        Population represents all Persons in the population.
        The next_person_id is the next available id for all created Persons,
        and should have a unique _id value.
        The vaccination percentage represents the total percentage of population
        vaccinated at the start of the simulation.
        You will need to keep track of the number of people currently infected with the disease.
        The total infected people is the running total that have been infected since the
        simulation began, including the currently infected people who died.
        You will also need to keep track of the number of people that have die as a result
        of the infection.

        All arguments will be passed as command-line arguments when the file is run.
        HINT: Look in the if __name__ == "__main__" function at the bottom.
        '''
        # Create a Logger object and bind it to self.logger.
        # Remember to call the appropriate logger method in the corresponding parts of the simulation.
        # Call self._create_population() and pass in the correct parameters.
        # Store the array that this method will return in the self.population attribute.
        # Store each newly infected person's ID in newly_infected attribute.
        # At the end of each time step, call self._infect_newly_infected()
        # and then reset .newly_infected back to an empty list.
        self.time_step_counter = 0
        self.pop_size = pop_size # Int
        self.next_person_id = 0 # Int
        self.initial_infected = 1 # Int
        self.virus = virus # Virus object
        self.vacc_percentage = vacc_percentage # float between 0 and 1
        self.total_infected = 0 # Int
        self.current_infected = 0 # Int
        self.new_deaths = 0
        self.total_dead = 0 # Int
        self.new_vaccinations = 0
        self.total_vaccinated = 0
        self.population = []# List of Person object
        self.logger = Logger('logs.txt')
        self.id = 0
        self.newly_infected = []
        # self.logger.write_metadata(self.pop_size, self.vacc_percentage,
        #                            self.virus.name, self.virus.mortality_rate,
        #                            self.virus.repro_rate)

    def _create_population(self, initial_infected):
        '''This method will create the initial population.
            Args:
                initial_infected (int): The number of infected people that the simulation
                will begin with.

            Returns:
                list: A list of Person objects.

        '''
        # This method should be called when the simulation
        # begins, to create the population that will be used. This method should return
        # an array filled with Person objects that matches the specifications of the
        # simulation (correct number of people in the population, correct percentage of
        # people vaccinated, correct number of initially infected people).

        create_pop = True
        while create_pop:
            virus = self.virus
            while len(self.population) <= initial_infected:
                self.id += 1
                infected_person = Person(self.id, False, virus, True)
                self.population.append(infected_person)
                # print(initial_infected)

            while len(self.population) <= self.pop_size:
                self.id += 1
                uninfected_person = Person(self.id, False, None, True)
                self.population.append(uninfected_person)
            # else:
            create_pop = False
        return self.population
    def _simulation_should_continue(self):
        ''' The simulation should only end if the entire population is dead
        or everyone is vaccinated.

            Returns:
                bool: True for simulation should continue, False if it should end.
        '''
<<<<<<< HEAD
        # TODO: Complete this helper method.  Returns a Boolean.
        if len(self.get_infected()) == 0:
=======

        if len(self.get_infected()) == 100:
>>>>>>> b58bf016e92fe0201a108e1fb49fd45e10f29358
            return False
        else:
            return True


    def get_infected(self):
        infected_list=[]

        self.current_infected = 0
        for person in self.population:
            if person.infection is not None and person.is_alive == True:
                infected_list.append(person)
                self.current_infected += 1
        return infected_list
        # print(infected_list)
    def run(self):
        ''' This method should run the simulation until all requirements for ending
        the simulation are met.
        '''
        

        #  Keep track of the number of time steps that have passed.
        log = self.logger
        log.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name, self.virus.mortality_rate, self.virus.repro_rate)
        self._create_population(self.initial_infected)
        should_continue = self._simulation_should_continue()
        # print(should_continue)
        while should_continue:
            # print(should_continue)
            self.time_step()
            self.time_step_counter +=1
            log.log_time_step(self.time_step_counter)
            should_continue = self._simulation_should_continue()

        print(f'The simulation has ended after {self.time_step_counter} turns.')

    def time_step(self):
        ''' This method should contain all the logic for computing one time step
        in the simulation.

        This includes:
            1. 100 total interactions with a randon person for each infected person
                in the population
            2. If the person is dead, grab another random person from the population.
                Since we don't interact with dead people, this does not count as an interaction.
            3. Otherwise call simulation.interaction(person, random_person) and
                increment interaction counter by 1.
            '''

        interactions = 0
        for person in self.population:
            # print(len(self.population))
            while interactions < 100:
                # print('a')
                # print(f'{person._id}: {interactions}')
                if person.is_alive == True and person.infection is not None:
                    random_person = random.choice(self.population)
                    if (random_person.is_alive == True):
                        self.interaction(person, random_person)
                        interactions += 1
                        print(interactions)
        self._infect_newly_infected()
        self.get_infected()


    def interaction(self, person, random_person):
        '''This method should be called any time two living people are selected for an
        interaction. It assumes that only living people are passed in as parameters.

        Args:
            person1 (person): The initial infected person
            random_person (person): The person that person1 interacts with.
        '''
        # Assert statements are included to make sure that only living people are passed
        # in as params
        assert person.is_alive == True
        assert random_person.is_alive == True

        
        #  The possible cases:
            # random_person is vaccinated:
            #     nothing happens to random person.
            # random_person is already infected:
            #     nothing happens to random person.
            # random_person is healthy, but unvaccinated:
            #     generate a random number between 0 and 1.  If that number is smaller
            #     than repro_rate, random_person's ID should be appended to
            #     Simulation object's newly_infected array, so that their .infected
            #     attribute can be changed to True at the end of the time step.

        if random_person.is_vaccinated:
            self.logger.log_interaction(person, random_person, False, True, False)
        elif random_person.infection is not None:
            self.logger.log_interaction(person, random_person, True, False, False)
        else:
            if random.uniform(0,1) < person.infection.repro_rate and random_person._id not in self.newly_infected:
                self.newly_infected.append(random_person)
                self.logger.log_interaction(person, random_person, False, False, True)
            else:
                self.logger.log_interaction(person, random_person, False, False, False)
        # draw = uniform(0,1)
        # person = person.infection
        # if (draw < person.repro_rate):
        #     self.newly_infected.append(random_person)

    def _infect_newly_infected(self):
        ''' This method should iterate through the list of ._id stored in self.newly_infected
        and update each Person object with the disease. '''

        for person in self.newly_infected:
            person.infection = self.virus
            self.total_infected +=1

if __name__ == "__main__":
    params = sys.argv[1:]
    virus_name = str(params[2])
    repro_num = float(params[4])
    mortality_rate = float(params[3])

    pop_size = int(params[0])

    vacc_percentage = float(params[1])

    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1

    virus = Virus(virus_name, repro_num, mortality_rate)
    sim = Simulation(pop_size, vacc_percentage, virus, initial_infected )
    # print(f"pop size: {pop_size} vacc percentage: {vacc_percentage} virus: {virus} initial infected: {initial_infected} ")

    sim.run()
