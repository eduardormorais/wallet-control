from fastapi import FastAPI
from fastapi_pagination import add_pagination


def init_routers(app: FastAPI):
    """
    This function is to load all routers in application.
    Here you can add routers from your modules.
    :param app:
    :return:
    """
    from app.modules.core import helthcheck_router
    from app.modules.user import router as user_router
    from app.modules.spent import router as spent_router

    app.include_router(helthcheck_router.router)
    app.include_router(user_router.router, prefix="/api/users", tags=["User"])
    app.include_router(spent_router.router, prefix="/api/spending", tags=["Spent"])

    add_pagination(app)
