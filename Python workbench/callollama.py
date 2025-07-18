import requests
import json

def callOLLAMA(user_message):
    try:
        url = "http://localhost:11434/api/generate"
        payload = {
            "model": "qwen2.5:0.5b",  # or "qwen2.5" if you installed that model
            "prompt": user_message,
            "stream": False
        }

        response = requests.post(
            url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload),
            timeout=120
        )

        if response.status_code == 200:
            result = response.json()
            return result.get("response", "Sorry, I am unable to help you.").strip()
        else:
            return "Error: Model response failed."

    except Exception as e:
        return f"Exception occurred: {e}"

