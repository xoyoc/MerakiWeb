import reflex as rx
import MerakiWeb.styles.styles as style

def service() -> rx.Component:
    return rx.container(
        rx.heading("Servicios", size="8", margin_y=".5em"),
        rx.flex(
            rx.card(
                rx.box(
                    rx.icon("stethoscope", color=style.COLOR_MERAKI),
                    rx.heading("Consultoría", size="1"),
                    rx.text("Estrategias a medida para tu empresa.", color="black"),
                ),
                size="2",
            ),
            rx.card(
                rx.box(
                    rx.icon("presentation", color=style.COLOR_MERAKI),
                    rx.heading("Capacitación", size="1"),
                    rx.text("Cursos y talleres para el desarrollo de habilidades.", color="black"),
                ),
                size="2",
            ),
            rx.card(
                rx.box(
                    rx.icon("square-arrow-out-up-right", color=style.COLOR_MERAKI),
                    rx.heading("Outsourcing", size="1"),
                    rx.text("Gestión de procesos de negocio externalizados.", color="black"),
                ),
                size="2",               
            ),
            rx.card(
                rx.box(
                    rx.icon("cpu", color=style.COLOR_MERAKI),
                    rx.heading("Tecnología", size="1"),
                    rx.text("Soluciones tecnológicas para la gestión del talento.", color="black"),
                ), 
                size="2",               
            ),
        spacing="2",
        ),
        margin_y=".5em",
    )