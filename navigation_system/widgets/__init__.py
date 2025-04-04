"""
Este paquete pretende ser un marco de trabajo para la navegación de una aplicación. Provee un gestor de vistas que internamente usa un controlador que permite conectar los insumos necesarios para dar vida a una vista. Y además del controlador, provee un control de navegación lateral que permite cambiar entre vistas y que funciona perfectamente con el controlador.
"""
from navigation_system.widgets.sidebar import Sidebar
from navigation_system.manager.controller import Controller
from navigation_system.manager.view_manager import ViewManager


__all__ = [
    "Sidebar",
    "ViewManager",
    "Controller",
]
