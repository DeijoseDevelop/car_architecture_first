from celery import shared_task
from django.core.mail import EmailMultiAlternatives

from utils.validators.file_validator import FileValidator
from utils.scrappers import DataMiner


@shared_task
def validate_file_task(filename):
    validator = FileValidator(filename)
    validator.validate_file()

    return set(validator.errors), validator.pd_to_list_of_dict()

@shared_task
def send_email_task(subject, from_email, to_emails, plain_message, html_message):
    email = EmailMultiAlternatives(
        subject, plain_message, from_email, to_emails)
    email.content_subtype = 'html'
    email.attach_alternative(html_message, "text/html")
    email.send()

@shared_task
def make_scrapper(topic: str):
    scrapper = DataMiner()
    courses = scrapper.get_courses(topic)
    return courses

