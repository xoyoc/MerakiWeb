import reflex as rx
import MerakiWeb.styles.styles as style

def contact() -> rx.Component:
    return rx.container(
        rx.center(
            rx.text("Contacto", color="white", size="9"),
            margin_top="5em",
        ),
        rx.center(
            rx.text("Hablemos sobre cómo podemos ayudarte a alcanzar tus objetivos.", color="white"),
            margin_y="1em",
        ),
        rx.center(
            rx.input(
                        placeholder="Ingresa tu correo electrónico",
                        variant="classic",
                        width="25em",
                        height="3.5em",
                        margin_right="1em",
                    ),
            rx.button("Enviar Mensaje", style=style.buttonMeraki),
        ),
        background="center/cover url('/contacto.png')",
        width="100%",
        height="450px",
    )