import flet as ft

from navigation_system.widget import Sidebar
from navigation_system.manager import ViewManager, Controller
from navigation_system.widget.sidebar import SidebarContent, SidebarGroup, SidebarItem


# Función principal de la aplicación
def main(page: ft.Page):
    page.title = "Jumpingkids"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.bgcolor = ft.Colors.BLUE_GREY_50

    page.appbar = ft.AppBar(
        leading=ft.Row(
            controls=[
                ft.Container(width=10),
                ft.Icon(ft.Icons.RUN_CIRCLE, size=30, color=ft.Colors.WHITE),
                ft.Text("Jumpingkids", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
            ]
        ),
        bgcolor=ft.Colors.BLUE_GREY_900,
    )

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


    # Crear la barra lateral
    sidebar = Sidebar(
        company_name="Jumpingkids",
        sidebar_content=sidebar_content,
        default_selected=INICIO,
    )

    # Estructura principal de la aplicación
    page.add(
        ft.Row(
            controls=[
                sidebar,
            ],
            expand=True,
            spacing=0,
        )
    )


# Lanzar la aplicación
if __name__ == "__main__":
    ft.app(target=main)