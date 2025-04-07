import flet as ft

from navigation_system.widget.sidebar.icon_text import IconText


class Selectable(ft.Container):
    """
    Un componente seleccionable mejorado para usar en menús y listas.
    
    Este componente muestra un ítem con ícono y texto que puede ser seleccionado,
    con efectos visuales mejorados para hover y selección.
    """
    def __init__(
        self,
        label: str,
        icon: ft.Icons,
        on_click=None,
        selected_color: ft.Colors | None = None,
        hover_color: ft.Colors | None = None,
    ) -> None:
        self._label = label
        self._icon_text = IconText(label, icon)
        self._is_selected = False
        self._on_click = on_click
        self._selected_color = selected_color
        self._hover_color = hover_color

        super().__init__(
            content=self._icon_text,
            padding=ft.padding.symmetric(horizontal=16, vertical=10),
            on_click=self._on_click_envolve,
            on_hover=self._on_hover,
            ink=True,
            border_radius=8,
            animate=ft.animation.Animation(300, ft.AnimationCurve.EASE_OUT),
        )
    
    @property
    def is_selected(self) -> bool:
        return self._is_selected

    @is_selected.setter
    def is_selected(self, value: bool) -> None:
        """Al seleccionar el control, se cambia el color del ``ft.Container`` y el color del ``IconText``."""
        self._is_selected = value
        self.bgcolor = self._selected_color if value else None
        self._icon_text.selected = value
        
        # Añadir un indicador visual lateral cuando está seleccionado
        if value:
            self.border = ft.border.only(
                left=ft.BorderSide(10, ft.Colors.LIGHT_BLUE_300)
            )
        else:
            self.border = None

    def _on_click_envolve(self, event: ft.ControlEvent):
        self.is_selected = True
        if self._on_click:
            self._on_click(event)
    
    def _on_hover(self, event: ft.ControlEvent):
        """Cambia el color de fondo al pasar el cursor sobre el elemento."""
        if not self._is_selected:
            self.bgcolor = self._hover_color if event.data == "true" else None
            self.update()