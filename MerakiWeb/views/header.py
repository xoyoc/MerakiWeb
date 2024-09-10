import reflex as rx
import MerakiWeb.styles.styles as style

def header() -> rx.Component:
    return rx.container(
        rx.hstack(
            rx.flex(
                rx.heading("Meraki"),
                rx.spacer(),
                rx.flex(
                    rx.button("Contacto", style=style.buttonMeraki),
                    rx.avatar(src="/avatar.png", radius="full"),
                    spacing="3",
                    justify="between",
                ),
                width="100%",
            ),
        ),
    )