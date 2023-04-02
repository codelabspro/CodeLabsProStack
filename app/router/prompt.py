import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, Response, Query
import database, models
# from sqlalchemy.orm import Session
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select
import oauth2

router = APIRouter(
    tags = ['Prompts']
)

###############################################################################
## Prompt

@router.post('/prompts/', response_model=models.PromptRead)
def create_prompt(
    *,
    session: Session = Depends(database.get_session),
    current_user: models.User = Depends(oauth2.get_current_user),
    prompt: models.PromptCreate
):
    db_prompt = models.Prompt.from_orm(prompt)
    session.add(db_prompt)
    session.commit()
    session.refresh(db_prompt)
    return prompt

@router.get('/prompts', response_model=List[models.PromptRead])
def read_prompts(
    *,
    session: Session = Depends(database.get_session),
    current_user: models.User = Depends(oauth2.get_current_user),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
):
    prompts = session.exec(select(models.Prompt).offset(offset).limit(limit)).all()
    return prompts

@router.get('/prompts/{prompt_id}', response_model=models.PromptReadWithUser)
def read_prompt(
    *,
    session: Session = Depends(database.get_session),
    current_user: models.User = Depends(oauth2.get_current_user),
    prompt_id: int
):
    prompt = session.get(models.Prompt, prompt_id)
    if not prompt:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Prompt with id {prompt_id} is not available")
    return prompt

@router.patch('/prompts/{prompt_id}', response_model=models.PromptRead)
def update_prompt(
    *,
    session: Session = Depends(database.get_session),
    current_user: models.User = Depends(oauth2.get_current_user),
    prompt_id: int,
    prompt: models.PromptUpdate
):
    db_prompt = session.get(models.Prompt, prompt_id)
    if not db_prompt:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Prompt with id {prompt_id} not found")
    prompt_data = prompt.dict(exclude_unset=True)
    for key, value in prompt_data.items():
        setattr(db_prompt, key, value)
    session.add(db_prompt)
    session.commit()
    session.refresh(db_prompt)
    return db_prompt

@router.delete('/prompts/{prompt_id}')
def delete_prompt(
    *,
    session: Session = Depends(database.get_session),
    current_user: models.User = Depends(oauth2.get_current_user),
    prompt_id: int,
):
    prompt = session.get(models.Prompt, prompt_id)
    if not prompt:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Prompt with id {prompt_id} not found")
    session.delete(prompt)
    session.commit()
    return {'detail': f"Prompt with id {prompt_id} was deleted"}


###############################################################################
