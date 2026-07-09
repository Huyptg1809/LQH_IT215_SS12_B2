from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List

from database import engine, get_db
from models import Base
from schemas import DocumentCreate, DocumentResponse
from document_services import (
    get_all_documents_service,
    create_document_service,
    delete_document_service
)

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/documents", response_model=List[DocumentResponse])
def get_documents(db: Session = Depends(get_db)):
    return get_all_documents_service(db)

@app.post("/documents", response_model=DocumentResponse)
def create_document(document: DocumentCreate, db: Session = Depends(get_db)):
    return create_document_service(document, db)
@app.delete("/documents/{document_id}")
def delete_document(document_id: int, db: Session = Depends(get_db)):
    return delete_document_service(document_id, db)
