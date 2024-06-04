
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware


class ErrorHandler(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except Exception as e:
            return JSONResponse(status_code=500, content={'msg': str(e)})
