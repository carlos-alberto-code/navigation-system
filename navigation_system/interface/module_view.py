from abc import ABC
from flet import Container


class ModuleView(Container, ABC):
    """
    Base para todas las vistas modulares. Todas la clases que representarán una vista completa (una pantalla) deben heredar de esta clase.
    """
    pass
