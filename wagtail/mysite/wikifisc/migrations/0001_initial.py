# Generated by Django 3.0.10 on 2020-10-20 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0052_pagelogentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wiki',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('subtitle', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Flex Page',
                'verbose_name_plural': 'Flex Pages',
            },
            bases=('wagtailcore.page',),
        ),
    ]
