from flask import Flask, render_template, request, session
import openai

app = Flask(__name__)

# set the secret key for session management
app.secret_key = "my_secret_key"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get-api-key", methods=["POST"])
def get_api_key():
    # get the OpenAI API key from the user
    api_key = request.form["api_key"]
    
    # store the API key in the session for this user's session
    session["api_key"] = api_key
    
    # redirect to the prompt page
    return render_template("prompt.html")

@app.route("/generate-response", methods=["POST"])
def generate_response():
    # get the prompt from the user
    prompt = request.form["prompt"]
    
    # get the OpenAI response
    openai.api_key = session["api_key"]
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.9,
    ).choices[0].text
    
    # return the response to the user
    return render_template("prompt.html", response=response, prompt=prompt)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
