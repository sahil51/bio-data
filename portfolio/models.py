from django.db import models

# Create your models here.


###################### main page database####################################################################################################################
class Hero_page(models.Model):
    BACKGROUND_CHOICES = [
        ('image', 'Image'),
        ('video', 'Video'),
    ]

    background_type = models.CharField(max_length=10, choices=BACKGROUND_CHOICES, default='image')
    image = models.ImageField(upload_to='home_background_image/', blank=True, null=True)
    video = models.FileField(upload_to='home_background_video/', blank=True, null=True)
    mes= models.CharField(verbose_name="Greet/or Message here",default='Hello, I am',max_length=400)
    name = models.CharField(verbose_name='Your name',   max_length=100)
    title = models.CharField(verbose_name='title',max_length=100,)
    des = models.TextField(verbose_name='Write short description')
    button_text = models.CharField(verbose_name='Modify button name',default="Expore",max_length=100)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - Background ({self.background_type})"
    
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

############################################################################### About database ##################################################################

class About(models.Model):
    background = models.FileField(verbose_name='Set Background image/video',upload_to='about_background_image_video/',blank=True,null=True)
    title = models.CharField(max_length=255,default="Who am I ?")
    des = models.CharField(max_length=300,default='A Web Designer / Python Developer')
    bio = models.TextField(default="I'm a web developer skilled in Html, CSS, Bootstrap, Python, Django, and MySQL, focusing on building scalable and efficient web applications.")
    cv = models.FileField(upload_to='cv/', blank=True, null=True)
            ##################### contact details#####################
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
    
#################################################### resume ############################################
class Resume(models.Model):
    background_video = models.FileField(verbose_name='Set Background Video',upload_to='resume_background_video/',blank=True,null=True)
    background_image = models.ImageField(verbose_name='Set Background Image',upload_to='resume_background_image/',blank=True,null=True)
    main_title = models.CharField(max_length=255, default='My Resume')
    main_description = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.main_title

class Expertise(models.Model):
    resume = models.ForeignKey(Resume,on_delete=models.CASCADE, related_name='experties')
    title = models.CharField(max_length=255)
    des = models.TextField(max_length=255)

    def __str__(self):
        return self.title

class Education(models.Model):
    resume = models.ForeignKey(Resume,on_delete=models.CASCADE,related_name='education')
    degree = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    start_year = models.CharField(max_length=20)
    end_year = models.CharField(max_length=24,blank=True,null=True)
    marks = models.CharField(max_length=10,blank=True,null=True)

    def __str__(self):
        return f'{self.degree} - {self.institution}'

class Certificate(models.Model):
    resume = models.ForeignKey(Resume,on_delete=models.CASCADE, related_name='certificate')
    title = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class ResSkill(models.Model):
    resume = models.ForeignKey(Resume,on_delete=models.CASCADE,related_name='skills')
    name = models.CharField(max_length=255)
    proficiency = models.IntegerField(help_text="Enter a value between 0 and 100")

    def __str__(self):
        return self.name
    
class Language(models.Model):
    resume = models.ForeignKey(Resume,on_delete=models.CASCADE,related_name='languages')
    name = models.CharField(max_length=255)
    proficiency = models.IntegerField(help_text="Enter a value between 0 and 100")

    def __str__(self):
        return self.name

class CustomCard(models.Model):
    resume = models.ForeignKey(Resume,on_delete=models.CASCADE,related_name='custom_cards')

    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title
################################################### project database#############################################################################################


class Projects(models.Model):
    title = models.CharField(max_length=255, help_text='Enter the project title.')
    tech = models.CharField(max_length=300,verbose_name='Technology Stack', help_text='List the technologies used, such as programming languages, frameworks, and tools.')
    des = models.TextField(help_text='Provide a brief description of your project, highlighting its features and purpose.')
    live_link = models.URLField(blank=True, null=True, help_text="If your project is deployed, enter its live URL. Leave blank if it's not hosted.")
    source_code = models.URLField(help_text="Enter the GitHub repository link or any source code URL.")

    # Add background fields for the whole section
    background_image = models.ImageField(verbose_name="Project Section Background Image",upload_to="project_background_image/",blank=True,null=True)
    background_video = models.FileField(verbose_name="Project Section Background Video",upload_to="project_background_video/",blank=True,null=True)

    def __str__(self):
        return self.title

###################################contact us#############
class ContactInfo(models.Model):
    heading = models.CharField(max_length=50)
    des = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    addres = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    background = models.ImageField(upload_to='contact_background',null=True,blank=True)

    def __str__(self):
        return f"Contact Info - {self.email}"
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.name} - {self.email}'
