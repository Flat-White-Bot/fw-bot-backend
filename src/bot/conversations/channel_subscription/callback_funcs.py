import os
from functools import wraps

from telegram import ChatMember, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

CHANNEL_ID = os.getenv("CHANNEL")


def require_subscription(func):
    @wraps(func)
    async def wrapper(
        update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs
    ):
        await update.effective_message.edit_reply_markup()
        chat_member = await context.bot.get_chat_member(
            chat_id=CHANNEL_ID, user_id=update.effective_user.id
        )
        if chat_member and chat_member.status in [
            ChatMember.MEMBER,
            ChatMember.ADMINISTRATOR,
            ChatMember.OWNER,
        ]:
            return await func(update, context, *args, **kwargs)
        else:
            await update.effective_message.reply_text(
                f"Пожалуйста, подпишитесь на наш канал, чтобы продолжить."
                f'\n▶ <a href="https://t.me/{CHANNEL_ID.replace("@", "")}">'
                "Flat White Media | медиа о коливингах в Telegram</a>"
                "\nВы не можете продолжить, пока не выполните подписку.",
                reply_markup=InlineKeyboardMarkup.from_button(
                    InlineKeyboardButton(
                        callback_data=update.callback_query.data, text="Подписался 🤝"
                    )
                ),
            )
            return None

    return wrapper
