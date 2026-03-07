"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
import reflex_local_auth
from rxconfig import config
from .ui.base import base_page
from .pages.about import about_page
from .pages.pricing import pricing_page
from .navigation import routes
from .auth.pages import registro_espanol



class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    # Welcome Page (Index)
    my_index_child = rx.vstack(
        rx.heading(
            "Welcome to Reflex!", size="9"
        ),
        rx.text(
            "Get started by editing ",
            rx.code(f"{config.app_name}/{config.app_name}.py"),
            size="5",
        ),
        rx.link(
            "Este es un link para about",
            href="/about"
        ),
        rx.link(
            rx.button("Check out our docs!"),
            href="https://reflex.dev/docs/getting-started/introduction/",
            is_external=True,
        ),
        spacing="5",
        justify="center",
        min_height="85vh",
        align="center"
    )
    return base_page(my_index_child)


app = rx.App()
app.add_page(index)
# reflex_local_auth pages
app.add_page(
    reflex_local_auth.pages.login_page,
    route=reflex_local_auth.routes.LOGIN_ROUTE,
    title="Login",
)
app.add_page(registro_espanol, route="/registrarse"),

# my pages
app.add_page(about_page,route=routes.ABOUT_US_ROUTE)
app.add_page(pricing_page,route=routes.PRICING_ROUTE)