class Logger(object):
    ''' Utility class responsible for logging all interactions during the simulation. '''

    def __init__(self, file_name):
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        '''
        The simulation class should use this method immediately to log the specific
        parameters of the simulation as the first line of the file.
        '''

        # TIP: Use 'w' mode when you open the file. For all other methods, use
        # the 'a' mode to append a new log to the end, since 'w' overwrites the file.
        file = open(self.file_name, "w")
        file.write(f"Population size: {pop_size}\tVaccination percentage: {vacc_percentage}\t"
                f"Virus name: {virus_name}\tMortality rate: {mortality_rate}\t"
                f"Basic reproduction number: {basic_repro_num}\n")
        # file.close()


    def log_interaction(self, person, random_person, random_person_sick=None,
                        random_person_vacc=None, did_infect=None):
        '''
        The Simulation object should use this method to log every interaction
        a sick person has during each time step.

        The format of the log should be: "{person.ID} infects {random_person.ID} \n"

        or the other edge cases:
            "{person.ID} didn't infect {random_person.ID} because {'vaccinated' or 'already sick'} \n"
        '''
        # Use the values passed along with each person,
        # along with whether they are sick or vaccinated when they interact to determine
        # exactly what happened in the interaction and create a String, and write to your logfile.
        file = open(self.file_name, 'a')
        if did_infect:
            file.write(f'Person {person._id} infects person {random_person._id}\n')
        elif random_person_vacc:
            file.write(f'Person {person._id} does not infect person {random_person._id} because they are vaccinate \n')
        elif random_person_sick:
            file.write(f'Person {person._id} does not infect {random_person._id} Because they are already infected \n')
        else:
            file.write(f'Person {person._id} does not infect person {random_person._id} \n')
        # file.close()

    def log_infection_survival(self, person, did_die_from_infection):
        ''' The Simulation object uses this method to log the results of every
        call of a Person object's .resolve_infection() method.

        The format of the log should be:
            "{person.ID} died from infection\n" or "{person.ID} survived infection.\n"
        '''
        # If the person survives, did_die_from_infection
        # should be False.  Otherwise, did_die_from_infection should be True.
        # Append the results of the infection to the logfile
        file = open(self.file_name, 'a')
        if did_die_from_infection:
            file.write(f"{person._id} died from infection\n")
        else:
            file.write(f"{person._id} survived the infection.\n")
        # file.close()

    def log_time_step(self, time_step_number):
        ''' STRETCH CHALLENGE DETAILS:

        If you choose to extend this method, the format of the summary statistics logged
        are up to you.

        At minimum, it should contain:
            The number of people that were infected during this specific time step.
            The number of people that died on this specific time step.
            The total number of people infected in the population, including the newly infected
            The total number of dead, including those that died during this time step.

        The format of this log should be:
            "Time step {time_step_number} ended, beginning {time_step_number + 1}\n"
        '''
        # TODO: Finish this method. This method should log when a time step ends, and a
        # new one begins.
        # NOTE: Here is an opportunity for a stretch challenge!
