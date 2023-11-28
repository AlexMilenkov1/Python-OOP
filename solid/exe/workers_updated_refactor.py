from abc import ABC, abstractmethod
import time


class Eating(ABC):
    @staticmethod
    @abstractmethod
    def eat():
        pass


class Working(ABC):
    @staticmethod
    @abstractmethod
    def work():
        pass


class Worker(Eating, Working):

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(Eating, Working):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, Working), "`worker` must be of type {}".format(Working)

        self.worker = worker

    def manage(self):
        self.worker.work()

    def lunch_break(self):
        self.worker.eat()


class Robot(Working):

    def work(self):
        print("I'm a robot. I'm working....")


work_manager = Manager()

break_manager = Manager()

work_manager.set_worker(Worker())

break_manager.set_worker(Worker())

work_manager.manage()

break_manager.lunch_break()

work_manager.set_worker(SuperWorker())

break_manager.set_worker(SuperWorker())

work_manager.manage()

break_manager.lunch_break()

work_manager.set_worker(Robot())

work_manager.manage()

try:
    break_manager.set_worker(Robot())
    break_manager.lunch_break()

except:
    pass
