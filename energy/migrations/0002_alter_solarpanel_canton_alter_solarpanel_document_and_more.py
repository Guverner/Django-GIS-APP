# Generated by Django 4.1.7 on 2023-03-20 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solarpanel',
            name='canton',
            field=models.CharField(choices=[('USK', 'Unsko-sanski'), ('POS', 'Posavski'), ('TUZ', 'Tuzlanski'), ('ZDK', 'Zeničko-dobojski'), ('BPO', 'Bosansko-podrinjski'), ('SBK', 'Srednjobosanski'), ('HN', 'Hercegovačko-neretvanski'), ('HB', 'Hercegbosanski')], max_length=50),
        ),
        migrations.AlterField(
            model_name='solarpanel',
            name='document',
            field=models.FileField(upload_to='solarpaneldocuments/'),
        ),
        migrations.AlterField(
            model_name='solarpanel',
            name='entity',
            field=models.CharField(choices=[('RS', 'Republika Srpska'), ('FBiH', 'Federacija Bosne i Hercegovine'), ('BD', 'Brčko distrikt')], max_length=50),
        ),
        migrations.AlterField(
            model_name='solarpanel',
            name='zone',
            field=models.CharField(choices=[('U', 'Urban'), ('R', 'Rural')], max_length=1),
        ),
        migrations.AlterField(
            model_name='windpowerplant',
            name='canton',
            field=models.CharField(choices=[('USK', 'Unsko-sanski'), ('POS', 'Posavski'), ('TUZ', 'Tuzlanski'), ('ZDK', 'Zeničko-dobojski'), ('BPO', 'Bosansko-podrinjski'), ('SBK', 'Srednjobosanski'), ('HN', 'Hercegovačko-neretvanski'), ('HB', 'Hercegbosanski')], max_length=50),
        ),
        migrations.AlterField(
            model_name='windpowerplant',
            name='document',
            field=models.FileField(upload_to='windpowerplantdocuments/'),
        ),
        migrations.AlterField(
            model_name='windpowerplant',
            name='entity',
            field=models.CharField(choices=[('RS', 'Republika Srpska'), ('FBiH', 'Federacija Bosne i Hercegovine'), ('BD', 'Brčko distrikt')], max_length=50),
        ),
        migrations.AlterField(
            model_name='windpowerplant',
            name='zone',
            field=models.CharField(choices=[('U', 'Urban'), ('R', 'Rural')], max_length=10),
        ),
    ]