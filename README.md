# Flask S3 File Uploader

A simple Flask application that lets users upload files to an AWS S3 bucket using `boto3`.

## 🔧 Features

- 📤 Upload any file to your configured S3 bucket
- 🔐 Uses environment variables for AWS credentials
- ⚠️ Handles common upload errors with user-friendly messages
- 🖥️ Easy to run locally for testing or extension

## 📁 Project Structure

```
python_s3/
├── main.py              # Flask app
├── templates/
│   └── upload.html      # HTML upload form
├── .env                 # (Not committed) AWS credentials
├── .gitignore
└── README.md
```

## 🧪 Setup Instructions

### 1. Clone this repository

```bash
git clone https://github.com/yourusername/flask-s3-uploader.git
cd flask-s3-uploader
```

### 2. (Optional) Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install dependencies

```bash
pip install flask boto3 python-dotenv
```

> If using `requirements.txt`:
> ```bash
> pip install -r requirements.txt
> ```

## 🔐 Configure `.env` File

Create a file called `.env` in the root of the project:

```
AWS_ACCESS_KEY_ID=your_access_key_id
AWS_SECRET_ACCESS_KEY=your_secret_access_key
S3_BUCKET_NAME=your_bucket_name
```

> ⚠️ **Never commit your `.env` file to GitHub**

## 🚀 Run the App

```bash
python main.py
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## 📦 Deployment Notes

- This is for development use only.
- Use a WSGI server (like Gunicorn) for production.
- Secure your `.env` and avoid hardcoded secrets.
- Add CORS and HTTPS if deploying for web clients.

## ✅ TODO (Suggestions)

- [ ] List uploaded files from S3
- [ ] Generate unique filenames to prevent overwriting
- [ ] Add file size/type validation
- [ ] Support download links

## 📄 License

This project is open-sourced under the MIT License.
