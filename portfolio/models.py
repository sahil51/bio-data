from django.db import models

# Create your models here.
class Hero_page(models.Model):
    mes= models.CharField(verbose_name="Greet/or Message here",default='Hello, I am',max_length=400)
    name = models.CharField(verbose_name='Your name',   max_length=100)
    title = models.CharField(verbose_name='title',max_length=100,)


    des = models.TextField(verbose_name='Write short description')
    button_text = models.CharField(verbose_name='Modify button name',default="Expore",max_length=100)

    background_image = models.ImageField(verbose_name='Set Background Image',upload_to='static/media/',blank=True,null=True)
    background_video = models.FileField(verbose_name='Set Background Video',upload_to='static/media/',blank=True,null=True)

    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

class SocailLinks(models.Model):
    Platform_Choices = [
        ('instagram', 'Instagram'),
        ('linkedin', 'Linkedin'),
        ('github', 'Github'),
        ('facebook', 'Facebook'),
        ('x', 'X'),
        ('whatsapp','WhatsApp'),
        ('mail', 'Mail')
    ]

    hero = models.ForeignKey(Hero_page,on_delete=models.CASCADE,related_name='social_links')
    platform = models.CharField(max_length=100,choices=Platform_Choices)
    url = models.URLField()
    icon_class = models.CharField(max_length=100,help_text="FontAwesome class (e.g., fa-brands fa-instagram)")



    def __str__(self):
        return f'{self.platform} - {self.url}'


class About(models.Model):
    background_video = models.FileField(verbose_name='Set Background image/video ',upload_to='static/media/about',blank=True,null=True)
    title = models.CharField(max_length=255,default="Who am I ?")
    des = models.CharField(max_length=300,default='A Web Designer / Python Developer')
    bio = models.TextField(default="I'm a web developer skilled in Html, CSS, Bootstrap, Python, Django, and MySQL, focusing on building scalable and efficient web applications.")
    cv = models.FileField(upload_to='cv/', blank=True, null=True)
    # contact details
    birthday = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    github = models.URLField()
    address = models.TextField()

    def __str__(self):
        return self.title
    
class Category(models.Model):
    about = models.ForeignKey(About,on_delete=models.CASCADE,related_name='Categories')
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
class Skill(models.Model):  
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='categories')
    About  = models.ForeignKey(About, on_delete=models.CASCADE,related_name='abouts')
    name = models.CharField(max_length=100)
    des = models.CharField(max_length=300)
    icon = models.CharField(max_length=100,help_text="Enter a FontAwesome or Bootstrap icon class (e.g., 'fa-solid fa-code')")

    def __str__(self):
        return f"{self.category} - {self.name}"