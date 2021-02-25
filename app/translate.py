import json
import requests
from flask_babel import _
from werkzeug.datastructures import Headers
from app import app

def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_APIKEY' not in app.config or \
        not app.config['MS_TRANSLATOR_APIKEY']:
        return _('Error: translation service is not configured.')
    auth = {
        'Ocp-Apim-Subscription-Key' : app.config['MS_TRANSLATOR_APIKEY'],
        'Ocp-Apim-Subscription-Region' : 'northeurope' }
    r = requests.post(app.config['MS_TRANSLATOR_API']+'/translate?api-version=3.0&from={}&to={}'.format(source_language, dest_language),
        headers=auth, json=[{'Text' : text}])
    if r.status_code != 200:
        return _('Error: translation service failed.')
    return r.json()[0]['translations'][0]['text']

# translate('potato', 'en', 'ru')