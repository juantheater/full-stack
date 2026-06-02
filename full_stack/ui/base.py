import reflex as rx
#from ..auth.state import SessionState
from .nav import navbar



def base_page(child:rx.Component,*args,**kwargs)->rx.Component:
    return rx.fragment(
        navbar,
        child,
        rx.color_mode.button(
            position="button-left"
        )
    )