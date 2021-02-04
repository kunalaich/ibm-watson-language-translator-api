import requests
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def englishtofrench(text):
    authenticator = IAMAuthenticator('Oeym1JfKdcTcCp2lCQ5YH24CAC0Oa2FXdZFyP2ZFVL1Z')
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )
    language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/228de068-98ee-4082-b7eb-ff67af934117')

    translation = language_translator.translate(
        text=text,
        model_id='en-fr').get_result()
    french = translation["translations"][0]["translation"]
    return french

if __name__ == "__main__":
    french = englishtofrench('Hello, how are you today?')
    print(french)
