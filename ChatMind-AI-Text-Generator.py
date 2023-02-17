from flask import Flask, request, render_template
import openai

app = Flask(__name__)

# set OpenAI API key and model engine
openai.api_key = "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"
model_engine = "text-davinci-002"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        prompt = request.form["prompt"]
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.9
        )
        response = completion.choices[0].text
        return render_template("index.html", response=response)
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
