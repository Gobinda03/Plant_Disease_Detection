import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_report(
        disease: str,
        confidence: float
):
    
    prompt = f"""
You are an agricultural expert.

Disease Detected:
{disease}

Model Confidence:
{confidence:.2f}%

Generate a professional report in markdown format.

Include:

# Disease Summary
- What is this disease?

# Symptoms
- Common symptoms

# Organic Treatment
- Natural remedies
- Organic sprays
- Compost or nutrient recommendations

# Prevention
- Best prevention practices

# Recovery Time
- Estimated recovery period

# Farmer Recommendations
- Immediate actions farmer should take

Keep response concise and practical.
"""

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.4
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"""
# Report Generation Failed

Error:

{str(e)}
"""