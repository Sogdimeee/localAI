import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import QuestionAnsweringBot, QuestionAnsweringBot2

class AskQuestionView(APIView):
    def post(self, request):
        question = request.data.get('question')

        if not question:
            return Response({"error": "Missing 'question' in request"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            context_path = os.path.join(os.path.dirname(__file__), "context.txt")
            with open(context_path, "r", encoding="utf-8") as f:
                context = f.read()
        except FileNotFoundError:
            return Response({"error": "context.txt not found"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        bot = QuestionAnsweringBot()
        answer = bot.ask(question, context)

        print(answer)

        bot2 = QuestionAnsweringBot2()
        answer = bot2.ask(answer)


        return Response({"question": question, "answer": answer}, status=status.HTTP_200_OK)

#
# {
# "question" : "how to get an credit?"
# }