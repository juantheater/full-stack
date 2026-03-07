import reflex as rx
import reflex_local_auth

def registro_espanol() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Crear una cuenta", size="8", margin_bottom="4px"),
            rx.text(
                "Únete a nuestra comunidad hoy mismo.",
                color_scheme="gray",
                margin_bottom="24px",
            ),
            
            # Formulario de registro
            rx.form(
                rx.vstack(
                    rx.text("Nombre de usuario", weight="bold", size="2"),
                    rx.input(
                        placeholder="Ej: juan_perez",
                        name="username",
                        size="3",
                        width="100%",
                        required=True,
                    ),
                    
                    rx.text("Correo electrónico", weight="bold", size="2", margin_top="12px"),
                    rx.input(
                        placeholder="correo@ejemplo.com",
                        name="email",
                        type="email",
                        size="3",
                        width="100%",
                        required=True,
                    ),
                    
                    rx.text("Contraseña", weight="bold", size="2", margin_top="12px"),
                    rx.input(
                        placeholder="Mínimo 8 caracteres",
                        name="password",
                        type="password",
                        size="3",
                        width="100%",
                        required=True,
                    ),
                    
                    rx.button(
                        "Registrarse",
                        type="submit",
                        size="3",
                        width="100%",
                        margin_top="24px",
                        color_scheme="indigo",
                        cursor="pointer",
                    ),
                    align_items="start",
                    width="100%",
                ),
                # Conexión con la lógica de autenticación de Reflex
                on_submit=reflex_local_auth.RegistrationState.handle_registration,
                width="100%",
            ),
            
            rx.hstack(
                rx.text("¿Ya tienes cuenta?"),
                rx.link("Inicia sesión", href="/login", color_scheme="indigo"),
                margin_top="16px",
                size="2",
            ),
            
            padding="40px",
            border=f"1px solid {rx.color('gray', 4)}",
            border_radius="12px",
            background=rx.color("gray", 1),
            box_shadow="lg",
            width="400px",
        ),
        padding_top="10vh",
    )

# Para añadirlo a tu aplicación:
# app = rx.App()
# app.add_page(registro_espanol, route="/registrar")
