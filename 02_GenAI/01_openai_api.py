# openai api 플랫폼 사이트에 api 키 발급

# openai api를 사용할 수 있는 모듈 설치
# pip install openai
# 
# pip install google-generativeai

# OpenAI api 모듈 사용
from openai import OpenAI

# OpenAI 객체 생성 [ apikey 를 코드에 직접 사용하는 것은 위험 파이썬 환경변수(.env) 파일에 저장하고 사용]
# dotenv() 외부모듈 사용
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

# 이전 대화 ID 저장
previous_id = None

print("AI 챗봇 시작! (종료: exit)")
while True:
    question = input('\n사용자: ')
    if question.lower() == 'exit':
        break

    # LLM AI 호출 및 응답
    response = client.responses.create(
        model = 'gpt-4o-mini',
        instructions="당신은 친절한 한국어 AI 챗봇입니다. 너는 강아지라서 언제나 끝은 멍멍! 이라고 해.",
        input=question,
        previous_response_id= previous_id,
    )

    # 응답결과 출력
    print("AI: ", response.output_text)

    previous_id = response.id
