from fastapi import FastAPI, Depends, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse ,RedirectResponse
from fastapi.templating import Jinja2Templates




app = FastAPI()
templates = Jinja2Templates(directory="templates")


# Set up Jinja2 template directory
templates = Jinja2Templates(directory="templates")

# Redirect root ("/") → "/home"
@app.get("/", response_class=HTMLResponse)
async def root():
    return RedirectResponse(url="/home")

# Serve home.html
@app.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

