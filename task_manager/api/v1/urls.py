from ninja import Router

from task_manager.api.v1.users.handlers import router as user_router
from task_manager.api.v1.labels.handlers import router as label_router
from task_manager.api.v1.statuses.handlers import router as status_router
from task_manager.api.v1.tasks.handlers import router as task_router


router = Router(tags=["v1"])

router.add_router("users/", user_router)
router.add_router("labels/", label_router)
router.add_router("statuses/", status_router)
router.add_router("tasks/", task_router)
