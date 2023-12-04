from django.db import models

# Create your models here.

class Category(models.Model):
    slug = models.CharField(max_length=150,null=False,blank=False)
    name = models.CharField(max_length=150,null=False,blank=False)
    image = models.ImageField(upload_to='Category_image', null=True,blank=True)
    description = models.TextField(max_length=500, null=False,blank=False)
    status = models.BooleanField(default=False,help_text="0=default, 1=Hidden")
    trending = models.BooleanField(default=False,help_text="0=default, 1=Trending")
    meta_title = models.CharField(max_length=150,null=False,blank=False)
    meta_keywords = models.CharField(max_length=150,null=False,blank=False)
    meta_description = models.TextField(max_length=500,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class SubCategory(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='subcat_image')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    slug = models.SlugField() 


    def __str__(self):
        return '{}-{}'.format(self.name,self.category.name)

class ProductSegment(models.Model):
    name1 = models.CharField(max_length=200)
    name2 = models.CharField(max_length=200)
    slug = models.SlugField()
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    category =models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return '{}-{}-{}'.format(self.name1,self.subcategory.name,self.category.name)

class ProductSeries(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Productseries_img')
    image1 = models.ImageField(upload_to='Productseries_img',null=True,blank=True)
    image2 = models.ImageField(upload_to='Productseries_img',null=True,blank=True)
    image3 = models.ImageField(upload_to='Productseries_img',null=True,blank=True)
    description = models.CharField(max_length=500,null=True,blank=True)
    slug = models.SlugField()
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name

class Product(models.Model):
    slug = models.CharField(max_length=150,null=False,blank=False)
    name = models.CharField(max_length=150,null=False,blank=False)
    image1 = models.ImageField(upload_to='product_images', null=True,blank=True)
    image2 = models.ImageField(upload_to='product_images', null=True,blank=True)
    image3 = models.ImageField(upload_to='product_images', null=True,blank=True)
    image4 = models.ImageField(upload_to='product_images', null=True,blank=True)
    image5 = models.ImageField(upload_to='product_images', null=True,blank=True)
    image6 = models.ImageField(upload_to='product_images', null=True,blank=True)
    image7 = models.ImageField(upload_to='product_images', null=True,blank=True)
    image8 = models.ImageField(upload_to='product_images', null=True,blank=True)
    video= models.FileField(upload_to='product_vdo',null=True,blank=True)
    small_description = models.CharField(max_length=250, null=False,blank=False)
    quantity = models.IntegerField(null=False,blank=False)
    description = models.TextField(max_length=500, null=False,blank=False)
    Original_price = models.FloatField(null=False,blank=False)
    selling_price = models.FloatField(null=False,blank=False)
    status = models.BooleanField(default=False,help_text="0=default, 1=Hidden")
    trending = models.BooleanField(default=False,help_text="0=default, 1=Trending")
    tag = models.CharField(max_length=150,null=False,blank=False)
    meta_title = models.CharField(max_length=150,null=False,blank=False)
    meta_keywords = models.CharField(max_length=150,null=False,blank=False)
    meta_description = models.TextField(max_length=500,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    productseries = models.ForeignKey(ProductSeries,on_delete=models.CASCADE)
    productsegment = models.ForeignKey(ProductSegment,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
