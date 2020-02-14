from django.db import models

class department(models.Model):
    department_id = models.AutoField(auto_created=True,primary_key=True)
    name = models.CharField(max_length=100)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
    description = models.CharField(max_length=1000,null=True,blank=True)
    
    def __str__(self):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
        return self.name
    
    class Meta:
        db_table = "department"
        
class category(models.Model):
    category_id = models.AutoField(auto_created=True,primary_key=True)
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000,null=True,blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "category"
        
class product(models.Model):
    product_id = models.AutoField(auto_created=True,primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.CharField(max_length=150,null=True,blank=True)
    image_2 = models.CharField(max_length=150,null=True,blank=True)
    thumbnail = models.CharField(max_length=150,null=True,blank=True)
    display = models.SmallIntegerField(default='0')
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "product"
        
class product_category(models.Model):
    product = models.ForeignKey(product,on_delete=models.CASCADE)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "product_category"
        
class attribute(models.Model):
    attribute_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "attribute"
        
class attribute_value(models.Model):
    attribute_value_id = models.AutoField(auto_created=True,primary_key=True)
    attribute = models.ForeignKey(attribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=100)
    
    def __str__(self):
        return self.value
    
    class Meta:
        db_table = "attribute_value"

class product_attribute(models.Model):
    product = models.ForeignKey(product,models.CASCADE)
    attribute_value = models.ForeignKey(attribute_value,models.CASCADE)
    
    def __str__(self):
        return self.product_id
    
    class Meta:
        db_table = "product_attribute"
    
class shopping_cart(models.Model):
    item_id = models.CharField(max_length=255,primary_key=True)
    cart_id = models.CharField(max_length=32)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    attributes = models.CharField(max_length=1000)
    quantity = models.IntegerField()
    buy_now = models.BooleanField(default=True)
    added_on = models.DateTimeField()
    
    def __str__(self):
        return self.attributes
    
    class Meta:
        db_table = "shopping_cart"
        
class shipping_region(models.Model):
    shipping_region_id = models.AutoField(auto_created=True,primary_key=True)
    shipping_region = models.CharField(max_length=100)
    
    def __str__(self):
        return self.shipping_region
    
    class Meta:
        db_table = "shipping_region"

class customer(models.Model):
    customer_id = models.AutoField(auto_created=True,primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    credit_card = models.TextField(null=True,blank=True)
    address_1 = models.CharField(max_length=100,null=True,blank=True)
    address_2 = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    region = models.CharField(max_length=100,null=True,blank=True)
    postal_code = models.CharField(max_length=100,null=True,blank=True)
    country = models.CharField(max_length=100,null=True,blank=True)
    shipping_region = models.ForeignKey(shipping_region,on_delete=models.CASCADE)
    day_phone = models.CharField(max_length=100,null=True,blank=True)
    eve_phone = models.CharField(max_length=100,null=True,blank=True)
    mob_phone = models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "customer"
        
class shipping(models.Model):
    shipping_id = models.AutoField(auto_created=True,primary_key=True)
    shipping_type = models.CharField(max_length=100)
    shipping_cost = models.DecimalField(max_digits=10,decimal_places=2)
    shipping_region = models.ForeignKey(shipping_region,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.shipping_type
    
    class Meta:
        db_table = "shipping"

class tax(models.Model):
    tax_id = models.AutoField(auto_created=True,primary_key=True)
    tax_type = models.CharField(max_length=100)
    tax_percentage = models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return self.tax_type
    
    class Meta:
        db_table = "tax"

        
class orders(models.Model):
    order_id = models.AutoField(auto_created=True,primary_key=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2,default='0.00')
    created_on = models.DateTimeField()
    shipped_on = models.DateTimeField(null=True)
    status = models.IntegerField()
    comments = models.CharField(max_length=255,null=True)
    customer = models.ForeignKey(customer,on_delete=models.CASCADE,null=True)
    auth_code = models.CharField(max_length=50,null=True)
    reference = models.CharField(max_length=50,null=True)
    shipping = models.ForeignKey(shipping,on_delete=models.CASCADE,null=True)
    tax = models.ForeignKey(tax,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.order_id
    
    class Meta:
        db_table = "orders"
    
class order_detail(models.Model):
    item_id = models.AutoField(auto_created=True,primary_key=True)
    orders = models.ForeignKey(orders,on_delete=models.CASCADE)
    product_id = models.IntegerField()
    attributes = models.CharField(max_length=1000)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit_cost = models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return self.product_name
    
    class Meta:
        db_table = "order_detail"
    
class audit(models.Model):
    audit_id = models.AutoField(auto_created=True,primary_key=True)
    orders = models.ForeignKey(orders,on_delete=models.CASCADE)
    created_on = models.DateTimeField()
    message = models.TextField()
    code = models.IntegerField()
    
    def __str__(self):
        return self.code
    
    class Meta:
        db_table = "audit"
        
class review(models.Model):
    review_id = models.AutoField(auto_created=True,primary_key=True)
    customer = models.ForeignKey(customer,on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.SmallIntegerField()
    created_on = models.DateTimeField()
    
    def __str__(self):
        return self.code
    
    class Meta:
        db_table = "review"
