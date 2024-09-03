import reflex as rx
import MerakiWeb.styles.styles as style

def menu()-> rx.Component:
    return rx.hstack(
        rx.flex(
            rx.link("Inicio"),
            rx.link("Servicios"),
            rx.link("Sobre Nosotros"),
            rx.link("Blog"),
            rx.link("Contacto"),
            width="100%",
            margin_y="1em",
            justify="between",
        ),
    )