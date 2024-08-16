from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from Calculate import Calculator

app = FastAPI()
calculator = Calculator()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def post_index(
    request: Request,
    a: float = Form(...),
    b: float = Form(...),
    operation: str = Form(...)
):
    result = None
    error = None
    
    try:
        if operation == "add":
            result = calculator.add(a, b)
        elif operation == "subtract":
            result = calculator.subtract(a, b)
        elif operation == "multiply":
            result = calculator.multiply(a, b)
        elif operation == "divide":
            result = calculator.divide(a, b)
        elif operation == "sign_change":
            result = calculator.sign_change(a, b)
    except ValueError:
        error = "Invalid input. Please enter numeric values."

    return templates.TemplateResponse("index.html", {"request": request, "result": result, "error": error})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000, loop = "auto")
