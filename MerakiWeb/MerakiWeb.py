"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from MerakiWeb.views.header import header
from MerakiWeb.views.body import body
from MerakiWeb.views.our_values import our_values
from MerakiWeb.views.service import service
from MerakiWeb.views.vacancies import vacancies
from MerakiWeb.views.contact import contact
from MerakiWeb.views.menu import menu
from MerakiWeb.views.footer import footer
import MerakiWeb.styles.styles as style

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        header(),
        rx.divider(size="4"),
        body(),
        our_values(),
        service(),
        vacancies(),
        contact(),
        menu(),
        footer(),
    )

def admin() -> rx.Component:
    return rx.container(
        header(),
        rx.text("Escritorio de administrador"),
        footer(),
    )


app = rx.App(
    stylesheets=[
    "https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,200..800;1,200..800&display=swap",
    ],
    style=style.BASE_STYLE
)
app.add_page(index, route='/')
app.add_page(admin, route='/admin')