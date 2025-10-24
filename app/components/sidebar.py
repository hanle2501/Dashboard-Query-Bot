import reflex as rx
from app.states.base_state import BaseState


def nav_item(icon: str, text: str, href: str, is_active: bool) -> rx.Component:
    """A single navigation item in the sidebar."""
    return rx.el.a(
        rx.icon(icon, class_name="h-5 w-5"),
        rx.el.span(text),
        href=href,
        class_name=rx.cond(
            is_active,
            "flex items-center gap-3 rounded-lg bg-orange-100 px-3 py-2 text-orange-600 transition-all hover:text-orange-700",
            "flex items-center gap-3 rounded-lg px-3 py-2 text-gray-500 transition-all hover:text-gray-900",
        ),
    )


def sidebar() -> rx.Component:
    """The main sidebar component for navigation."""
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    rx.icon("bot", class_name="h-8 w-8 text-orange-600"),
                    rx.el.span("ChatDash", class_name="sr-only"),
                    href="/",
                    class_name="flex items-center gap-2 font-semibold text-lg",
                ),
                class_name="flex h-16 items-center border-b px-6",
            ),
            rx.el.nav(
                nav_item(
                    "message-square",
                    "Chat",
                    "/",
                    is_active=BaseState.router.page.path == "/",
                ),
                nav_item(
                    "layout-dashboard",
                    "Dashboard",
                    "/dashboard",
                    is_active=BaseState.router.page.path == "/dashboard",
                ),
                nav_item("settings", "Settings", "#", is_active=False),
                class_name="flex-1 grid items-start p-4 text-sm font-medium",
            ),
            class_name="flex-1 overflow-auto py-2",
        ),
        class_name="hidden border-r bg-gray-100/40 md:flex md:flex-col w-64",
    )