import reflex as rx
import MerakiWeb.styles.styles as style

def our_values() -> rx.Component:
    return rx.container(
        rx.heading("Nuestros Valores", size="8"),
        rx.text("Conoce los pilares que sustentan nuestra filosofía de trabajo.", margin_y=".5em",),
        rx.flex(
            rx.card(
                rx.box(
                    rx.icon("brain-circuit", color=style.COLOR_MERAKI, margin_y=".5em"),
                    rx.heading("Integridad", size="3"),
                    rx.text("Actuamos con honestidad y transparencia.", color="black"),
                ),
            ),
            rx.card(
                rx.box(
                    rx.icon("brain-cog", color=style.COLOR_MERAKI, margin_y=".5em"),
                    rx.heading("Innovación", size="3"),
                    rx.text("Buscamos constantemente nuevas soluciones.", color="black"),
                ),
            ),
            rx.card(
                rx.box(
                    rx.icon("handshake", color=style.COLOR_MERAKI, margin_y=".5em"),
                    rx.heading("Compromiso", size="3"),
                    rx.text("Estamos dedicados al éxito de nuestros clientes.", color="black"),
                ),                
            ),
        spacing="2",
        ),
        margin_y=".5em",
    )