import reflex as rx
import MerakiWeb.styles.styles as style

def our_values() -> rx.Component:
    return rx.container(
        rx.heading("Nuestros Valores", size="8"),
        rx.text("Conoce los pilares que sustentan nuestra filosofía de trabajo.", margin_y=".5em",),
        rx.flex(
            rx.card(
                rx.box(
                    rx.icon("brain-circuit", color=style.COLOR_MERAKI),
                    rx.heading("Integridad", size="1"),
                    rx.text("Actuamos con honestidad y transparencia.", color="black"),
                ),
            ),
            rx.card(
                rx.box(
                    rx.icon("brain-cog", color=style.COLOR_MERAKI),
                    rx.heading("Innovación", size="1"),
                    rx.text("Buscamos constantemente nuevas soluciones.", color="black"),
                ),
            ),
            rx.card(
                rx.box(
                    rx.icon("handshake", color=style.COLOR_MERAKI),
                    rx.heading("Compromiso", size="1"),
                    rx.text("Estamos dedicados al éxito de nuestros clientes.", color="black"),
                ),                
            ),
        spacing="2",
        ),
        margin_y=".5em",
    )