# Generated by Django 5.0.6 on 2024-06-17 14:25

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [
        ("mailing", "0001_initial"),
        ("mailing", "0002_alter_mailing_options"),
        ("mailing", "0003_mailing_image"),
        ("mailing", "0004_mailing_is_sended"),
        ("mailing", "0005_remove_mailing_is_sended_mailing_is_sent"),
        ("mailing", "0006_remove_mailing_is_sent_mailing_status_and_more"),
    ]

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Mailing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "text",
                    models.TextField(
                        help_text=(
                            "Здесь можно использовать некоторые теги HTML "
                            '(<a href="https://core.telegram.org/bots/api#html-style">'
                            "https://core.telegram.org/bots/api#html-style</a>). "
                            "Например, <code>&lt;b&gt;жирный текст&lt;/b&gt;</code>. "
                            "А также вставлять эмодзи 😊."
                        ),
                        max_length=1024,
                        verbose_name="Текст сообщения",
                    ),
                ),
                (
                    "send_date",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        help_text=(
                            "Наличие рассылки проверяется каждый час, поэтому, "
                            "если выставлено 12:34, рассылка начнётся в 13:00."
                        ),
                        verbose_name="Дата рассылки",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="mailings/",
                        verbose_name="Фото к сообщению",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("is_waiting", "Ждёт"),
                            ("is_sending", "Отправляется"),
                            ("is_sent", "Отправлено"),
                        ],
                        default="is_waiting",
                        max_length=10,
                        verbose_name="Статус",
                    ),
                ),
            ],
            options={
                "verbose_name": "Рассылка",
                "verbose_name_plural": "Рассылки",
            },
        ),
    ]
