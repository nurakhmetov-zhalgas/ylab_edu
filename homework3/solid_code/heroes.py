from abc import ABC, abstractmethod
from weapons import Laser, Gun, Karate


class AbstractHero(ABC):
    @property
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def attack(self):
        pass


class AbstractSuperhero(AbstractHero):
    @abstractmethod
    def ultimate(self):
        pass


class Superman(AbstractSuperhero, Laser, Karate):
    name = "Clark Kent"

    def attack(self):
        self.roundhouse_kick()
        self.ultimate()

    def ultimate(self):
        self.incinerate_with_lasers()


class ChuckNorris(AbstractHero, Karate, Gun):
    name = "Chuck Norris"

    def attack(self):
        self.roundhouse_kick()
        self.fire_a_gun()


class Pleakley(AbstractSuperhero, Laser, Karate, Gun):
    name = "Pleakley"

    def attack(self):
        self.roundhouse_kick()
        self.fire_a_gun()
        self.ultimate()

    def ultimate(self):
        return self.incinerate_with_lasers()
