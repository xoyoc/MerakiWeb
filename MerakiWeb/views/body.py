import reflex as rx
import MerakiWeb.styles.styles as style

def body()-> rx.Component:
    return rx.container(
        # rx.color_mode.button(position="top-right"),
        rx.hstack(
            rx.box(
                rx.image(src="/LogoMeraki.jpeg"),
            ),
            rx.divider(orientation="vertical", size="4"),
            rx.box(
                rx.heading("Capital Humano en Acción", size="9", margin_y=".5em",),
                rx.text("Descubre cómo potenciamos el talento dentro de las organizaciones."),
                rx.flex(
                    rx.button("Nuestros Servicios", style=style.buttonMeraki),
                    rx.button("Aprende Más", style=style.buttonDefault),
                    spacing="3",
                    flex_grow="1",
                    justify="center",
                    margin_y="1em",
                ),
            ),
        ),
    )