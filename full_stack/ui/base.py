import reflex as rx

from .nav import navbar

def base_page(child:rx.Component)->rx.Component:
    return rx.fragment(
        navbar(),
        child,
        rx.logo(),
        rx.color_mode.button(position="bottom-left")
    )