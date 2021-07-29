from fastapi import APIRouter, Depends
from starlette.requests import Request
from sqlalchemy.orm import Session
from ariadne.asgi import GraphQL
from app.data.database import get_db
from . import schema

graphql_app = GraphQL(schema, debug=False)
graphQL_router = APIRouter()


@graphQL_router.get("/")
async def graphiql(request: Request):
    return await graphql_app.render_playground(request=request)


@graphQL_router.post("/")
async def graphql_post(request: Request, db: Session = Depends(get_db)):
    request.state.db = db
    return await graphql_app.graphql_http_server(request=request)