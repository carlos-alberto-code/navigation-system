import flet as ft

from typing import Callable
from dataclasses import dataclass

from navigation_system.widget.switch import Switch
from navigation_system.widget.selectable import Selectable


@dataclass
class SidebarItem:
    """Clase para representar un elemento de la barra lateral."""
    name: str
    icon: ft.Icons


@dataclass
class SidebarGroup:
    """Clase para representar una sección de la barra lateral."""
    title: str
    items: list[SidebarItem]


@dataclass
class SidebarContent:
    """Clase para representar el contenido de la barra lateral."""
    groups: list[SidebarGroup]


class Sidebar(ft.Container):
    """
    Un componente de barra lateral mejorado para navegación entre vistas.

    Proporciona una interfaz visual organizada y atractiva para navegar entre diferentes vistas
    de la aplicación, con soporte para agrupaciones de ítems, encabezado y pie de página.

    Ejemplo de uso:
    ```python
    # Configurar el contenido del sidebar
    sidebar_content = SidebarContent(
        groups=[
            SidebarGroup(
                title="Principal",
                items=[
                    SidebarItem(name="Inicio", icon=ft.Icons.HOME),
                    SidebarItem(name="Inventario", icon=ft.Icons.INVENTORY),
                ]
            ),
            SidebarGroup(
                title="Administración",
                items=[
                    SidebarItem(name="Ventas", icon=ft.Icons.POINT_OF_SALE),
                    SidebarItem(name="Configuración", icon=ft.Icons.SETTINGS),
                ]
            ),
        ]
    )

    # Crear el sidebar
    sidebar = Sidebar(
        company_name="Mi Empresa",
        icon_company=ft.Icons.BUSINESS,
        sidebar_content=sidebar_content,
        on_select=on_view_selected,
        default_selected="Inicio",
    )
    ```
    """

    def __init__(
        self,
        company_name: str,
        icon_company: ft.Icons,
        sidebar_content: SidebarContent,
        on_select: Callable | None = None,
        default_selected: str | None = None,
        width: int = 250,
        bgcolor=ft.Colors.BLUE_GREY_900,
    ) -> None:
        self._company_name = company_name
        self._icon_company = icon_company
        self._sidebar_content = sidebar_content
        self._on_select = on_select
        self._default_selected = default_selected
        self._width = width
        self._bgcolor = bgcolor

        # Crear los elementos seleccionables para cada vista
        self._selectables: dict[str, Selectable] = {}
        self._create_selectables()

        # Seleccionar el elemento por defecto si se especificó
        if default_selected:
            if default_selected not in self._selectables:
                raise ValueError("El módulo por defecto no existe en la barra lateral")
            self._selectables[default_selected].selected = True
            # Pasar al switch el elemento seleccionado por defecto
            self._switch = Switch(self._selectables[default_selected])
        elif self._selectables:
            # Si no hay elemento por defecto pero existen elementos, seleccionar el primero
            first_item_name = list(self._selectables.keys())[0]
            self._selectables[first_item_name].selected = True
            self._switch = Switch(self._selectables[first_item_name])

        # Construir la interfaz
        super().__init__(
            width=width,
            bgcolor=bgcolor,
            content=self._build_layout(),
            padding=10,
        )

    def _create_selectables(self):
        """Crea los elementos seleccionables para cada vista."""
        for group in self._sidebar_content.groups:
            for item in group.items:
                self._selectables[item.name] = Selectable(
                    label=item.name,
                    icon=item.icon,
                    on_click=self._envolve_on_select_event,
                )

    def _envolve_on_select_event(self, event: ft.ControlEvent):
        """Maneja el evento de selección de un elemento."""
        # Capturamos el control que disparó el evento
        selectable: Selectable = event.control
        # Desmarcamos el Selectable actual
        self._switch.current_selectable.selected = False
        # Marcamos el nuevo Selectable
        selectable.selected = True
        # Actualizamos el switch
        self._switch.current_selectable = selectable
        # Ejecutamos la lógica entrante de selección
        if self._on_select:
            self._on_select(event)

    def _build_footer(self) -> ft.Container:
        """Construye el pie de página del sidebar."""
        return ft.Container(
            content=ft.Text(
                value=f"Versión 1.0.0 • © 2025 {self._company_name}",
                color=ft.Colors.with_opacity(0.5, ft.Colors.WHITE),
                size=12,
                text_align=ft.TextAlign.CENTER,
            ),
            padding=ft.padding.all(15),
            border=ft.border.only(top=ft.BorderSide(1, ft.Colors.with_opacity(0.1, ft.Colors.WHITE))),
        )
    
    def _build_group(self, group: SidebarGroup) -> ft.Column:
        """Construye un grupo de ítems para el sidebar."""
        items = [self._selectables[item.name] for item in group.items]
        
        return ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text(
                        value=group.title.upper(),
                        color=ft.Colors.with_opacity(0.5, ft.Colors.WHITE),
                        size=12,
                        weight=ft.FontWeight.BOLD,
                    ),
                    padding=ft.padding.only(left=16, top=12, bottom=4),
                ),
                *items,
            ],
            spacing=0,
            tight=True,
        )

    def _build_layout(self) -> ft.Column:
        """Construye la estructura completa del sidebar."""
        
        # Crear los grupos
        groups = [self._build_group(group) for group in self._sidebar_content.groups]
        
        # Crear el contenido principal (área scrollable)
        content = ft.Container(
            content=ft.Column(
                controls=groups,
                spacing=0,
                scroll=ft.ScrollMode.AUTO,
            ),
            expand=True,
            padding=ft.padding.symmetric(vertical=8),
        )
        
        # Crear el pie de página
        footer = self._build_footer()
        
        # Ensamblar todo
        return ft.Column(
            controls=[
                content,
                footer,
            ],
            spacing=0,
            expand=True,
        )