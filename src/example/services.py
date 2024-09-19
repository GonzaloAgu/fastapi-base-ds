from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.example.models import Persona, Mascota, Vehiculo, Paseo
from src.example import schemas, exceptions

# operaciones CRUD para Personas


def crear_persona(db: Session, persona: schemas.PersonaCreate) -> Persona:
    db_persona = db.scalars(select(Persona).where(Persona.email == persona.email)).first()
    if db_persona:
        raise exceptions.EmailDuplicado()
    return Persona.create(db, persona)


def listar_personas(db: Session) -> List[Persona]:
    return Persona.get_all(db)


def leer_persona(db: Session, persona_id: int) -> Persona:
    db_persona = Persona.get(db, persona_id)
    if db_persona is None:
        raise exceptions.PersonaNoEncontrada()
    return db_persona


def modificar_persona(
    db: Session, persona_id: int, persona: schemas.PersonaUpdate
) -> Persona:
    db_persona = leer_persona(db, persona_id)
    return db_persona.update(db, persona)


def eliminar_persona(db: Session, persona_id: int) -> Persona:
    db_persona = leer_persona(db, persona_id)
    if len(db_persona.mascotas) > 0:
        raise exceptions.PersonaTieneMascotas()
    db_persona.delete(db)
    return db_persona


# operaciones CRUD para Mascota


def crear_mascota(db: Session, mascota: schemas.MascotaCreate) -> Mascota:
    return Mascota.create(db, mascota)


def listar_mascotas(db: Session) -> List[Mascota]:
    return Mascota.get_all(db)


def leer_mascota(db: Session, mascota_id: int) -> Mascota:
    db_mascota = Mascota.get(db, mascota_id)
    if db_mascota is None:
        raise exceptions.MascotaNoEncontrada()
    return db_mascota


def modificar_mascota(
    db: Session, mascota_id: int, mascota: schemas.MascotaUpdate
) -> Mascota:
    db_mascota = leer_mascota(db, mascota_id)
    return db_mascota.update(db, mascota)


def eliminar_mascota(db: Session, mascota_id: int) -> schemas.MascotaDelete:
    db_mascota = leer_mascota(db, mascota_id)
    db_mascota.delete(db)
    return db_mascota

# Operaciones CRUD para vehiculos

def crear_vehiculo(db: Session, vehiculo: schemas.VehiculoCreate) -> Vehiculo:
    return Vehiculo.create(db, vehiculo)

def leer_vehiculo(db: Session, vehiculo_id: int) -> Vehiculo:
    db_vehiculo = Vehiculo.get(db, vehiculo_id)
    if db_vehiculo is None:
        raise exceptions.VehiculoNoEncontrado()
    return db_vehiculo

def listar_vehiculos(db: Session) -> List[Vehiculo]:
    return Vehiculo.get_all(db)

# Operaciones CRUD para paseos

def listar_paseos(db: Session) -> List[Paseo]:
    return Paseo.get_all(db)

def crear_paseo(db: Session, paseo: schemas.PaseoCreate) -> Paseo:
    return Paseo.create(db, paseo)