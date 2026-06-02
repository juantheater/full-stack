import reflex as rx
from full_stack.ui.base import base_page
from ..navigation import routes
import asyncio


class ContactEntryModel(rx.Model, table=True):
    __tablename__ = 'contactentrymodel'
    __table_args__ = {'extend_existing': True}
    nombre:str
    apellido:str
    email:str
    mensaje:str

class ContactState(rx.State):
    form_data:dict={}
    did_submit:bool=False
    
    @rx.var
    def thank_you(self)->str:
        nombre=self.form_data.get("first_name") or ""
        return f"Gracias {nombre}".strip() + "!"

    @rx.event
    async def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        #print(form_data)
        self.form_data = form_data
        yield
        await asyncio.sleep(3)
        self.did_submit=False
        yield

@rx.page(route=routes.CONTACTO_ROUTE)
def contact_page() -> rx.Component:
    my_form=rx.form(
            rx.vstack(
                rx.hstack(
                    rx.input(
                    placeholder="First Name",
                    name="first_name",
                    required=True,
                    width="100%"
                    ),
                rx.input(
                    placeholder="Last Name",
                    name="last_name",
                    width="100%"
                    ),
                    width="100%"
                ),
                rx.input(
                    name="email",
                    placeholder="email",
                    type="email",
                    width="100%"
                ),
                rx.text_area(
                    placeholder="message",
                    name="message",
                    required=True,
                    width="100%"
                    ),
                rx.button("Submit", type="submit"),
            ),
            on_submit=ContactState.handle_submit,
            reset_on_submit=True
    )
    my_contact_child=rx.vstack(
        rx.heading(
            "Contact us!",
            size="9"
        ),
        rx.cond(ContactState.did_submit,ContactState.thank_you,""),
        rx.desktop_only(
            rx.box(
                my_form,
                width="50vw"
            ),
        ),
        rx.mobile_and_tablet(
            my_form
        ),
        spacing="5",
        justify="center",
        min_height="85vh",
        align="center"
    )
    return base_page(
        my_contact_child
    )