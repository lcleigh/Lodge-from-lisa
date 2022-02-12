# Generated by Django 4.0.1 on 2022-02-07 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lodge', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=240)),
                ('last_name', models.CharField(max_length=240)),
                ('email', models.CharField(blank=True, max_length=240, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='booking_rooms',
            name='booking_id',
        ),
        migrations.RemoveField(
            model_name='booking_rooms',
            name='room_id',
        ),
        migrations.RemoveField(
            model_name='bookings',
            name='customer_id',
        ),
        migrations.DeleteModel(
            name='Bulk_discounts',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='booking_id',
        ),
        migrations.DeleteModel(
            name='Discount_type',
        ),
        migrations.RemoveField(
            model_name='roles',
            name='allowed_actions',
        ),
        migrations.RemoveField(
            model_name='rooms',
            name='room_type',
        ),
        migrations.DeleteModel(
            name='Seasonal_discounts',
        ),
        migrations.RemoveField(
            model_name='users',
            name='role_id',
        ),
        migrations.RemoveField(
            model_name='checkin',
            name='booking_id',
        ),
        migrations.AlterField(
            model_name='checkin',
            name='checkin_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Actions',
        ),
        migrations.DeleteModel(
            name='Booking_rooms',
        ),
        migrations.DeleteModel(
            name='Bookings',
        ),
        migrations.DeleteModel(
            name='Checkout',
        ),
        migrations.DeleteModel(
            name='Customers',
        ),
        migrations.DeleteModel(
            name='Roles',
        ),
        migrations.DeleteModel(
            name='Room_type',
        ),
        migrations.DeleteModel(
            name='Rooms',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.AddField(
            model_name='customer',
            name='checkins',
            field=models.ManyToManyField(blank=True, related_name='customers', to='Lodge.Checkin'),
        ),
    ]