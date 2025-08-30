# In future, you can connect SQLite, PostgreSQL, or MongoDB here.
# For now, we’ll just keep a placeholder.

def save_chat(user_type, user_message, bot_reply):
    """Simulate saving chat logs (extend with DB later)."""
    with open("chat_logs.txt", "a", encoding="utf-8") as f:
        f.write(f"{user_type} >> {user_message}\n")
        f.write(f"Bot >> {bot_reply}\n\n")
