# Generated by Django 3.2.9 on 2021-11-18 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('c_name', models.CharField(max_length=30)),
                ('c_tele', models.CharField(max_length=10)),
                ('c_email', models.EmailField(max_length=254)),
                ('formality', models.CharField(choices=[('E', 'Eat now'), ('T', 'Take away')], max_length=1)),
                ('c_address', models.CharField(max_length=200, null=True)),
                ('total', models.BigIntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('D', 'Doing'), ('F', 'Finish'), ('C', 'Canceled')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('avatar', models.ImageField(upload_to='uploads/SImages')),
                ('staff_type', models.CharField(choices=[('M', 'Manager'), ('R', 'Receiption'), ('S', 'Shipper')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('E', 'Empty'), ('R', 'Reserved')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rtime', models.DateTimeField()),
                ('no_customer', models.IntegerField()),
                ('interval', models.IntegerField()),
                ('staff_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todo.staff')),
                ('table_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.table')),
                ('name',models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Foods',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('info', models.TextField(blank=True, null=True)),
                ('qty_day', models.IntegerField()),
                ('image', models.ImageField(upload_to='uploads/FImages')),
                ('price', models.BigIntegerField()),
                ('cost', models.BigIntegerField()),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.category')),
            ],
        ),
        migrations.CreateModel(
            name='Food_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('food_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.foods')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.order')),
            ],
        ),
    ]
