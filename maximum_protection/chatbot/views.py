from django.http import JsonResponse
from google.cloud import dialogflow
import os

def detect_intent(request):
    if request.method == 'POST':
        project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
        session_id = request.session.session_key
        text = request.POST.get('text')
        language_code = 'fr'

        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(project_id, session_id)

        text_input = dialogflow.TextInput(text=text, language_code=language_code)
        query_input = dialogflow.QueryInput(text=text_input)

        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )

        return JsonResponse({
            'response': response.query_result.fulfillment_text
        })