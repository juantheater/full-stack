import reflex as rx 
import reflex_local_auth

from ..ui.base import base_page

@reflex_local_auth.require_login
def protected_page() -> rx.Component:
    my_child = rx.vstack(
            rx.heading("Protect Page", size="9"),
            rx.text(
                "Protected page",
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
        )
    return base_page(my_child)