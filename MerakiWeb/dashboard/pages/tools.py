import reflex as rx

from MerakiWeb.dashboard.navigation import navbar
from MerakiWeb.dashboard.template import template

@template
def tools() -> rx.Component:
    return rx.box(
            navbar(heading="Tools"),
            rx.box(
                rx.text("placeholder"),
                margin_top="calc(50px + 2em)",
                padding="2em",
            ),
            padding_left="250px",
        )
