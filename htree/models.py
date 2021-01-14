from django.db import models


class Pseudofs(models.Model):
    ffile = models.CharField(max_length=40, verbose_name='Имя файла/каталога')
    parent = models.ForeignKey(
        'self',
        verbose_name='Родительский каталог',
        blank=True,
        null=True,
        related_name='pseudofs_children',
        on_delete=models.CASCADE
    )

    is_child = models.BooleanField(default=False)

    def __str__(self):
        return str(self.Pseudofs)

    @property
    def get_parent(self):
        if not self.parent:
            return ""
        return self.parent





