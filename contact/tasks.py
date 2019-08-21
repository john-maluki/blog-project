from celery.decorators import task
from celery.utils.log import get_task_logger
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from contact.emails import send_contact_email
from contact.emails import send_periodic_email

logger = get_task_logger(__name__)


@task(name="send_contact_email_task")
def send_contact_email_task(email, message):
    """sends an email when contact form is filled successfully"""
    logger.info("Sent contact email")
    return send_contact_email(email, message)


@periodic_task(run_every=(
    crontab(minute='*/1')), name="sendperiodic_email", ignore_result=True)
def send_periodic_email_task():
    logger.info("Sent periodic email")
    send_periodic_email()
