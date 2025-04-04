from navigation_system.widget.selectable import Selectable


class Switch:

    def __init__(self, default_selectabel: Selectable) -> None:
        self._current_selectable: Selectable = default_selectabel
    
    @property
    def current_selectable(self) -> Selectable:
        return self._current_selectable
    
    @current_selectable.setter
    def current_selectable(self, value: Selectable) -> None:
        self._current_selectable = value