import reflex as rx

from rxconfig import config

class State(rx.State):
    """The app state."""

    ...

@rx.page(route="/", title="Wesley Wong")
def index():
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Wesley Wong", size="9"),
            rx.text(
                "Software Engineering @ ",
                rx.code("San Jose State University"),
                size="5",
            ),
            rx.button(
                "About me",
                on_click=rx.redirect("/about"),
            ),
            rx.button(
                "See my projects ;)",
                on_click=rx.redirect("/projects"),
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )

def about():
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("I am a Software Engineering major @ San Jose State University", size="8"),
            rx.text(
                "I'm a college student passionate about software engineering, with a focus on backend development. On track to graduate December 2026",
                size="5",
            ),
            rx.text(
                "I'm an officer in SJSU's Software and Computer Engineering club.",
                size="3",
            ),
            rx.text(
                "I'm eager to learn more about software engineering and have a strong interest in roles that challenge me to solve complex problems.",
                size="3",
            ),
            rx.text(
                "I'm also currently seeking internships!!!",
                size="3",
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )

def projects():
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("My projects", size="8", spacing="6"),
            rx.flex(
                rx.card(
                    rx.heading("SCE-TV", size="3"),
                    rx.link("Github", href="https://github.com/SCE-Development/sce-tv"),
                    ),
                rx.card(
                    rx.heading("SCE-TV", size="3"),
                    rx.link("Github", href="https://github.com/SCE-Development/sce-tv"),
                ),
                rx.card(
                    rx.heading("SCE-TV", size="3"),
                    rx.link("Github", href="https://github.com/SCE-Development/sce-tv"),
                ),
                rx.card(
                    rx.heading("SCE-TV", size="3"),
                    rx.link("Github", href="https://github.com/SCE-Development/sce-tv"),
                ),
                rx.card(
                    rx.heading("SCE-TV", size="3"),
                    rx.link("Github", href="https://github.com/SCE-Development/sce-tv"),
                ),
                spacing="2",
                width="100%",
                padding="5em"
            )   
        ),
    )


app = rx.App()
app.add_page(index)
app.add_page(about, route='/about')
app.add_page(projects, route='/projects')
