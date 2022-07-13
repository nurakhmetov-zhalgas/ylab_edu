from heroes import Superman, ChuckNorris, Pleakley
from places import Kostroma, Tokyo, SomePlanet
from save_the_place import SavePlace
from media import Newspaper


if __name__ == "__main__":
    SavePlace(Superman(), Kostroma(), Newspaper())
    print("-" * 20)
    SavePlace(ChuckNorris(), Tokyo(), Newspaper())
    print("-" * 20)
    SavePlace(Pleakley(), SomePlanet(), Newspaper())
