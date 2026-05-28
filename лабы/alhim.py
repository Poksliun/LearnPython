recipes = {
    ("Вода", "Огонь"): "Пар",
    ("Вода", "Земля"): "Грязь",
    ("Воздух", "Вода"): "Грязь",
}
class Element:
    def __init__(self, name: str):
        self.name = name
    def __add__(self, other: "Element") -> "Element":
        pair = tuple(sorted([self.name, other.name]))
        result_name = recipes.get(pair)

        return Element(result_name) if result_name else None
    def __repr__(self):
        return f"Element({self.name!r})"

class Water(Element):
    def __init__(self, name: str):
        super().__init__(name)


class Fire(Element):
    def __init__(self, name: str):
        super().__init__(name)

class Steam(Element):
    components = (Water, Fire)
    def __init__(self, name: str):
        super().__init__(name)

steam = Steam.components
water = Element("Вода")
fire = Element("Огонь")
earth = Element("Земля")

result = water + fire
#result2 = game.combine(earth, water)
#result3 = game.combine(fire, water)
print(result, steam)