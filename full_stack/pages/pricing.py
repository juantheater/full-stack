import reflex as rx
from full_stack.ui.base import base_page

def pricing_page() -> rx.Component:
    # Welcome Page (Index)
    my_pricing_child = rx.vstack(
        rx.heading(
            "Welcome to Pricing!", size="9"
        ),
        rx.text(
            "This is another one!",
            size="5",
        ),
        rx.link(
            rx.button("Pricing!"),
            href="https://reflex.dev/docs/getting-started/introduction/",
            is_external=True,
        ),
        spacing="5",
        justify="center",
        min_height="85vh",
        align="center"
    )
    return base_page(my_pricing_child)