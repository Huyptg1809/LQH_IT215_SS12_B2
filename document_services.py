from sqlalchemy.orm import Session
from models import DocumentModel
from schemas import DocumentCreate
from fastapi import HTTPException, status

def get_all_documents_service(db: Session):
    return db.query(DocumentModel).all()

def create_document_service(document: DocumentCreate, db: Session):
    new_doc = DocumentModel(**document.model_dump())
    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)
    return new_doc

def delete_document_service(document_id: int, db: Session):
    doc = db.query(DocumentModel).filter(DocumentModel.id == document_id).first()
    if not doc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tài liệu không tồn tại"
        )
    
    db.delete(doc)
    db.commit()
    return {"message": "Xóa tài liệu thành công", "document_id": document_id}
