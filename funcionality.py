from navigation_system.interface import ModuleView, EventView, Service, Repository


class MyView(ModuleView):
    def __init__(self):
        super().__init__()


class MyEvent(EventView):
    def __init__(self, view: ModuleView, services: list[Service]) -> None:
        super().__init__(view, services)
    
    def _connect_events(self) -> None:
        print("Events connected")


class MyRepository(Repository):
    def __init__(self) -> None:
        super().__init__()


class MyService(Service):

    def __init__(self, *repositories: Repository) -> None:
        super().__init__(*repositories)
