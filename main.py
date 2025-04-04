import flet as ft

from navigation_system.widget import Sidebar
from navigation_system.manager import ViewManager, Controller
from navigation_system.interface import ModuleView, EventView, Service, Repository
from navigation_system.widget.icon_text import IconText

# Ejemplo de implementaciones concretas


class HomeView(ModuleView):
    def __init__(self):
        super().__init__(
            content=ft.Column([
                ft.Text("Página de Inicio", size=24),
                ft.Text("Bienvenido a la aplicación"),
            ]),
            padding=20,
        )


class InventoryView(ModuleView):
    def __init__(self):
        super().__init__(
            content=ft.Column([
                ft.Text("Inventario", size=24),
                ft.Text("Gestión de productos"),
            ]),
            padding=20,
        )


class SalesView(ModuleView):
    def __init__(self):
        super().__init__(
            content=ft.Column([
                ft.Text("Ventas", size=24),
                ft.Text("Registro y gestión de ventas"),
            ]),
            padding=20,
        )


class HomeEvents(EventView):
    def __init__(self, view: ModuleView, services: list[Service]) -> None:
        super().__init__(view, services)

    def _connect_events(self) -> None:
        # Conectar eventos si los hubiera
        pass


class InventoryEvents(EventView):
    def __init__(self, view: ModuleView, services: list[Service]) -> None:
        super().__init__(view, services)

    def _connect_events(self) -> None:
        # Conectar eventos si los hubiera
        pass


class SalesEvents(EventView):
    def __init__(self, view: ModuleView, services: list[Service]) -> None:
        super().__init__(view, services)

    def _connect_events(self) -> None:
        # Conectar eventos si los hubiera
        pass


class HomeRepository(Repository):
    pass


class InventoryRepository(Repository):
    pass


class SalesRepository(Repository):
    pass


class HomeService(Service):
    pass


class InventoryService(Service):
    pass


class SalesService(Service):
    pass

# Ejemplo de uso en una aplicación Flet


def main(page: ft.Page):
    page.title = "Ejemplo de Navegación"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0

    # Definir constantes para los nombres de módulos
    INICIO = "Inicio"
    INVENTARIO = "Inventario"
    VENTAS = "Ventas"

    # Configurar el gestor de vistas
    view_manager = ViewManager()

    # Registrar controladores para las diferentes vistas
    view_manager[INICIO] = Controller(
        view_class=HomeView,
        event_class=HomeEvents,
        service_classes={
            HomeService: [HomeRepository]
        }
    )

    view_manager[INVENTARIO] = Controller(
        view_class=InventoryView,
        event_class=InventoryEvents,
        service_classes={
            InventoryService: [InventoryRepository]
        }
    )

    view_manager[VENTAS] = Controller(
        view_class=SalesView,
        event_class=SalesEvents,
        service_classes={
            SalesService: [SalesRepository]
        }
    )

    # Configurar íconos para cada módulo
    modulos_iconos = {
        "Rutinas": ft.Icons.RUN_CIRCLE,
        "Ejercicios": ft.Icons.FITNESS_CENTER,
        "My Kids": ft.Icons.PERSON,
        "Suscripción": ft.Icons.SUBSCRIPTIONS,
        "Configuración": ft.Icons.SETTINGS,
        "Nutricionistas": ft.Icons.FOOD_BANK,
        "Entrenadores": ft.Icons.FITNESS_CENTER,
        "Mensajes": ft.Icons.MESSAGE,
        "Estadísticas": ft.Icons.DATASET_SHARP,
    }

    # Variable para almacenar la vista actual
    current_view = view_manager[INICIO]  # Vista inicial

    # Función para manejar la selección en la barra lateral
    def on_view_selected(event: ft.ControlEvent):
        # module_name = event.control.content.controls[1].value
        # current_view = view_manager[module_name]
        # main_content.content = current_view
        # page.update()
        print("Nada")

    # Crear la barra lateral
    sidebar = Sidebar(
        company_name="Jumpingkids",
        icon_company=ft.Icons.RUN_CIRCLE,
        module_names_and_icons=modulos_iconos,
        on_select=on_view_selected,
        # default_selected=INICIO,
    )

    # Contenedor para la vista actual
    main_content = view_manager[INICIO]

    page.appbar = ft.AppBar(
        leading=ft.Row(
            controls=[
                ft.Container(width=10),
                IconText(
                    "Jumpingkids",
                    icon=ft.Icons.RUN_CIRCLE,
                    size=20,
                    selected_color=ft.Colors.WHITE,
                    default_color=ft.Colors.WHITE70,
                ),
            ]
        ),
        bgcolor=ft.Colors.BLUE_GREY_900,
    )

    # Estructura principal de la aplicación
    page.add(
        ft.Row(
            [
                sidebar,
                main_content,
            ],
            expand=True,
        )
    )


# Lanzar la aplicación
ft.app(target=main)
