from django.shortcuts import render,redirect
from .models import Hero_page,About,Skill,Projects,Resume,ContactInfo,ContactMessage
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('mes')

        if all([name, email, message]): 
            try:
                send_mail(
                f"New Message from {name}",
                f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
                settings.EMAIL_HOST_USER,
                ['sahilrajputygamer@gmail.com']
                )

                ContactMessage.objects.create(name=name, email=email, message=message)
                messages.success(request, "✅ Message sent successfully!")
            except Exception as e:
                messages.error(request, "❌ Email sending failed! Try again later.")
                print(f"Error: {e}") 

            return redirect('home')

    # main section
    hero = Hero_page.objects.filter(is_active=True).first()
    sociallink = hero.social_links.all() if hero else []
    background = Hero_page.objects.first()

    about = About.objects.first()
    skills = Skill.objects.all()



    # resume section
    resume = Resume.objects.first()
    expertises = resume.experties.all() if resume else []
    education = resume.education.all() if resume else []
    certificates = resume.certificate.all() if resume else []
    resume_skills = resume.skills.all() if resume else []
    languages = resume.languages.all() if resume else []
    custom_cards = resume.custom_cards.all() if resume else []    
    resume_background_video = resume.background_video.url if resume and resume.background_video else None
    resume_background_image = resume.background_image.url if resume and resume.background_image else None




    # Project section
    project = Projects.objects.all()
    project_section_background = Projects.objects.filter(background_image__isnull=False).first()
   
   
   
   
    ## contact
    contact_us = ContactInfo.objects.first()
    contact_us = ContactInfo.objects.first()
    contact_us_background = contact_us.background.url if contact_us and contact_us.background else None





    context = {
        'skills': skills,
        'background_video':background,
        'background': background,
        'about': about,
        'about':about,
        'hero': hero,
        'links': sociallink, 
        'projects': project,
        'project_section_background': project_section_background,
        'resume': resume,
        'expertises': expertises,
        'education': education,
        'certificates': certificates,
        'resume_skills': resume_skills,
        'languages': languages,
        'custom_cards': custom_cards,
        'resume_background_video': resume_background_video,
        'resume_background_image': resume_background_image,
        'contact_us':contact_us,
        'contact_back': contact_us_background
    }
    return render(request, 'base.html', context)

