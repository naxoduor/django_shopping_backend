# Generated by Django 3.0.1 on 2019-12-27 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='attribute',
            fields=[
                ('attribute_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'attribute',
            },
        ),
        migrations.CreateModel(
            name='attribute_value',
            fields=[
                ('attribute_value_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=100)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.attribute')),
            ],
            options={
                'verbose_name_plural': 'attribute_value',
            },
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('category_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'verbose_name_plural': 'category',
            },
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('customer_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=200)),
                ('credit_card', models.TextField(blank=True, null=True)),
                ('address_1', models.CharField(blank=True, max_length=100, null=True)),
                ('address_2', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('region', models.CharField(blank=True, max_length=100, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('day_phone', models.CharField(blank=True, max_length=100, null=True)),
                ('eve_phone', models.CharField(blank=True, max_length=100, null=True)),
                ('mob_phone', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'customer',
            },
        ),
        migrations.CreateModel(
            name='department',
            fields=[
                ('department_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'verbose_name_plural': 'department',
            },
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('product_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discounted_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.CharField(blank=True, max_length=150, null=True)),
                ('image_2', models.CharField(blank=True, max_length=150, null=True)),
                ('thumbnail', models.CharField(blank=True, max_length=150, null=True)),
                ('display', models.SmallIntegerField(default='0')),
            ],
            options={
                'verbose_name_plural': 'product',
            },
        ),
        migrations.CreateModel(
            name='shipping_region',
            fields=[
                ('shipping_region_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('shipping_region', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'shipping_region',
            },
        ),
        migrations.CreateModel(
            name='tax',
            fields=[
                ('tax_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('tax_type', models.CharField(max_length=100)),
                ('tax_percentage', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name_plural': 'tax',
            },
        ),
        migrations.CreateModel(
            name='shopping_cart',
            fields=[
                ('item_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('cart_id', models.CharField(max_length=32)),
                ('attributes', models.CharField(max_length=1000)),
                ('quantity', models.IntegerField()),
                ('buy_now', models.BooleanField(default=True)),
                ('added_on', models.DateTimeField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.product')),
            ],
            options={
                'verbose_name_plural': 'shopping_cart',
            },
        ),
        migrations.CreateModel(
            name='shipping',
            fields=[
                ('shipping_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('shipping_type', models.CharField(max_length=100)),
                ('shipping_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('shipping_region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.shipping_region')),
            ],
            options={
                'verbose_name_plural': 'shipping',
            },
        ),
        migrations.CreateModel(
            name='review',
            fields=[
                ('review_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('review', models.TextField()),
                ('rating', models.SmallIntegerField()),
                ('created_on', models.DateTimeField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.product')),
            ],
            options={
                'verbose_name_plural': 'review',
            },
        ),
        migrations.CreateModel(
            name='product_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.category')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.product')),
            ],
            options={
                'verbose_name_plural': 'product_category',
            },
        ),
        migrations.CreateModel(
            name='product_attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.attribute_value')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.product')),
            ],
            options={
                'verbose_name_plural': 'product_attribute',
            },
        ),
        migrations.CreateModel(
            name='orders',
            fields=[
                ('order_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('total_amount', models.DecimalField(decimal_places=2, default='0.00', max_digits=10)),
                ('created_on', models.DateTimeField()),
                ('shipped_on', models.DateTimeField(null=True)),
                ('status', models.IntegerField()),
                ('comments', models.CharField(max_length=255, null=True)),
                ('auth_code', models.CharField(max_length=50, null=True)),
                ('reference', models.CharField(max_length=50, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shopping.customer')),
                ('shipping', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shopping.shipping')),
                ('tax', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shopping.tax')),
            ],
            options={
                'verbose_name_plural': 'orders',
            },
        ),
        migrations.CreateModel(
            name='order_detail',
            fields=[
                ('item_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('product_id', models.IntegerField()),
                ('attributes', models.CharField(max_length=1000)),
                ('product_name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('unit_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('orders', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.orders')),
            ],
            options={
                'verbose_name_plural': 'order_detail',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='shipping_region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.shipping_region'),
        ),
        migrations.AddField(
            model_name='category',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.department'),
        ),
        migrations.CreateModel(
            name='audit',
            fields=[
                ('audit_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField()),
                ('message', models.TextField()),
                ('code', models.IntegerField()),
                ('orders', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.orders')),
            ],
            options={
                'verbose_name_plural': 'audit',
            },
        ),
    ]