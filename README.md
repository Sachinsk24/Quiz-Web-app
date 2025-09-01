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

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/MCQ-App.git
cd MCQ-App

2️⃣ Create a virtual environment
python -m venv venv

3️⃣ Activate the virtual environment

On Windows:

venv\Scripts\activate


On macOS/Linux:

source venv/bin/activate

4️⃣ Install dependencies
pip install flask requests

▶️ Run Locally
python app.py


Your app will be running at:

http://127.0.0.1:5000

🌍 Share Publicly with ngrok

Start your Flask server:

python app.py


In another terminal:

ngrok http 5000


Copy the generated https://xxxx.ngrok-free.app
 URL and share it.

📁 Project Structure
MCQ App/
├── app.py              # Main Flask app
├── templates/          # HTML templates
│   ├── index.html
│   ├── quiz.html
│   └── result.html
├── static/             # CSS, JS, or images (if any)
└── README.md           # Documentation

🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

📜 License

This project is free to use under the MIT License.

💡 Credits

Flask

Open Trivia DB

ngrok


---

### **Steps to add this to your repo**
1. Create the file:
   ```powershell
   notepad README.md


Paste the content above and save.

Commit and push:

git add README.md
git commit -m "Added README.md"
git push


Would you like me to also generate a requirements.txt file to make it easier to install dependencies on another system?

You said:
yes
ChatGPT said:

Here’s a requirements.txt file for your MCQ App to make installation easier on any system.

requirements.txt
Flask==3.0.0
requests==2.31.0

Steps to create and use it
1. Create the file

In your project folder:

notepad requirements.txt


Paste the above content and save.
