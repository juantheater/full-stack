"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""
    pass

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(rx.text(text, size="4", weight="medium"), href=url)


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="https://web.reflex-assets.dev/other/logo.jpg",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading("Reflex", size="7", weight="bold"),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", "/#"),
                    rx.menu.root(
                        rx.menu.trigger(
                            rx.button(
                                rx.text("Services", size="4", weight="medium"),
                                rx.icon("chevron-down"),
                                weight="medium",
                                variant="ghost",
                                size="3",
                            ),
                        ),
                        rx.menu.content(
                            rx.menu.item("Service 1"),
                            rx.menu.item("Service 2"),
                            rx.menu.item("Service 3"),
                        ),
                    ),
                    navbar_link("Pagina", "/pagina"),
                    navbar_link("Contact", "/#"),
                    justify="end",
                    spacing="5",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="https://web.reflex-assets.dev/other/logo.jpg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading("Reflex", size="6", weight="bold"),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=30)),
                    rx.menu.content(
                        rx.menu.item("Home"),
                        rx.menu.sub(
                            rx.menu.sub_trigger("Services"),
                            rx.menu.sub_content(
                                rx.menu.item("Service 1"),
                                rx.menu.item("Service 2"),
                                rx.menu.item("Service 3"),
                            ),
                        ),
                        rx.menu.item("About"),
                        rx.menu.item("Pagina"),
                        rx.menu.item("Contact"),
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


def base_page(child:rx.Component,*args,**kargs)->rx.Component:
    return rx.fragment(
        navbar(),
        rx.box(
            rx.center(
                child
            ),
        ),
        rx.logo(),
        rx.color_mode.button(position="bottom-left")
    )

def index() -> rx.Component:
    # Welcome Page (Index)
        index_child=rx.vstack(
            rx.flex(
                rx.heading(
                "Welcome to Reflex!", 
                size="9",
                align="center",
                direction="column",
                width="100%"
                )
            ),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        return base_page(index_child)


def pagina() -> rx.Component:
    # Welcome Page (Index)
        pagina_child=rx.vstack(
            rx.flex(
                rx.heading(
                "Mi pagina", 
                size="9",
                align="center",
                direction="column",
                width="100%"
                )
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        return base_page(pagina_child)


app = rx.App()
app.add_page(index)
app.add_page(pagina,route="/pagina")