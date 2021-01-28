from os import getenv
import logging
from pprint import pprint

import sib_api_v3_sdk
from django.dispatch import receiver
from django.urls import reverse

from django_rest_resetpassword.signals import reset_password_token_created
from sib_api_v3_sdk.rest import ApiException


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param args:
    :param kwargs:
    :return:
    """
    # send an e-mail to the user
    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.email,
        'email': reset_password_token.user.email,
        'reset_password_url': "bkadhiveshan.na.baps.org/#/auth{}?token={}".format(
            reverse('password_reset:reset-password-confirm'), reset_password_token.key)
    }

    # Configure API key authorization: api-key
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = getenv('SENDINBLUE_API_KEY')
    # create an instance of the API class
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=[{"email": reset_password_token.user.email}],
                                                   sender={'email': 'kishore@na.baps.org'},
                                                   template_id=282,
                                                   params={"link": context.get('reset_password_url'), },
                                                   )
    try:
        # Send a transactional email
        api_instance.send_transac_email(send_smtp_email)
    except ApiException as e:
        pprint(e.body)
        logging.error("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
