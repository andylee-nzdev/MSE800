# Image Loader

A web application that allows users to load and display images from their local system, built with Flask and vanilla JavaScript.

## Features

- Upload images via drag & drop or file browser
- Images are stored on the server in the `uploads/` directory
- Supports PNG, JPG, JPEG, GIF, WebP, BMP, and SVG formats
- 16 MB maximum file size

## Project Structure

```
Activity4/
├── app.py              # Flask backend
├── templates/
│   └── index.html      # Frontend UI
├── uploads/            # Uploaded images (created automatically)
└── README.md
```

## Setup

1. Install Flask:
   ```bash
   pip install flask
   ```

2. Run the application:
   ```bash
   python app.py
   ```

3. Open http://localhost:5000 in your browser.

## API

| Method | Endpoint             | Description                  |
|--------|----------------------|------------------------------|
| GET    | `/`                  | Serves the main page         |
| POST   | `/upload`            | Uploads an image (multipart) |
| GET    | `/uploads/<filename>`| Serves an uploaded image     |
