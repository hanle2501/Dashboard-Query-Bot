import reflex as rx
from app.states.chat_state import ChatState
from app.components.dashboard import revenue_chart, category_chart, multi_metric_chart


def message_bubble(message: dict) -> rx.Component:
    """A chat message bubble that can contain text and a chart."""
    is_user = message["role"] == "user"
    return rx.el.div(
        rx.el.div(
            rx.el.p(message["content"], class_name="text-sm"),
            rx.match(
                message["chart_type"],
                ("revenue", rx.el.div(revenue_chart(), class_name="mt-4")),
                ("category", rx.el.div(category_chart(), class_name="mt-4")),
                ("multi_metric", rx.el.div(multi_metric_chart(), class_name="mt-4")),
                rx.fragment(),
            ),
            class_name=rx.cond(
                is_user,
                "rounded-xl bg-orange-500 text-white p-4 max-w-xl",
                "rounded-xl bg-gray-200 text-gray-800 p-4 max-w-xl",
            ),
        ),
        class_name=rx.cond(
            is_user, "flex justify-end w-full", "flex justify-start w-full"
        ),
    )


def chat_interface() -> rx.Component:
    """The main chat interface component."""
    return rx.el.main(
        rx.el.div(
            rx.foreach(ChatState.messages, message_bubble),
            rx.cond(
                ChatState.is_processing,
                rx.el.div(
                    rx.el.div(
                        rx.spinner(class_name="text-orange-500"),
                        class_name="rounded-xl bg-gray-200 p-3",
                    ),
                    class_name="flex justify-start w-full",
                ),
                None,
            ),
            class_name="flex-1 overflow-y-auto p-6 space-y-6",
        ),
        rx.el.div(
            rx.el.form(
                rx.el.input(
                    placeholder="Ask about your data...",
                    name="user_input",
                    class_name="flex-1 appearance-none bg-transparent border-none focus:ring-0 text-sm",
                    disabled=ChatState.is_processing,
                ),
                rx.el.button(
                    rx.icon("send", class_name="h-4 w-4"),
                    type_="submit",
                    class_name="rounded-full p-2 bg-orange-500 text-white hover:bg-orange-600 disabled:opacity-50",
                    disabled=ChatState.is_processing,
                ),
                on_submit=ChatState.handle_submit,
                reset_on_submit=True,
                class_name="relative flex-1 flex items-center",
            ),
            class_name="mx-4 mb-4 flex items-center gap-2 rounded-lg border bg-white p-2 shadow-sm",
        ),
        class_name="flex flex-col h-full",
    )