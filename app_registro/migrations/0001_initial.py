from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conferencista',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('experiencia', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
                ('correo', models.EmailField(max_length=254)),
                ('twitter', models.CharField(blank=True, max_length=35, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Conferencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=35)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('conferencista', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.CASCADE, to='app_registro.conferencista')),
            ],
        ),
    ]
