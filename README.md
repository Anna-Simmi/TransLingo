
# TransLingo

[![Python](https://img.shields.io/badge/Python-3.13-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.1-orange)](https://flask.palletsprojects.com/)

A web application that translates text into multiple languages using Google Translate API. Built with Flask and deployed online for public use.

---

## 🌐 Live Demo
Try the app online: [TransLingo](https://translingo-tmlh.onrender.com)

---

## 🚀 Features
- Translate text into multiple languages simultaneously.
- Automatic language detection.
- Simple and user-friendly interface.
- Fully deployed online for public access.

---

## 🛠 Technologies Used
- **Python** – Core programming language  
- **Flask** – Web framework  
- **deep-translator** – Translation library  
- **Gunicorn** – WSGI HTTP server for deployment  
- **HTML / CSS / JavaScript** – Frontend  
- **Render** – Hosting platform  

---

## 💾 Installation

To run the app locally:

1. **Clone the repository:**  
```bash
git clone https://github.com/Anna-Simmi/TransLingo.git
````

2. **Navigate to the project folder:**

```bash
cd TransLingo
```

3. **Create a virtual environment:**

```bash
python -m venv venv
```

4. **Activate the virtual environment:**

* On Windows:

```bash
venv\Scripts\activate
```

* On Mac/Linux:

```bash
source venv/bin/activate
```

5. **Install dependencies:**

```bash
pip install -r requirements.txt
```

6. **Run the app:**

```bash
python app.py
```

7. **Open in your browser:**
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📝 Usage

1. Enter the text you want to translate.
2. Select one or more target languages.
3. Click **Translate** to get the translated results.

---

## ⚙️ Deployment on Render

* Use `gunicorn app:app` as the start command.
* Set Python version in Render to match your `requirements.txt`.
* Your app will be live at a Render-provided URL.

---

## 📁 Project Structure

```
TransLingo/
│
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # HTML template
└── README.md           # Project documentation
```

---

## 🙌 Contributing

Contributions are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Add feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a Pull Request

---

## 🌐 Connect With Me

<p align="center">
  <a href="https://github.com/Anna-Simmi"><img src="https://img.shields.io/badge/GitHub-%23121011.svg?&style=for-the-badge&logo=github&logoColor=white" /></a>
  <a href="https://www.linkedin.com/in/anna-simmi-m-d-797ba8339"><img src="https://img.shields.io/badge/LinkedIn-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" /></a>
  <a href="annasimmim@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" /></a>
</p>  





