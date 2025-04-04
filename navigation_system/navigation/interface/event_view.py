from abc import ABC, abstractmethod

from navigation_system.navigation.interface.service import Service
from navigation_system.navigation.interface.module_view import ModuleView


class EventView(ABC):

    @abstractmethod
    def __init__(self, view: ModuleView, services: list[Service]) -> None:
        self._view = view
        self._services = services
        self._connect_events()

    @property
    def view(self) -> ModuleView:
        """
        Devuelve la vista con sus eventos ya conectados. Los eventos hacen uso de servicios para suministrar datos para las acciones demandadas.
        """
        return self._view

    @abstractmethod
    def _connect_events(self) -> None:
        """
        Conecta los eventos de la vista con los servicios.
        """
        pass
    