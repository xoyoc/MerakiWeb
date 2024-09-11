"""The main index page."""

import reflex as rx
from MerakiWeb.dashboard.data import (
    line_chart_data,
    lines,
    pie_chart_data,
    area_chart_data,
    areas,
    stat_card_data,
    tabular_data,
)
from MerakiWeb.dashboard.graphs import (
    area_chart,
    line_chart,
    pie_chart,
    stat_card,
    table,
)
from MerakiWeb.dashboard.navigation import navbar
from MerakiWeb.dashboard.template import template

# Content in a grid layout.


def content_grid():
    return rx.grid(
        *[
            rx.box(stat_card(*c), col_span=1, row_span=1)
            for c in stat_card_data
        ],
        rx.box(
            line_chart(data=line_chart_data, data_key="name", lines=lines),
            col_span=3,
            row_span=2,
        ),
        rx.box(
            pie_chart(data=pie_chart_data, data_key="value", name_key="name"),
            row_span=2,
            col_span=1,
        ),
        rx.box(table(tabular_data=tabular_data), col_span=4, row_span=2),
        rx.box(
            area_chart(data=area_chart_data, data_key="name", areas=areas),
            col_span=3,
            row_span=2,
        ),
        template_columns="repeat(4, 1fr)",
        width="100%",
        gap=4,
        row_gap=8,
    )


@template
def admin() -> rx.Component:
    return rx.box(
            navbar(heading="Dashboard"),
            rx.box(
                content_grid(),
                margin_top="calc(50px + 2em)",
                padding="2em",
            ),
            padding_left="250px",
        )
