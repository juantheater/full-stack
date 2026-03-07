import reflex as rx
from full_stack.ui.base import base_page

def about_page() -> rx.Component:
    
    my_about_child=rx.vstack(
        rx.heading(
            "Welcome to About!", size="9"
        ),
        rx.text(
            "This is a new page",
            size="5",
        ),
        rx.link(
            rx.button("About!"),
            href="https://reflex.dev/docs/getting-started/introduction/",
            is_external=True,
        ),
            spacing="5",
            justify="center",
            min_height="85vh",
            align="center"
    )
    return base_page(
        my_about_child
    )