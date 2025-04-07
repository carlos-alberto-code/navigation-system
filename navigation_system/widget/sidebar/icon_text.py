import flet as ft


class IconText(ft.Row):
    """
    Un ``IconText`` es un control que muestra un icono y un texto en una fila.
    
    Está diseñado para ser usado en un ``Selectable``, cambiando el color del icono 
    y el texto cuando se selecciona, proporcionando feedback visual al usuario.

    ### Parámetros
    - ``label``: El texto que se mostrará en el control.
    - ``icon``: El icono que se mostrará en el control.
    - ``selected_color``: El color que tomará el icono y el texto cuando el control esté seleccionado.
    - ``default_color``: El color que tomará el icono y el texto cuando el control no esté seleccionado.
    - ``size``: El tamaño del texto.
    """

    def __init__(
        self,
        label: str,
        icon: ft.Icons,
        selected_color: ft.Colors | None = None,
        default_color: ft.Colors | None = None,
        size: int = 16,
    ) -> None:
        self._label = label
        self._icon = icon
        self._selected_color = selected_color
        self._default_color = default_color
        self._size = size
        self._selected: bool = False
        
        # Crear los controles con animación
        self._icon_control = ft.Icon(
            self._icon, 
            color=self._default_color,
            size=20,
            animate_opacity=ft.animation.Animation(300, ft.AnimationCurve.EASE_IN_OUT),
        )
        
        self._text_control = ft.Text(
            self._label, 
            color=self._default_color, 
            size=self._size,
            weight=ft.FontWeight.NORMAL,
            animate_opacity=ft.animation.Animation(300, ft.AnimationCurve.EASE_IN_OUT),
        )
        
        super().__init__(
            controls=[self._icon_control, self._text_control],
            spacing=12,
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

    @property
    def selected(self) -> bool:
        return self._selected

    @selected.setter
    def selected(self, value: bool) -> None:
        """
        Método que permite cambiar el estado de selección del control. 
        Cuando se selecciona, el color del icono y el texto cambia al color seleccionado,
        y se aplica negrita al texto para mayor énfasis visual.
        """
        self._selected = value
        color = self._selected_color if value else self._default_color
        weight = ft.FontWeight.BOLD if value else ft.FontWeight.NORMAL
        
        self._icon_control.color = color
        self._text_control.color = color
        self._text_control.weight = weight