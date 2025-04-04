from navigation_system.widgets.selectable import Selectable


class Switch:

    def __init__(self, selectables: list[Selectable]) -> None:
        self._items: list[Selectable] = selectables
    
    def execute(self) -> None:
        position = self._get_selectable_selected_position()
        self._items[position].selected = False
        for item in self._items:
            item.selected = False
    
    def _get_selectable_selected_position(self) -> int:
        position = 0
        for index, item in enumerate(self._items):
            if item.selected:
                position = index
                break
        return position