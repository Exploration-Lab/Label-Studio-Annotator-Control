"""This file and its contents are licensed under the Apache License 2.0. Please see the included NOTICE for copyright information and LICENSE for a copy of the license.
"""
import logging

from django.db.models import signals

from core.permissions import AllPermissions
from core.utils.common import temporary_disconnect_signal, temporary_disconnect_all_signals
from tasks.models import Annotation, Prediction, update_is_labeled_after_removing_annotation
from webhooks.utils import emit_webhooks_for_instance
from webhooks.models import WebhookAction
from data_manager.functions import evaluate_predictions

all_permissions = AllPermissions()
logger = logging.getLogger(__name__)


def retrieve_tasks_predictions(project, queryset, **kwargs):
    """ Retrieve predictions by tasks ids

    :param project: project instance
    :param queryset: filtered tasks db queryset
    """
    evaluate_predictions(queryset)
    return {'processed_items': queryset.count(), 'detail': 'Retrieved ' + str(queryset.count()) + ' predictions'}


# Deleted "delete tasks" function

# Deleted "delete task annotations" function

# Deleted "delete task predictions" function


actions = [
    {
        'entry_point': retrieve_tasks_predictions,
        'permission': all_permissions.predictions_any,
        'title': 'Retrieve Predictions',
        'order': 90,
        'dialog': {
            'text': 'Send the selected tasks to all ML backends connected to the project.'
                    'This operation might be abruptly interrupted due to a timeout. '
                    'The recommended way to get predictions is to update tasks using the Label Studio API.'
                    '<a href="https://labelstud.io/guide/ml.html>See more in the documentation</a>.'
                    'Please confirm your action.',
            'type': 'confirm'
        }
    },
  
  
    # Removed 3 Actions of Tasks: Delete Tasks, Delete Task Annotations, Delete Task Predcitions
]
