"""
Este paquete pretende ser un marco de trabajo para la navegación de una aplicación. Provee un gestor de vistas que internamente usa un controlador que permite conectar los insumos necesarios para dar vida a una vista. Y además del controlador, provee un control de navegación lateral que permite cambiar entre vistas y que funciona perfectamente con el controlador.
"""
from navigation_system.widget.sidebar.sidebar import Sidebar, SidebarItem, SidebarGroup, SidebarContent


__all__ = [
    "Sidebar",
    "SidebarItem",
    "SidebarGroup",
    "SidebarContent"
]
