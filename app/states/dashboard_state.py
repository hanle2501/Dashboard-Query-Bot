import reflex as rx
import random
from typing import TypedDict


class Metric(TypedDict):
    title: str
    value: str
    change: str
    change_type: str
    icon: str


class RevenueData(TypedDict):
    month: str
    revenue: int


class CategoryData(TypedDict):
    category: str
    sales: int


class MultiMetricData(TypedDict):
    month: str
    users: int
    sessions: int
    page_views: int


class DashboardState(rx.State):
    """Manages the data and state for the dashboard page."""

    metrics: list[Metric] = [
        {
            "title": "Total Users",
            "value": "10,234",
            "change": "+12.5%",
            "change_type": "increase",
            "icon": "users",
        },
        {
            "title": "Revenue",
            "value": "$45,231.89",
            "change": "+8.1%",
            "change_type": "increase",
            "icon": "dollar-sign",
        },
        {
            "title": "Engagement",
            "value": "78.9%",
            "change": "-1.2%",
            "change_type": "decrease",
            "icon": "activity",
        },
        {
            "title": "Growth",
            "value": "+3.4%",
            "change": "+0.5%",
            "change_type": "increase",
            "icon": "trending-up",
        },
    ]
    revenue_data: list[RevenueData] = [
        {"month": "Jan", "revenue": random.randint(1000, 5000)},
        {"month": "Feb", "revenue": random.randint(1500, 6000)},
        {"month": "Mar", "revenue": random.randint(2000, 7000)},
        {"month": "Apr", "revenue": random.randint(2500, 8000)},
        {"month": "May", "revenue": random.randint(3000, 9000)},
        {"month": "Jun", "revenue": random.randint(3500, 10000)},
    ]
    category_data: list[CategoryData] = [
        {"category": "Electronics", "sales": random.randint(100, 1000)},
        {"category": "Clothing", "sales": random.randint(100, 1000)},
        {"category": "Books", "sales": random.randint(100, 1000)},
        {"category": "Home Goods", "sales": random.randint(100, 1000)},
        {"category": "Toys", "sales": random.randint(100, 1000)},
    ]
    multi_metric_data: list[MultiMetricData] = [
        {"month": "Jan", "users": 120, "sessions": 200, "page_views": 450},
        {"month": "Feb", "users": 150, "sessions": 250, "page_views": 550},
        {"month": "Mar", "users": 180, "sessions": 300, "page_views": 650},
        {"month": "Apr", "users": 220, "sessions": 350, "page_views": 750},
        {"month": "May", "users": 250, "sessions": 400, "page_views": 850},
        {"month": "Jun", "users": 280, "sessions": 450, "page_views": 950},
    ]