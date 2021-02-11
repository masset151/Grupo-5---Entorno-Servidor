# Generated by Django 2.2.5 on 2021-02-11 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id_publicacion', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('hora', models.DateTimeField(auto_now=True)),
                ('lugar', models.CharField(max_length=300)),
                ('archivo', models.URLField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='ConsultarPublicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicacion.Publicacion')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.Usuario')),
            ],
        ),
    ]