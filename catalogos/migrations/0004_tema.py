# Generated by Django 3.2.8 on 2021-10-16 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0003_fotos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(verbose_name='descripción')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='temas_curso', to='catalogos.curso')),
                ('fotos', models.ManyToManyField(related_name='fotos', to='catalogos.Fotos')),
            ],
        ),
    ]