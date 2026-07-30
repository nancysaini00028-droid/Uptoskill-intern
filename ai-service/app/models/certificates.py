from pydantic import BaseModel


class CertificateRequest(BaseModel):
    task: str