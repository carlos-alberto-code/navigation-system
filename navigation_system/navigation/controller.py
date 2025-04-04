from navigation_system.interface import ModuleView, EventView, Service, Repository


class Controller:

    def __init__(
        self,
        view_class: type[ModuleView],
        event_class: type[EventView],
        service_classes: dict[type[Service], list[type[Repository]]]
    ) -> None:
        self._view_class = view_class
        self._event_class = event_class
        self._services_class = service_classes
    
    def build(self) -> ModuleView:
        view = self._view_class()
        services = [
            service_class(
                *[
                    repository_class()
                    for repository_class in repositories
                ]
            ) for service_class, repositories in self._services_class.items()
        ]
        return self._event_class(view, services).view