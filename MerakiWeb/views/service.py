import reflex as rx
import MerakiWeb.styles.styles as style

def service() -> rx.Component:
    return rx.container(
        rx.heading("Servicios", size="8", margin_y=".5em"),
        rx.flex(
            rx.card(
                rx.box(
                    rx.icon("stethoscope", color=style.COLOR_MERAKI, margin_y=".5em"),
                    rx.heading("Consultoría", size="3"),
                    rx.text("Estrategias a medida para tu empresa.", color="black"),
                ),
                width="100%",
                size="3",
            ),
            rx.card(
                rx.box(
                    rx.icon("presentation", color=style.COLOR_MERAKI, margin_y=".5em"),
                    rx.heading("Capacitación", size="3"),
                    rx.text("Cursos y talleres para el desarrollo de habilidades.", color="black"),
                ),
                width="100%",
                size="3",
            ),
            rx.card(
                rx.box(
                    rx.icon("square-arrow-out-up-right", color=style.COLOR_MERAKI, margin_y=".5em"),
                    rx.heading("Outsourcing", size="3"),
                    rx.text("Gestión de procesos de negocio externalizados.", color="black"),
                ),
                width="100%",
                size="3",               
            ),
            rx.card(
                rx.box(
                    rx.icon("cpu", color=style.COLOR_MERAKI, margin_y=".5em"),
                    rx.heading("Tecnología", size="3"),
                    rx.text("Soluciones tecnológicas para la gestión del talento.", color="black"),
                ),
                width="100%", 
                size="3",               
            ),
        spacing="2",
        width="100%",
        ),
        margin_y=".5em",
    )