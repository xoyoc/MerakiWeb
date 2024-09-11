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
from MerakiWeb.dashboard.pages.index import admin
import MerakiWeb.styles.styles as style
from MerakiWeb.config.database import db
import json

from rxconfig import config

def serializacion(lista):
    result = list(lista)
    data = json.loads(json.dumps(result, default=str))
    return data

class State(rx.State):
    #resultado = db["vacancies"].find()
    #vacantes = serializacion(resultado)
    pass

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
        admin(),
    )


app = rx.App(
    stylesheets=[
    "https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,200..800;1,200..800&display=swap",
    ],
    style=style.BASE_STYLE
)
app.add_page(index, route='/')
app.add_page(admin, route='/admin')