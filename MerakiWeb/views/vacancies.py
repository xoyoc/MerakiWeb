import reflex as rx
import MerakiWeb.styles.styles as style

def vacancies() -> rx.Component:
    return rx.container(
        rx.center(
            rx.heading("Únete a nuestro equipo", size="8", margin_y=".5em"),
        ),
        rx.center(
            rx.text("¿Listo para hacer la diferencia? Explora las oportunidades de carrera con nosotros."),
        ),
        rx.center(
            rx.button("Ver Vacantes", style=style.buttonMeraki, margin_y="2em"),
        ),
        rx.flex(
            rx.card(
                rx.box(
                    rx.image(src="/nuestra_cultura.png"),
                    rx.text("Nuestra Cultura", size="3"),
                    rx.text("Fomentamos un ambiente de trabajo inclusivo y dinámico.", color="black"),
                ),
                width="100%",
                size="3",
                variant="ghost",
                margin_x="1px",
            ),
            rx.card(
                rx.box(
                    rx.image(src="/nuestros_proyectos.png"),
                    rx.text("Nuestros Proyectos", size="3"),
                    rx.text("Proyectos innovadores que transforman industrias.", color="black"),
                ),
                width="100%",
                size="3",
                variant="ghost",
                margin_x="1px",
            ),
            rx.card(
                rx.box(
                    rx.image(src="/nuestra_cultura.png"),
                    rx.text("Nuestro Impacto", size="3"),
                    rx.text("Comprometidos con el desarrollo social y empresarial.", color="black"),
                ),
                width="100%",
                size="3",
                variant="ghost",
                margin_x="1px",
            ),                        
        ),
        margin_y="2em",
    )