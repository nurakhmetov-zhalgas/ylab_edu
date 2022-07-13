from heroes import AbstractHero
from places import AbstractPlace
from media import AbstractMedia


class SavePlace:
    def __init__(self, hero: AbstractHero, place: AbstractPlace, media: AbstractMedia):
        self.place = place
        self.hero = hero
        self.media = media

        self.find_antagonist()
        self.hero.attack()
        self.notify()

    def find_antagonist(self) -> None:
        self.place.get_antogonist()

    def notify(self) -> None:
        self.media.notify(f"{self.hero.name} saved the {self.place.name}")
