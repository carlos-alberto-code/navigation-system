import flet as ft

from navigation_system.widgets.icon_text import IconText
from navigation_system.widgets.selectable import Selectable


# class Sidebar(ft.Container):

#     def __init__(
#         self,
#         title: str,
#         items: list[str],
#         trailing: list[ft.Control],
#         on_select=None,
#     ) -> None:
#         super().__init__(
#             width=250,
#             padding=15,
#             expand=True,
#             bgcolor=ft.Colors.BLUE_GREY_900,
#         )
#         self.content = ft.Column(
#             controls=[
#                 IconText(
#                     label=title,
#                     icon=ft.Icons.BRANDING_WATERMARK,
#                     size=18,
#                 ),
#                 ft.Divider(color=ft.Colors.WHITE, thickness=0.5),
#                 *items,
#                 ft.Divider(color=ft.Colors.WHITE, thickness=0.5),
#                 ft.Column(
#                     controls=[*trailing],
#                     alignment=ft.MainAxisAlignment.END,
#                     expand=True,
#                 ),
#             ],
#             alignment=ft.MainAxisAlignment.START,
#             spacing=10,

#         )

#     def event_wrapper(self, event: ft.ControlEvent):
#         ...


class Sidebar(ft.NavigationDrawer):
    def __init__(self, view_names: list[str]):
        super().__init__(bgcolor=ft.Colors.BLUE_GREY_900,)
        self.view_names: list[str] = view_names
