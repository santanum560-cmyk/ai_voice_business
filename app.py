from flask import Flask, render_template, request, send_file
import edge_tts
import asyncio
import os

app = Flask(__name__)

async def generate_voice(text):
    output = "static/output.mp3"
    communicate = edge_tts.Communicate(
        text=text,
        voice="hi-IN-MadhurNeural"
    )
    await communicate.save(output)
    return output

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        asyncio.run(generate_voice(text))
        return send_file("static/output.mp3", as_attachment=True)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
