import pathlib
from fastapi import FastAPI, Request # type: ignore
from fastapi.staticfiles import StaticFiles # type: ignore
from starlette.middleware.cors import CORSMiddleware # type: ignore
from api.router import router as api_router
from fastapi.templating import Jinja2Templates # type: ignore
from fastapi.responses import HTMLResponse # type: ignore


# from main.api.v1.router import router as api_router # type: ignore
# from main.core.config import get_app_settings # type: ignore
# from main.core.exceptions import add_exceptions_handlers # type: ignore

# templates = Jinja2Templates(directory="templates")
BASE_DIR = pathlib.Path(__file__).parent
templates = Jinja2Templates(directory=[
    BASE_DIR / "templates",
])

def create_app() -> FastAPI:
    """
    Application factory, used to create application.
    """
    # settings = get_app_settings()
    # app.mount("/static", StaticFiles(directory="static"), name="static")
    # application = FastAPI(**settings.fastapi_kwargs)
    application = FastAPI()

    application.add_middleware(
        CORSMiddleware,
        # allow_origins=settings.allowed_hosts,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(api_router, prefix="/api")
    application.mount("/static", StaticFiles(directory="static", html = True), name="static")
    # add_exceptions_handlers(app=application)

    return application


app = create_app()

@app.get("/sample")
async def home(request: Request):
    # todos = db.query(models.Todo).order_by(models.Todo.id.desc())
    # return templates.TemplateResponse("index.html", {"request": request, "todos": todos})
    context = {"request": request}
    return templates.TemplateResponse("index.html", context)   
# if __name__ == "__main__":
#     import uvicorn # type: ignore
#     uvicorn.run(app, host="127.0.0.1", port=8000)

@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    posts = [
        {"id":1, "title":"fastapi.blog title 1", "body":"Learn FastAPI with the fastapi.blog team 1"},
        {"id":2, "title":"fastapi.blog title 2", "body":"Learn FastAPI with the fastapi.blog team 2"},
        {"id":3, "title":"fastapi.blog title 3", "body":"Learn FastAPI with the fastapi.blog team 3"},
    ]
    products = [
        {"id":1, "title":"fastapi.blog title 1", "body":"Learn FastAPI with the fastapi.blog team 1"},
        {"id":2, "title":"fastapi.blog title 2", "body":"Learn FastAPI with the fastapi.blog team 2"},
        {"id":3, "title":"fastapi.blog title 3", "body":"Learn FastAPI with the fastapi.blog team 3"},
    ]
    context = {
        "request": request,
        "posts": posts,
        "products": products,
        "title": "Bakey Home Page"
    }
    response = templates.TemplateResponse("index.html", context)
    return response


@app.get('/products/{item_id}', response_class=HTMLResponse)
async def product_detail(item_id, request: Request):
    context = {
        "request": request,
        "title": "Bakey Home Page",
        "item_id": item_id
    }
    response = templates.TemplateResponse("detail.html", context)
    return response