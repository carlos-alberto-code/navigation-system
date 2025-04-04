import flet as ft

from navigation_system.widget.switch import Switch
from navigation_system.widget.icon_text import IconText
from navigation_system.widget.selectable import Selectable


class Sidebar(ft.Container):
    """
    Un componente de barra lateral para navegación entre vistas.

    Proporciona una interfaz visual para navegar entre diferentes vistas
    de la aplicación, manteniendo el estado de selección y desencadenando
    eventos cuando el usuario selecciona una vista.

    Ejemplo de uso:
    ```python
    # Definir los nombres de los módulos como constantes
    INVENTARIO = "Inventario"
    VENTAS = "Ventas"

    # Configurar el ViewManager
    view_manager = ViewManager()
    view_manager[INVENTARIO] = Controller(...)
    view_manager[VENTAS] = Controller(...)

    # Crear el diccionario de íconos
    modulos_iconos = {
        INVENTARIO: ft.Icons.INVENTORY,
        VENTAS: ft.Icons.POINT_OF_SALE
    }

    # Función para manejar la selección
    def on_view_selected(e, view_name):
        # Cargar la vista seleccionada
        main_content.content = view_manager[view_name]
        page.update()

    # Crear el sidebar
    sidebar = Sidebar(
        title="Mi Aplicación",
        items_content=modulos_iconos,
        on_select=on_view_selected,
    )
    ```
    """

    def __init__(
        self,
        company_name: str,
        icon_company: ft.Icons,
        module_names_and_icons: dict[str, ft.Icons],
        on_select=None,
        default_selected: str | None = None,
        width: int = 250,
        bgcolor=ft.Colors.BLUE_GREY_900,
    ) -> None:
        self._company_name = company_name
        self._icon_company = icon_company
        self._module_names_and_icons = module_names_and_icons
        self._on_select = on_select
        self._default_selected = default_selected

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


        # Construir la interfaz
        super().__init__(
            width=width,
            padding=10,
            bgcolor=bgcolor,
            content=self._build_layout(),
        )

    def _create_selectables(self):
        """Crea los elementos seleccionables para cada vista."""
        self._selectables = {
            module_name: Selectable(
                label=module_name,
                icon=icon,
                on_click=self._envolve_on_select_event,
            )
            for module_name, icon in self._module_names_and_icons.items()
        }

    def _envolve_on_select_event(self, event: ft.ControlEvent):
        """Maneja el evento de selección de un elemento. Envuelve el evento de entrada que maneja la lógica de cambio de vista. Mientras que internamente maneja la lógica de selección correspondiente al Sidebar."""
        # Capturamos el control que disparó el evento
        selectable: Selectable = event.control
        # Desmarcamos el Selectable actual
        self._switch.current_selectable.selected
        # Marcamos el nuevo Selectable
        selectable.selected = True
        # Actualizamos el switch
        self._switch.current_selectable = selectable
        # Ejecutamos la lógica entrante de selección
        if self._on_select:
            self._on_select(event)

    def _build_layout(self) -> ft.Column:
        """Construye la barra lateral."""
        return ft.Column(
            controls=[
                *self._selectables.values(),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

    