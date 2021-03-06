"""
Contains misc and util functions used by multiple files in the app
"""
import re
from django.core.exceptions import ValidationError


def validate_parent(parent, current_round):
    """
    Checks to see if a Match object being saved has valid 'prev_matches' fields
    Currently checks to see if the 'round' fields in 'prev_matches' are all lower
    than the 'round' in the request's body

    Used in:
        serializers.MatchSerializer.validate
        forms.MatchForm.clean

    :param parent: a parent match
    :param current_round: integer value that is guaranteed to be >= 1
    :return: Raises a ValidationError if field is invalid
    """

    if parent.round <= current_round:
        raise ValidationError(
            "The match '{0}' has a round of '{1}' "
            "which is less than or equal to "
            "the current round of '{2}'".format(parent, parent.round, current_round))


def validate_email(email):
    """
    Validates a given email based on regex

    :param email: email to be validated
    """
    from django.core.validators import validate_email
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False


def validate_token(token):
    """
    Validates a given token based on regex

    :param token: token string
    """
    if not re.match('[a-z0-9-]*', token):
        raise ValidationError("Token does not match regex")

    if len(token) != 40:
        raise ValidationError("Token length is incorrect")


def does_url_match_id(url, id_num):
    """
    Takes an API url string and checks if the ID at the end matches the input

    :param url: URL string
    :param id_num: number of id
    :return: True or False
    """
    return int(url.path.split("/")[3]) == id_num
