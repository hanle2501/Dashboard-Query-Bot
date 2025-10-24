import reflex as rx
from app.states.dashboard_state import DashboardState

TOOLTIP_PROPS = {
    "content_style": {
        "background": "white",
        "border_color": "#E4E4E7",
        "border_radius": "0.5rem",
        "font_size": "0.875rem",
        "box_shadow": "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1)",
    },
    "label_style": {"color": "#18181B"},
    "separator": "",
}


def metric_card(metric: dict) -> rx.Component:
    """A card displaying a single key metric."""
    return rx.el.div(
        rx.el.div(
            rx.el.h3(metric["title"], class_name="text-sm font-medium text-gray-500"),
            rx.icon(metric["icon"], class_name="h-4 w-4 text-gray-400"),
            class_name="flex items-center justify-between",
        ),
        rx.el.div(
            rx.el.p(metric["value"], class_name="text-2xl font-bold"),
            rx.el.p(
                metric["change"],
                class_name=rx.cond(
                    metric["change_type"] == "increase",
                    "text-sm text-green-500",
                    "text-sm text-red-500",
                ),
            ),
            class_name="flex items-baseline gap-2",
        ),
        class_name="bg-white p-6 rounded-lg border border-gray-200 shadow-sm",
    )


def revenue_chart() -> rx.Component:
    """An area chart for displaying revenue trends."""
    return rx.el.div(
        rx.el.h3("Revenue Trends", class_name="text-lg font-semibold mb-4"),
        rx.recharts.area_chart(
            rx.recharts.cartesian_grid(
                horizontal=True, stroke_dasharray="3 3", class_name="text-gray-200"
            ),
            rx.recharts.graphing_tooltip(**TOOLTIP_PROPS),
            rx.recharts.x_axis(
                data_key="month", tick_line=False, axis_line=False, class_name="text-xs"
            ),
            rx.recharts.y_axis(tick_line=False, axis_line=False, class_name="text-xs"),
            rx.recharts.area(
                data_key="revenue",
                type_="natural",
                stroke="#f97316",
                fill="#ffedd5",
                stroke_width=2,
                dot=False,
            ),
            data=DashboardState.revenue_data,
            height=300,
            class_name="[&_.recharts-tooltip-cursor]:fill-orange-100",
        ),
        class_name="bg-white p-6 rounded-lg border border-gray-200 shadow-sm",
    )


def category_chart() -> rx.Component:
    """A bar chart for displaying sales by category."""
    return rx.el.div(
        rx.el.h3("Sales by Category", class_name="text-lg font-semibold mb-4"),
        rx.recharts.bar_chart(
            rx.recharts.cartesian_grid(
                vertical=False, stroke_dasharray="3 3", class_name="text-gray-200"
            ),
            rx.recharts.graphing_tooltip(**TOOLTIP_PROPS),
            rx.recharts.x_axis(
                data_key="category",
                type_="category",
                tick_line=False,
                axis_line=False,
                class_name="text-xs",
            ),
            rx.recharts.y_axis(tick_line=False, axis_line=False, class_name="text-xs"),
            rx.recharts.bar(data_key="sales", fill="#fb923c", radius=[4, 4, 0, 0]),
            data=DashboardState.category_data,
            height=300,
            bar_category_gap=20,
            class_name="[&_.recharts-tooltip-cursor]:fill-orange-100",
        ),
        class_name="bg-white p-6 rounded-lg border border-gray-200 shadow-sm",
    )


def multi_metric_chart() -> rx.Component:
    """A composed chart for multiple metrics."""
    return rx.el.div(
        rx.el.h3("User Activity Trends", class_name="text-lg font-semibold mb-4"),
        rx.recharts.composed_chart(
            rx.recharts.cartesian_grid(
                stroke_dasharray="3 3", class_name="text-gray-200"
            ),
            rx.recharts.graphing_tooltip(**TOOLTIP_PROPS),
            rx.recharts.x_axis(
                data_key="month", tick_line=False, axis_line=False, class_name="text-xs"
            ),
            rx.recharts.y_axis(tick_line=False, axis_line=False, class_name="text-xs"),
            rx.recharts.area(data_key="page_views", fill="#fed7aa", stroke="#f97316"),
            rx.recharts.bar(data_key="sessions", fill="#fb923c"),
            rx.recharts.line(data_key="users", stroke="#ea580c"),
            data=DashboardState.multi_metric_data,
            height=300,
            class_name="[&_.recharts-tooltip-cursor]:fill-orange-100",
        ),
        class_name="bg-white p-6 rounded-lg border border-gray-200 shadow-sm",
    )


def dashboard_page() -> rx.Component:
    """The main dashboard page component."""
    return rx.el.main(
        rx.el.div(
            rx.el.div(
                rx.el.h1("Dashboard", class_name="text-2xl font-bold"),
                class_name="mb-6",
            ),
            rx.el.div(
                rx.foreach(DashboardState.metrics, metric_card),
                class_name="grid gap-6 md:grid-cols-2 lg:grid-cols-4 mb-6",
            ),
            rx.el.div(
                revenue_chart(),
                category_chart(),
                class_name="grid gap-6 md:grid-cols-2 mb-6",
            ),
            rx.el.div(multi_metric_chart(), class_name="grid gap-6"),
            class_name="p-6",
        ),
        class_name="flex-1 bg-gray-50 overflow-y-auto",
    )