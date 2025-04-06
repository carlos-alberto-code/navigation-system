# navigation-system

Es un marco para gestionar la navegación de una aplicación Flet.

## Descripción

El `navigation-system` es un framework diseñado para facilitar la navegación en aplicaciones desarrolladas con [Flet](https://flet.dev/). Proporciona componentes reutilizables como barras laterales, gestores de vistas y controladores que permiten conectar vistas, eventos y servicios de manera estructurada.

## Características

- **Sidebar interactiva**: Una barra lateral personalizable para navegar entre diferentes vistas.
- **Gestión de vistas**: Controladores que conectan vistas con eventos y servicios.
- **Modularidad**: Soporte para vistas modulares que pueden ser fácilmente registradas y gestionadas.
- **Estética mejorada**: Controles con efectos visuales para hover y selección.

## Instalación

1. Asegurate de tener instalado poetry.

2. Activa el entorno virtual:
   ```bash
   poetry shell
   ```

3. Instala las dependencias usando [Poetry](https://python-poetry.org/):
   ```bash
   poetry install
   ```

4. Agrega el proyecto como una dependencia de poetry desde el repositorio de GitHub:
    ```bash
    poetry add git+https://github.com/carlos-alberto-code/navigation-system.git
    ```

4. Ejecuta la aplicación:
   ```bash
   python main.py
   ```

## Ejemplo de Uso

A continuación, se muestra un ejemplo básico de cómo configurar y usar el `navigation-system`:

```python
from navigation_system.widget.sidebar import SidebarContent, SidebarGroup, SidebarItem, Sidebar
import flet as ft

def main(page: ft.Page):
    sidebar_content = SidebarContent(
        groups=[
            SidebarGroup(
                title="Finanzas",
                items=[
                    SidebarItem(name="Presupuestos", icon=ft.Icons.ATTACH_MONEY),
                    SidebarItem(name="Facturación", icon=ft.Icons.RECEIPT),
                ],
            ),
        ]
    )

    def on_change(event: ft.ControlEvent):
        print(f"Vista seleccionada: {event.control}")

    sidebar = Sidebar(
        sidebar_content=sidebar_content,
        company_name="Mi Empresa",
        on_select=on_change,
    )

    page.add(sidebar)

ft.app(target=main)
```

## Estructura del Proyecto

```plaintext
navigation-system/
├── navigation_system/
│   ├── widget/
│   │   ├── sidebar/
│   │   │   ├── __init__.py
│   │   │   ├── sidebar.py
│   │   │   ├── selectable.py
│   │   │   ├── switch.py
│   │   │   └── icon_text.py
│   ├── manager/
│   │   ├── __init__.py
│   │   ├── controller.py
│   │   └── view_manager.py
│   ├── interface/
│   │   ├── __init__.py
│   │   ├── module_view.py
│   │   ├── event_view.py
│   │   ├── service.py
│   │   └── repository.py
├── pyproject.toml
└── README.md
```

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas contribuir, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
