import reflex as rx
import reflex_local_auth
from full_stack.navigation import routes
from  full_stack.navigation.state import NavState 


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(rx.text(text, size="4", weight="medium"), href=url)


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Reflex", size="7", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link(
                        "Home", routes.HOME
                    ),
                    navbar_link(
                        "About", routes.ABOUT_US_ROUTE
                    ),
                    navbar_link(
                        "Pricing", routes.PRICING_ROUTE
                    ),
                    navbar_link(
                        "Contact", routes.CONTACTO_ROUTE
                    ),
                    spacing="5",
                ),
                rx.hstack(
                    rx.link(
                        rx.button(
                            "Registrarse", 
                            size="3", 
                            variant="outline"
                        ),
                        href=reflex_local_auth.routes.REGISTER_ROUTE
                    ),
                    rx.link(
                        rx.button(
                            "Login", 
                            size="3"
                        ),
                        href=reflex_local_auth.routes.LOGIN_ROUTE
                    ),
                    spacing="4",
                    justify="end",
                ),
            justify="between",
            align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg", width="2em", height="auto", border_radius="25%"
                    ),
                    rx.heading("Reflex", size="6", weight="bold"),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=30)),
                    rx.menu.content(
                        rx.menu.item(
                            "Home",
                            on_click=NavState.to_home
                        ),
                        rx.menu.item(
                            "About",
                            on_click=NavState.to_about_us
                        ),
                        rx.menu.item(
                            "Pricing",
                            on_click=NavState.to_pricing
                        ),
                        rx.menu.item(
                            "Contact",
                            on_click=NavState.to_contacto
                        ),
                        rx.menu.separator(),
                        rx.menu.item(
                            "Login",
                            on_click=NavState.to_login
                        ),
                        rx.menu.item(
                            "Register",
                            on_click=NavState.to_register
                        ),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )