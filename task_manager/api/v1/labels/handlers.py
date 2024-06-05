from django.http import HttpRequest
from ninja import Router

from task_manager.api.v1.labels.schemas import LabelListSchema, LabelSchema
from task_manager.apps.labels.services.labels import BaseLabelService, ORMLabelService


router = Router(tags=["Labels"])


@router.get("", response=LabelListSchema)
def get_label_list_handler(request: HttpRequest) -> LabelListSchema:
    service: BaseLabelService = ORMLabelService()
    label_list = service.get_label_list()

    return [LabelSchema.from_entity(obj) for obj in label_list]
