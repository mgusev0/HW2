


class Path:
    # атрибут класса, хранящий в себе список координат, то есть путь машины
    def __init__(self, tunnels: list[tuple[float, float, float]]):
        self.tunnels = tunnels

    # метод класса, возвращающий путь машины
    def get_path_coordinates(self):
        return self.tunnels


class Support:
    # атрибуты класса крепи
    def __init__(self, support_type, wear_percentage):
        self.type = support_type  # тип крепи: трапецеидальная или арочная
        self.wear_percentage = wear_percentage  # процент износа
    # метод класса, возвращающий процент износа крепи
    def get_wear_percentage(self):
        return self.wear_percentage


class Machine:
    def __init__(self):
        self.is_on_path = False  # атрибут, показывающий на пути ли машина; по умолчанию False
        self.current_path = None  # атрибут, хранящий текущий путь
        self.coordinates = (0.0, 0.0, 0.0)  # атрибут, хранящий координаты машины

    # метод, позволяющий контролёру направлять машину на путь
    def move_to_path(self, path: Path):
        self.is_on_path = True
        self.current_path = path
        print("Машина отправлена на путь.")

    # метод, позволяющий контролёру отправлять машину на парковку
    def move_to_parking(self):
        self.is_on_path = False
        self.current_path = None
        self.coordinates = (0.0, 0.0, 0.0)
        print("Машина отправлена на парковку.")

    # метод, позволяющий контролёру узнавать координаты машины
    def get_current_coordinates(self):
        return self.coordinates


    # этот класс наследуется от абстрактного класса Machine
class DrillingMachine(Machine):
    def drill(self):
        # метод, позволяющий узнать, где находится буровая установка
        if self.is_on_path:
            print("Буровая установка начала бурение.")
        else:
            print("Буровая установка не находится на пути.")


    # этот класс наследуется от абстрактного класса Machine
class MappingMachine(Machine):
    # метод, позволяющий узнать, где находится машина для картографии
    def map_path(self):
        if self.is_on_path:
            print("Машина для картографии начала съемку картограммы.")
        else:
            print("Машина для картографии не находится на пути.")


    # этот класс наследуется от абстрактного класса Machine
class InspectionMachine(Machine):
    # метод, позволяющий узнать, где находится машина для осмотра крепей
    def inspect_support(self, support: Support):
        if self.is_on_path:
            print(f"Машина для осмотра крепей проверяет крепь типа {support.type}.")
            print(f"Процент износа: {support.get_wear_percentage()}%.")
        else:
            print("Машина для осмотра крепей не находится на пути.")


class MineController:
    # атрибут класса, хранящий в себе список всех машин
    def __init__(self):
        self.machines = []
    # метод, позволяющий контролёру добавить новую машину в список
    def add_machine(self, machine: Machine):
        self.machines.append(machine)
    # метод, позволяющий отправить машину на путь
    def send_to_path(self, machine: Machine, path: Path):
        machine.move_to_path(path)
        print(f"Машина отправлена на путь: {path.get_path_coordinates()}.")
    # метод позволяющий отправить машину на парковку
    def send_to_parking(self, machine: Machine):
        machine.move_to_parking()
        print("Машина отправлена на парковку.")

