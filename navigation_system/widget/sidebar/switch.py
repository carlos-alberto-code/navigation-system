from navigation_system.widget.sidebar.selectable import Selectable


class Switch:
    """
    Un administrador para elementos de UI seleccionables.
    
    Esta clase maneja el estado de selección de elementos de UI que implementan
    la interfaz Selectable.
    
    ### Comportamiento:
    - En la inicialización, el elemento seleccionable predeterminado se establece como la selección actual
    - Al cambiar a un nuevo elemento, el elemento actual se deselecciona (``selected=False``)
      y el nuevo elemento se selecciona (``selected=True``)
    """

    def __init__(self, default_selectable: Selectable) -> None:
        self._current_selectable: Selectable = default_selectable
        self._current_selectable.is_selected = True
    
    @property
    def current_selectable(self) -> Selectable:
        """Obtiene el elemento actualmente seleccionado."""
        return self._current_selectable
    
    @current_selectable.setter
    def current_selectable(self, value: Selectable) -> None:
        if value is not self._current_selectable:
            self._current_selectable.is_selected = False
            self._current_selectable = value
            self._current_selectable.is_selected = True
