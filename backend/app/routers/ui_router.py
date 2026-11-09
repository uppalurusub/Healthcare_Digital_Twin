from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.services.digital_twin_service import DigitalTwinService
from app.schemas.request_model import PatientTwinRequest
from pathlib import Path

router = APIRouter(
    prefix="/ui",
    tags=["HTMX UI"]
)

BASE_DIR = Path(__file__).resolve().parent.parent

templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)





print(Path("templates").resolve())

service = None

def get_service():

    global service

    if service is None:
        service = DigitalTwinService()

    return service


@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        "base.html",
        {
            "request": request
        }
    )


@router.post("/digital-twin/patient")
async def create_patient(request: Request):

    form = await request.form()

    patient = PatientTwinRequest(
        patient_id=form.get("patient_id"),
        age=int(form.get("age")),
        gender=form.get("gender"),
        height_cm=float(form.get("height")),
        weight_kg=float(form.get("weight")),
        heart_rate=int(form.get("heart_rate")),
        blood_pressure=form.get("blood_pressure"),
        temperature=float(form.get("temperature")),
        diagnoses=[form.get("diagnosis")] if form.get("diagnosis") else [],
    )

    service = get_service()

    result = await service.create_patient_twin(patient)

    
    
    return templates.TemplateResponse(
        "patient_result.html",
        {
            "request": request,
            "result": result,
        },
    )