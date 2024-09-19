from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db
from src.example import models, schemas, exceptions, services

router = APIRouter()

# Rutas para Personas


@router.post("/personas", response_model=schemas.Persona)
def create_persona(persona: schemas.PersonaCreate, db: Session = Depends(get_db)):
    return services.crear_persona(db, persona)


@router.get("/personas", response_model=list[schemas.Persona])
def read_personas(db: Session = Depends(get_db)):
    return services.listar_personas(db)


@router.get("/personas/{persona_id}", response_model=schemas.Persona)
def read_persona(persona_id: int, db: Session = Depends(get_db)):
    return services.leer_persona(db, persona_id)


@router.put("/personas/{persona_id}", response_model=schemas.Persona)
def update_persona(
    persona_id: int, persona: schemas.PersonaUpdate, db: Session = Depends(get_db)
):
    return services.modificar_persona(db, persona_id, persona)


@router.delete("/personas/{persona_id}", response_model=schemas.Persona)
def delete_persona(persona_id: int, db: Session = Depends(get_db)):
    return services.eliminar_persona(db, persona_id)


# Rutas para Personas


@router.post("/mascotas", response_model=schemas.Mascota)
def create_mascota(mascota: schemas.MascotaCreate, db: Session = Depends(get_db)):
    return services.crear_mascota(db, mascota)


@router.get("/mascotas", response_model=list[schemas.Mascota])
def read_mascotas(db: Session = Depends(get_db)):
    return services.listar_mascotas(db)


@router.get("/mascotas/{mascota_id}", response_model=schemas.Mascota)
def read_mascota(mascota_id: int, db: Session = Depends(get_db)):
    return services.leer_mascota(db, mascota_id)


@router.put("/mascotas/{mascota_id}", response_model=schemas.Mascota)
def update_mascota(
    mascota_id: int, mascota: schemas.MascotaUpdate, db: Session = Depends(get_db)
):
    return services.modificar_mascota(db, mascota_id, mascota)


@router.delete("/mascotas/{mascota_id}", response_model=schemas.MascotaDelete)
def delete_mascota(mascota_id: int, db: Session = Depends(get_db)):
    return services.eliminar_mascota(db, mascota_id)

# Rutas para vehículos

@router.get("/vehiculos", response_model = list[schemas.Vehiculo])
def get_vehiculos(db: Session = Depends(get_db)):
    return services.listar_vehiculos(db)

@router.post("/vehiculos", response_model = schemas.Vehiculo)
def post_vehiculo(vehiculo: schemas.VehiculoCreate, db: Session = Depends(get_db)):
    return services.crear_vehiculo(db, vehiculo)

# Rutas para paseos

@router.get("/paseos", response_model = list[schemas.Paseo])
def get_paseos(db: Session = Depends(get_db)):
    return services.listar_paseos(db)

@router.post("/paseos", response_model = schemas.PaseoCreate)
def post_paseo(paseo: schemas.PaseoCreate, db: Session = Depends(get_db)):
    return services.crear_paseo(db, paseo)