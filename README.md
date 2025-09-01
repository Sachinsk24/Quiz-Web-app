# MCQ App 🎯

A **Flask-based Multiple Choice Quiz App** that fetches questions dynamically from the [Open Trivia DB](https://opentdb.com/) API and displays results in real-time.

---

## 🚀 Features
- Choose quiz **categories** like Sports, History, Science, and more.
- Dynamic **question and answer** loading from API.
- Interactive **Bootstrap-based UI**.
- Real-time **score calculation**.
- Works locally and can be shared via **ngrok**.

---

## 🛠️ Tech Stack
- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS, Bootstrap  
- **API:** Open Trivia DB  
- **Deployment (local tunneling):** ngrok  

---

## 📦 Installation

## Create a virtual environment
```bash
python -m venv venv
Activate the virtual environment
On Windows:
venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate

Install dependencies
pip install -r requirements.txt

▶️ Run Locally
python app.py


App will run at:

http://127.0.0.1:5000

🌍 Share Publicly with ngrok
Start Flask server:
python app.py

Then open another terminal:
ngrok http 5000


Use the generated https://xxxx.ngrok-free.app
 URL to share the app.

## 📁 Project Structure
MCQ App/
├── app.py              # Main Flask app
├── templates/          # HTML templates
│   ├── index.html
│   ├── quiz.html
│   └── result.html
├── static/             # CSS, JS, or images (if any)
├── requirements.txt    # Python dependencies
└── README.md           # Documentation

🤝 Contributing

Pull requests are welcome.
For major changes, please open an issue first to discuss what you’d like to change.

📜 License

This project is free to use under the MIT License.

💡 Credits

Flask

Open Trivia DB

ngrok
