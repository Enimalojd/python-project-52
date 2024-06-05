from typing import List
from django.http import HttpRequest
from ninja import Router

from task_manager.api.v1.statuses.schemas import StatusSchema
from task_manager.apps.statuses.services.statuses import (
    BaseStatusService,
    ORMStatusService,
)


router = Router(tags=["Statuses"])


@router.get("/", response=List[StatusSchema])
def get_status_list_handler(request: HttpRequest) -> List[StatusSchema]:
    service: BaseStatusService = ORMStatusService()

    status_list = service.get_status_list()

    return [StatusSchema.from_entity(obj) for obj in status_list]
