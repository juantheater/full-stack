"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
import reflex_local_auth
from rxconfig import config
from .ui.base import base_page
from .auth.pages import (
    my_login_page,
    my_register_page,
    my_logout_page)

from .auth.state import SessionState
from . import contact,navigation,pages,pages
from .pages.protected import protected_page


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
app.add_page(index,title="Pagina del curso Reflex")

# reflex_local_auth pages
app.add_page(
    my_login_page,
    route=reflex_local_auth.routes.LOGIN_ROUTE,
    title="Login",
)
app.add_page(
    my_register_page,
    route=reflex_local_auth.routes.REGISTER_ROUTE,
    title="Register",
)

app.add_page(
    my_logout_page,
    route=navigation.routes.LOGOUT_ROUTE,
    title="Logout",
)

# my pages
app.add_page(
    pages.pricing_page, 
    route=navigation.routes.PRICING_ROUTE
)

app.add_page(
    pages.about_page,
    route=navigation.routes.ABOUT_US_ROUTE
)

app.add_page(
    contact.contact_page, 
    route=navigation.routes.CONTACT_US_ROUTE
)

app.add_page(
    contact.contact_entries_list_page, 
    route=navigation.routes.CONTACT_ENTRIES_ROUTE,
    on_load=contact.ContactState.list_entries
)

app.add_page(
    protected_page, 
    route="/protected/",
    on_load=SessionState.on_load
)