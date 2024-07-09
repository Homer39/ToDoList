import uuid
from django.conf import settings
from django.db import models

NULLABLE = {
    'null': True,
    'blank': True
}


class Task(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name="Пользователь",
                              **NULLABLE)

    title = models.CharField(max_length=100, verbose_name='Задача')
    description = models.TextField(verbose_name='Описание задачи', **NULLABLE)
    is_complete = models.BooleanField(default=False, verbose_name='Выполнено')
    tag = models.ManyToManyField("Tag", verbose_name='Тег')

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"Task - {self.title}"

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"


class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название тега')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
