
import os

AZURE_OPENAI_ENDPOINT= os.getenv("AZURE_OPENAI_ENDPOINT")
LOGIN_EURLEX= os.getenv("LOGIN_EURLEX")
MOT_DE_PASSE_EURLEX= os.getenv("MOT_DE_PASSE_EURLEX")


### API legifrance
client_id_pro = os.getenv("client_id_pro")
client_secret_pro = os.getenv("client_secret_pro")
client_id = os.getenv("client_id") 
client_secret = os.getenv("client_secret")

### OpenAI
Azure_OpenAI_OB_Key = os.getenv("Azure_OpenAI_OB_Key")
Azure_OpenAI_OB_Endpoint = os.getenv("Azure_OpenAI_OB_Endpoint")
AZURE_OPENAI_KEY= os.getenv("AZURE_OPENAI_KEY")
api_key_firecraw = os.getenv("api_key_firecraw")