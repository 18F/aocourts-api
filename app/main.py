import os

from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.api_v1.api import api_router
from app.docs.api_metadata import tags_metadata
from app.api.graph_ql.routes_public import graphQL_router_public
from app.api.graph_ql.routes_private import graphQL_router_private


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    openapi_tags=tags_metadata
)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(graphQL_router_public, prefix=settings.GRAPHQL_ENDPOINT_PUBLIC, tags=["GraphQL"])
app.include_router(graphQL_router_private, prefix=settings.GRAPHQL_ENDPOINT_PRIVATE, tags=["GraphQL"])


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)  # type: ignore
