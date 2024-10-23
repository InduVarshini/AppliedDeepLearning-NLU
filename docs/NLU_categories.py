import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 \
    import Features, CategoriesOptions, EntitiesOptions, KeywordsOptions \
    , ConceptsOptions, EmotionOptions, SentimentOptions, SyntaxOptions


from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Print the environment variables
IAM_KEY = os.getenv('IAM_KEY')
SERVICE_URL = os.getenv('SERVICE_URL')
# print(os.getenv('IAM_KEY'))
print(os.getenv('SERVICE_URL'))

authenticator = IAMAuthenticator(IAM_KEY)
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2022-04-07',
    authenticator=authenticator
)

natural_language_understanding.set_service_url(SERVICE_URL)

#https://cloud.ibm.com/apidocs/natural-language-understanding?code=python#categories


#Categories
response = natural_language_understanding.analyze(
    url='www.ibm.com',
    features=Features(categories=CategoriesOptions(limit=3))).get_result()

print(json.dumps(response, indent=2))

# #Enttities
# response = natural_language_understanding.analyze(
#     url='www.cnn.com',
#     features=Features(entities=EntitiesOptions(sentiment=True,limit=1))).get_result()

# print(json.dumps(response, indent=2))

#Emotions
# response = natural_language_understanding.analyze(
#     html="<html><head><title>Fruits</title></head><body><h1>Apples and Oranges</h1><p>I love apples! I don't like oranges.</p></body></html>",
#     features=Features(emotion=EmotionOptions(targets=['apples','oranges']))).get_result()

# print(json.dumps(response, indent=2))