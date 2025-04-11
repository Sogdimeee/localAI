import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from openai import OpenAI

class AskQuestionView(APIView):
    def post(self, request):
        question = request.data.get('question')

        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key="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",
        )

        completion = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional. Site URL for rankings on openrouter.ai.
                "X-Title": "<YOUR_SITE_NAME>",  # Optional. Site title for rankings on openrouter.ai.
            },
            extra_body={},
            model="deepseek/deepseek-r1-distill-qwen-32b:free",
            messages=[
                {
                    "role": "user",
                    "content": "What is the meaning of life?"
                }
            ]
        )
        answer = completion.choices[0].message.content


        return Response({"question": question, "answer": answer}, status=status.HTTP_200_OK)

#
# {
# "question" : "how to get an credit?"
# }