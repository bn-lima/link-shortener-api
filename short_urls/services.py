import uuid

def get_url_domain(url):
    start = str(url).split('/')[0]
    end = str(url).split('/')[2]
    return start + '//' + end + '/'

def create_formated_uuid():
    return str(uuid.uuid4()).split('-')[0]