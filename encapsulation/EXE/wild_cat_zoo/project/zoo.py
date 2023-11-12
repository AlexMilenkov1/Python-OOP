class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) >= self.__animal_capacity:
            return "Not enough space for animal"
        elif self.__budget < price:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) >= self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        summed_salaries = 0
        for worker in self.workers:
            summed_salaries += worker.salary
        if self.__budget >= summed_salaries:
            self.__budget -= summed_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        summed_money_for_taking_care = 0
        for animal in self.animals:
            summed_money_for_taking_care += animal.money_for_care
        if self.__budget >= summed_money_for_taking_care:
            self.__budget -= summed_money_for_taking_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = []
        tigers = []
        cheetahs = []
        result = [f"You have {len(self.animals)} animals"]
        for animal in self.animals:
            if animal.__class__.__name__ == 'Lion':
                lions.append(repr(animal))
            elif animal.__class__.__name__ == 'Tiger':
                tigers.append(repr(animal))
            elif animal.__class__.__name__ == 'Cheetah':
                cheetahs.append(repr(animal))
        result.append(f'----- {len(lions)} Lions:')
        result.extend(lions)
        result.append(f'----- {len(tigers)} Tigers:')
        result.extend(tigers)
        result.append(f'----- {len(cheetahs)} Cheetahs:')
        result.extend(cheetahs)

        return '\n'.join(result)

    def workers_status(self):
        keepers = []
        caretakers = []
        vets = []
        result = [f"You have {len(self.workers)} workers"]
        for worker in self.workers:
            if worker.__class__.__name__ == 'Keeper':
                keepers.append(repr(worker))
            elif worker.__class__.__name__ == 'Caretaker':
                caretakers.append(repr(worker))
            elif worker.__class__.__name__ == 'Vet':
                vets.append(repr(worker))
        result.append(f'----- {len(keepers)} Keepers:')
        result.extend(keepers)
        result.append(f'----- {len(caretakers)} Caretakers:')
        result.extend(caretakers)
        result.append(f'----- {len(vets)} Vets:')
        result.extend(vets)

        return '\n'.join(result)
