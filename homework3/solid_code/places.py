from abc import ABC, abstractmethod


class AbstractPlace(ABC):
    @abstractmethod
    def get_antogonist(self) -> str:
        pass

    @property
    def name(self):
        raise NotImplementedError


class Kostroma(AbstractPlace):
    name: str = "Kostroma"

    def get_antogonist(self) -> None:
        print("Orcs hid in the forest")


class Tokyo(AbstractPlace):
    name: str = "Tokyo"

    def get_antogonist(self) -> None:
        print("Godzilla stands near a skyscraper")


class SomePlanet(AbstractPlace):
    coordinates: list[float] = [12.5, 18.36]

    @property
    def name(self) -> str:
        return " ".join(map(str, self.coordinates))

    def get_antogonist(self):
        return "Monster from other planet are coming!"
