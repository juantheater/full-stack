import reflex as rx 

from ..auth.state import SessionState
from .state import ContactState

def contact_form() -> rx.Component:
    return rx.form(
            # rx.cond(
            #     SessionState.my_user_id,
            #     rx.box(
            #         rx.input(
            #             type='hidden',
            #             name='user_id',
            #             value=SessionState.my_user_id
            #         ),
            #         display='none'
            #     ),
            #     rx.fragment('')
            # ),
            rx.vstack(
                rx.hstack(
                    rx.input(
                        name="Nombre",
                        placeholder="Nombre",
                        required=True,
                        type='text',
                        width='100%',
                    ),
                    rx.input(
                        name="Apellido",
                        placeholder="Apellido",
                        type='text',
                        width='100%',
                    ),
                    width='100%'
                ),
                rx.input(
                    name='Email',
                    placeholder='Tu email',
                    type='email',
                    width='100%',
                ),
                rx.text_area(
                    name='message',
                    placeholder="Mensaje",
                    required=True,
                    width='100%',
                ),
                rx.button(
                    "Enviar",
                    type="submit"
                    ),
                    align="center"
            ),
            on_submit=ContactState.handle_submit,
            reset_on_submit=True,
    )