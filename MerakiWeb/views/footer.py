import reflex as rx
import datetime
import MerakiWeb.styles.styles as style

def footer() -> rx.Component:
    return rx.container(
        rx.hstack(
            rx.flex(
                rx.center(
                    rx.icon("facebook", color=style.COLOR_MERAKI),
                    rx.icon("twitter", color=style.COLOR_MERAKI),
                    rx.icon("instagram", color=style.COLOR_MERAKI),
                ),
                rx.center(
                    rx.text(f"© {datetime.date.today().year} meraki. Todos los derechos reservados."),
                ),
                direction="column",
                width="100%",
            ),
        ),
    )