import flet as ft

from navigation_system.widget.icon_text import IconText


class Selectable(ft.Container):
    def __init__(
        self,
        label: str,
        icon: ft.Icons,
        on_click=None,
        selected_color: ft.Colors = ft.Colors.BLUE_GREY_800,
        hover_color: ft.Colors = ft.Colors.BLUE_GREY_700,

    ) -> None:
        self._label = label
        self._icon_text = IconText(label, icon)
        self._selected = False
        self._on_click = on_click
        self._selected_color = selected_color
        self._hover_color = hover_color

        super().__init__(
            content=self._icon_text,
            padding=ft.padding.symmetric(horizontal=10, vertical=5),
            on_click=self._on_click_envolve,
            ink=True,
            bgcolor=None,
            border_radius=10,
        )
    
    @property
    def selected(self) -> bool:
        return self._selected

    @selected.setter
    def selected(self, value: bool) -> None:
        """Al seleccionar el control, se cambia el color del ``ft.Container`` y el color del ``IconText``."""
        self._selected = value
        self.bgcolor = self._selected_color if value else None
        self._icon_text.selected = value
        # self.update()

    def _on_click_envolve(self, event: ft.ControlEvent):
        self.selected = True
        if self._on_click:
            self._on_click(event)
