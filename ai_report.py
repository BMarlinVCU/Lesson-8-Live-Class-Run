from groq import Groq
import os

def make_report(weather_data):
    client=Groq(api_key=os.environ.get("GROQ_API_KEY"))


    response=client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role":"system",
            "content":("you are a weather reporter"
                        "write a short report about the provied weather data"
                        "do not invent fake data")},
            {"role":"user",
            "content":weather_data}
        ],
        reasoning_effort="low"
    )
    report=response.choices[0].message.content
    usage=response.usage

    return report,usage