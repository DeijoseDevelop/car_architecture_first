from celery import shared_task

from utils.validators.file_validator import FileValidator


@shared_task
def validate_file_task(filename):
    validator = FileValidator(filename)
    validator.validate_file()

    return set(validator.errors), validator.pd_to_list_of_dict()
