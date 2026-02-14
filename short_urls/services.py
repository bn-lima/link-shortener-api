import uuid

def create_formated_uuid():
    return str(uuid.uuid4()).split('-')[0]

def get_short_url(id_token):
    return f"127.0.0.1:8000/short/{id_token}/"
