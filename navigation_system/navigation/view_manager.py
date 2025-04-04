from navigation_system.navigation.controller import Controller
from navigation_system.interface.module_view import ModuleView


class ViewManager:
    """
    Gestiona las vistas de la aplicación utilizando Controllers.
    
    Esta clase proporciona mecanismos para:
    1. Registrar Controllers para diferentes módulos
    2. Obtener vistas reconstruidas bajo demanda
    
    Cada vez que se solicita una vista, se reconstruye completamente,
    lo que garantiza un estado fresco pero puede implicar más tiempo
    de procesamiento en las transiciones.
    
    Ejemplo de uso:
    ```python
    view_manager = ViewManager()
    view_manager["inventory"] = Controller(
        view=InventoryView,
        events=InventoryEvents,
        services={
            InventoryServiceCore: (InventoryRepositoryAdapter, ProductsRepositoryAdapter),
            StoreServiceCore: (StoreRepositoryAdapter,)
        }
    )
    
    # Obtener la vista instanciada (reconstruida cada vez)
    inventory_view = view_manager["inventory"]  # Retorna un ft.Control
    ```
    """

    def __init__(self) -> None:
        self._controllers: dict[str, Controller] = {}

    def __getitem__(self, key: str) -> ModuleView:
        if key not in self._controllers:
            raise KeyError(f"Controlador no registrado: {key}")
        
        controller = self._controllers[key]
        return controller.build()

    def __setitem__(self, key: str, controller: Controller) -> None:
        self._controllers[key] = controller
    
    def keys(self) -> list[str]:
        """Devuelve una lista de las claves de los controladores registrados. Pueden ser usadas como nombres de vistas."""
        return list(self._controllers.keys())
    