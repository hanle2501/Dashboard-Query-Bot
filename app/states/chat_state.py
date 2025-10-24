import reflex as rx
from typing import TypedDict, Literal, Any
from app.states.dashboard_state import DashboardState
import asyncio
import random


class Message(TypedDict):
    role: Literal["user", "bot"]
    content: str
    chart_type: Literal["none", "revenue", "category", "multi_metric"]


class ChatState(rx.State):
    """Manages the chat history and user input."""

    messages: list[Message] = [
        {
            "role": "bot",
            "content": "Hello! I'm your data assistant. How can I help you with the dashboard today? Ask me about revenue, sales by category, or user activity.",
            "chart_type": "none",
        }
    ]
    is_processing: bool = False

    @rx.event
    async def handle_submit(self, form_data: dict):
        """Handle user message submission."""
        user_question = form_data.get("user_input", "").strip()
        if not user_question:
            return
        self.messages.append(
            {"role": "user", "content": user_question, "chart_type": "none"}
        )
        self.is_processing = True
        yield
        yield ChatState.get_bot_response(user_question)

    @rx.event(background=True)
    async def get_bot_response(self, question: str):
        """Simulate generating a bot response with chart integration."""
        await asyncio.sleep(1.5)
        q_lower = question.lower()
        response_content = ""
        chart_type: Literal["none", "revenue", "category", "multi_metric"] = "none"
        if "revenue" in q_lower or "trend" in q_lower:
            response_content = "Here are the revenue trends for the past six months. It looks like there has been steady growth, with a significant increase in the last quarter."
            chart_type = "revenue"
        elif "category" in q_lower or "sales by" in q_lower or "comparison" in q_lower:
            response_content = "This chart shows the sales distribution across different product categories. Electronics and Toys are the top performers this period."
            chart_type = "category"
        elif "user" in q_lower or "activity" in q_lower or "session" in q_lower:
            response_content = "Here's a look at user activity. We can see a consistent rise in new users and page views, indicating healthy engagement and platform growth."
            chart_type = "multi_metric"
        else:
            responses = [
                f"I've looked into '{question}'. Here's what I found...",
                f"Let me check the data for '{question}'. One moment...",
                "I'm not sure how to answer that. Try asking about revenue, categories, or user activity.",
            ]
            response_content = random.choice(responses)
            chart_type = "none"
        async with self:
            self.messages.append(
                {"role": "bot", "content": response_content, "chart_type": chart_type}
            )
            self.is_processing = False