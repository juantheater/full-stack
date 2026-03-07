import asyncio
import reflex as rx
from full_stack.ui.base import base_page
from full_stack.navigation import routes


class ContactState(rx.State):
    form_data:dict={}
    did_submit:bool=False

    @rx.var
    def thank_you(self)->str:
        first_name=self.form_data.get("first_name")
        return f"Thank you {first_name}!"

    @rx.event
    async def handle_submit(self,form_data:dict):
        "Handle the form submit"
        print(form_data)
        self.form_data=form_data
        self.did_submit=True
        yield
        await asyncio.sleep(3)
        self.did_submit=False
        yield

@rx.page(route=routes.CONTACT_US_ROUTE)
def contact_page() -> rx.Component:
    my_form=rx.form(
        rx.vstack(
                rx.input(
                    name="first_name",
                    placeholder="First Name",
                    width='100%'
                ),
                rx.input(
                    name="last_name",
                    placeholder="Last Name",
                    width='100%'
                ),
                rx.text_area(
                    name='message',
                    placeholder='Your message',
                    width='100%'
                ),
                rx.button("Submit", type="submit"),
                align="center"
        ),
            on_submit=ContactState.handle_submit,
            reset_on_submit=True,
    )
    my_contact_child=rx.vstack(
        rx.heading(
            "Welcome to Contact!", size="9"
        ),
        rx.cond(
            ContactState.did_submit,ContactState.thank_you,""
        ),
        rx.link(
            rx.button("Contact Us!"),
            href="https://reflex.dev/docs/getting-started/introduction/",
            is_external=True,
        ),
            rx.desktop_only(
                rx.box(
                    my_form,
                    width='50vw'
                ),
            ),
            rx.mobile_and_tablet(
                rx.box(
                    my_form,
                    width='50vw'
                ),
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh"
    )
    return base_page(
        my_contact_child
    )