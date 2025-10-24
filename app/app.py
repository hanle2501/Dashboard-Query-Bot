import reflex as rx
from app.components.sidebar import sidebar
from app.components.chat import chat_interface
from app.components.dashboard import dashboard_page


def index() -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.div(chat_interface(), class_name="flex flex-col flex-1"),
        class_name="grid h-screen w-full md:grid-cols-[256px_1fr] font-['Lato']",
    )


def dashboard() -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.div(dashboard_page(), class_name="flex flex-col flex-1"),
        class_name="grid h-screen w-full md:grid-cols-[256px_1fr] font-['Lato']",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index)
app.add_page(dashboard, route="/dashboard")