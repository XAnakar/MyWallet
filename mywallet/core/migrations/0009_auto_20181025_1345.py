# Generated by Django 2.1.2 on 2018-10-25 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0008_investimento_id_moeda'),
    ]

    operations = [
        migrations.AddField(
            model_name='despesa',
            name='criacao',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='despesa',
            name='custo',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='despesa',
            name='id_moeda',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Moeda'),
        ),
        migrations.AddField(
            model_name='despesa',
            name='id_tipoDespesa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.TipoDespesa'),
        ),
        migrations.AddField(
            model_name='despesa',
            name='id_usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
