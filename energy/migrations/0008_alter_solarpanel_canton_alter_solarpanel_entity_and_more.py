# Generated by Django 4.1.7 on 2023-04-05 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0007_alter_solarpanel_canton_alter_solarpanel_entity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solarpanel',
            name='canton',
            field=models.CharField(blank=True, choices=[('USK', 'Una-Sana Canton'), ('POS', 'Posavina Canton'), ('TUZ', 'Tuzla Canton'), ('ZDK', 'Zenica-Doboj Canton'), ('BPO', 'Bosnian-Podrinje Canton Goražde'), ('SBK', 'Central Bosnia Canton'), ('HN', 'Herzegovina-Neretva Canton'), ('HB', 'Herzeg-Bosnian Canton'), ('SA', 'Sarajevo Canton'), ('ZHK', 'Western Herzegovina Canton')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='solarpanel',
            name='entity',
            field=models.CharField(choices=[('RS', 'Republic of Srpska'), ('FBiH', 'Federation of Bosnia and Herzegovina'), ('BD', 'District Brcko')], default='entitet', max_length=50),
        ),
        migrations.AlterField(
            model_name='solarpanel',
            name='zone',
            field=models.CharField(blank=True, choices=[('U', 'Urban'), ('R', 'Rural')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='windpowerplant',
            name='canton',
            field=models.CharField(blank=True, choices=[('USK', 'Una-Sana Canton'), ('POS', 'Posavina Canton'), ('TUZ', 'Tuzla Canton'), ('ZDK', 'Zenica-Doboj Canton'), ('BPO', 'Bosnian-Podrinje Canton Goražde'), ('SBK', 'Central Bosnia Canton'), ('HN', 'Herzegovina-Neretva Canton'), ('HB', 'Herzeg-Bosnian Canton'), ('SA', 'Sarajevo Canton'), ('ZHK', 'Western Herzegovina Canton')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='windpowerplant',
            name='entity',
            field=models.CharField(choices=[('RS', 'Republic of Srpska'), ('FBiH', 'Federation of Bosnia and Herzegovina'), ('BD', 'District Brcko')], default='entitet', max_length=50),
        ),
        migrations.AlterField(
            model_name='windpowerplant',
            name='zone',
            field=models.CharField(blank=True, choices=[('U', 'Urban'), ('R', 'Rural')], max_length=50, null=True),
        ),
    ]