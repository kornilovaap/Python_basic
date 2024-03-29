"""
Реализовать класс Road (дорога).

  + определить атрибуты: length (длина), width (ширина);
  - значения атрибутов должны передаваться при создании экземпляра класса;
  + атрибуты сделать защищёнными;
  - определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
  - использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
  - проверить работу метода.

Например: 20 м*5000 м*25 кг*5 см = 12500 т.

"""


class Road:
    _length: int
    _width: int

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def count_of_road(self, asphalt_mass=25, thickness=5):
        return f"{int(self._length * self._width * asphalt_mass * thickness / 1000)} т."


road_one = Road(20, 5000)
print(road_one.count_of_road())
__________________________________
12500 т.
           
