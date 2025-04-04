import flet as ft

from navigation_system.widget import Sidebar
from navigation_system.manager import ViewManager, Controller
from navigation_system.interface import ModuleView, EventView, Service, Repository
from navigation_system.widget.sidebar import SidebarContent, SidebarGroup, SidebarItem


# Ejemplo de implementaciones concretas
class HomeView(ModuleView):
    def __init__(self):
        super().__init__(
            content=ft.Container(
                content=ft.Column([
                    ft.Text("Página de Inicio", size=24, weight=ft.FontWeight.BOLD),
                    ft.Container(height=20),
                    ft.Text("Bienvenido a la aplicación", size=16),
                ]),
                padding=20,
                bgcolor=ft.Colors.WHITE,
                border_radius=8,
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=10,
                    color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK),
                    offset=ft.Offset(0, 2),
                ),
            ),
            padding=20,
            bgcolor=ft.Colors.BLUE_GREY_50,
            expand=True,
        )


class RoutinesView(ModuleView):
    def __init__(self):
        super().__init__(
            content=ft.Container(
                content=ft.Column([
                    ft.Text("Rutinas", size=24, weight=ft.FontWeight.BOLD),
                    ft.Container(height=20),
                    ft.Text("Gestión de rutinas de ejercicio", size=16),
                ]),
                padding=20,
                bgcolor=ft.Colors.WHITE,
                border_radius=8,
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=10,
                    color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK),
                    offset=ft.Offset(0, 2),
                ),
            ),
            padding=20,
            bgcolor=ft.Colors.BLUE_GREY_50,
            expand=True,
        )


class ExercisesView(ModuleView):
    def __init__(self):
        super().__init__(
            content=ft.Container(
                content=ft.Column([
                    ft.Text("Ejercicios", size=24, weight=ft.FontWeight.BOLD),
                    ft.Container(height=20),
                    ft.Text("Biblioteca de ejercicios", size=16),
                ]),
                padding=20,
                bgcolor=ft.Colors.WHITE,
                border_radius=8,
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=10,
                    color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK),
                    offset=ft.Offset(0, 2),
                ),
            ),
            padding=20,
            bgcolor=ft.Colors.BLUE_GREY_50,
            expand=True,
        )


# Eventos para cada vista
class HomeEvents(EventView):
    def __init__(self, view: ModuleView, services: list[Service]) -> None:
        super().__init__(view, services)

    def _connect_events(self) -> None:
        pass


class RoutinesEvents(EventView):
    def __init__(self, view: ModuleView, services: list[Service]) -> None:
        super().__init__(view, services)

    def _connect_events(self) -> None:
        pass


class ExercisesEvents(EventView):
    def __init__(self, view: ModuleView, services: list[Service]) -> None:
        super().__init__(view, services)

    def _connect_events(self) -> None:
        pass


# Repositorios simples
class HomeRepository(Repository):
    pass


class RoutinesRepository(Repository):
    pass


class ExercisesRepository(Repository):
    pass


# Servicios para cada módulo
class HomeService(Service):
    pass


class RoutinesService(Service):
    pass


class ExercisesService(Service):
    pass


# Función principal de la aplicación
def main(page: ft.Page):
    page.title = "Jumpingkids"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.bgcolor = ft.Colors.BLUE_GREY_50

    # Definir constantes para los nombres de módulos
    INICIO = "Inicio"
    RUTINAS = "Rutinas"
    EJERCICIOS = "Ejercicios"
    MY_KIDS = "My Kids"
    NUTRICIONISTAS = "Nutricionistas"
    ENTRENADORES = "Entrenadores"
    MENSAJES = "Mensajes"
    ESTADISTICAS = "Estadísticas"
    SUSCRIPCION = "Suscripción"
    CONFIGURACION = "Configuración"

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

    view_manager[RUTINAS] = Controller(
        view_class=RoutinesView,
        event_class=RoutinesEvents,
        service_classes={
            RoutinesService: [RoutinesRepository]
        }
    )

    view_manager[EJERCICIOS] = Controller(
        view_class=ExercisesView,
        event_class=ExercisesEvents,
        service_classes={
            ExercisesService: [ExercisesRepository]
        }
    )

    # Configuración del contenido del sidebar
    sidebar_content = SidebarContent(
        groups=[
            SidebarGroup(
                title="Principal",
                items=[
                    SidebarItem(name=INICIO, icon=ft.Icons.HOME),
                    SidebarItem(name=RUTINAS, icon=ft.Icons.RUN_CIRCLE),
                    SidebarItem(name=EJERCICIOS, icon=ft.Icons.FITNESS_CENTER),
                    SidebarItem(name=MY_KIDS, icon=ft.Icons.PERSON),
                ]
            ),
            SidebarGroup(
                title="Profesionales",
                items=[
                    SidebarItem(name=NUTRICIONISTAS, icon=ft.Icons.FOOD_BANK),
                    SidebarItem(name=ENTRENADORES, icon=ft.Icons.FITNESS_CENTER),
                ]
            ),
            SidebarGroup(
                title="Comunidad",
                items=[
                    SidebarItem(name=MENSAJES, icon=ft.Icons.MESSAGE),
                    SidebarItem(name=ESTADISTICAS, icon=ft.Icons.DATASET_SHARP),
                ]
            ),
            SidebarGroup(
                title="Cuenta",
                items=[
                    SidebarItem(name=SUSCRIPCION, icon=ft.Icons.PAYMENT),
                    SidebarItem(name=CONFIGURACION, icon=ft.Icons.SETTINGS),
                ]
            ),
        ]
    )

    # Variable para almacenar la vista actual
    current_view = view_manager[INICIO]  # Vista inicial
    content_container = ft.Container(content=current_view, expand=True)

    # Función para manejar la selección en la barra lateral
    def on_view_selected(event: ft.ControlEvent):
        nonlocal current_view, content_container
        
        # Obtener el nombre del ítem seleccionado
        selected_item_name = event.control.content.controls[1].value
        
        # Solo cambiar la vista si está registrada en el ViewManager
        if selected_item_name in view_manager.keys():
            current_view = view_manager[selected_item_name]
            content_container.content = current_view
            page.update()

    # Crear la barra lateral
    sidebar = Sidebar(
        company_name="Jumpingkids",
        icon_company=ft.Icons.RUN_CIRCLE,
        sidebar_content=sidebar_content,
        on_select=on_view_selected,
        default_selected=INICIO,
    )

    # Estructura principal de la aplicación
    page.add(
        ft.Row(
            controls=[
                sidebar,
                content_container,
            ],
            expand=True,
            spacing=0,
        )
    )


# Lanzar la aplicación
if __name__ == "__main__":
    ft.app(target=main)