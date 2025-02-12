import asyncio

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from telegram import Bot

from theatre.models import Reservation

MY_TOKEN = settings.TELEGRAM_BOT_API_KEY
CHAT_ID = settings.CHAT_ID


async def async_send_telegram_notification(chat_id, message):
    """
    Asynchronous function to send a message via Telegram bot.
    """
    bot = Bot(token=MY_TOKEN)
    await bot.send_message(chat_id=chat_id, text=message)


def send_telegram_notification(chat_id, message):
    """
    Wrapper to run the async function in an asyncio loop.
    """
    asyncio.run(async_send_telegram_notification(chat_id, message))


@receiver(post_save, sender=Reservation)
def notify_new_reservation(sender, instance, created, **kwargs):
    if created:
        message = f"New reservation created: {instance.user_id.email} - {instance.reservation.created_at}"
        send_telegram_notification(chat_id=CHAT_ID, message=message)
