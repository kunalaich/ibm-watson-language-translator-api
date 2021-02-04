"""
Language Translator
"""

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

WATSON_API = 'https://api.us-south.language-translator.watson.cloud.ibm.com/'
WATSON_API += 'instances/228de068-98ee-4082-b7eb-ff67af934117'


def englishtofrench(text):
    """
    English to French
    """
    authenticator = IAMAuthenticator('Oeym1JfKdcTcCp2lCQ5YH24CAC0Oa2FXdZFyP2ZFVL1Z')
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )
    language_translator.set_service_url(WATSON_API)
    if text is None or text == '':
        return 'Input is empty'
    translation = language_translator.translate(
        text=text,
        model_id='en-fr').get_result()
    french_txt = translation["translations"][0]["translation"]
    return french_txt

def englishtogerman(text):
    """
    English to German
    """
    authenticator = IAMAuthenticator('Oeym1JfKdcTcCp2lCQ5YH24CAC0Oa2FXdZFyP2ZFVL1Z')
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )
    language_translator.set_service_url(WATSON_API)
    if text is None or text == '':
        return 'Input is empty'
    translation = language_translator.translate(
        text=text,
        model_id='en-de').get_result()
    german_txt = translation["translations"][0]["translation"]
    return german_txt

if __name__ == "__main__":
    french = englishtofrench('Hello')
    print(french)
    german = englishtogerman('Hello')
    print(german)
