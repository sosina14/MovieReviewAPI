# **Movie Review API**

## **Project Description**
The Movie Review API allows users to browse, create, and manage reviews for movies. This project demonstrates the use of Django and Django REST Framework to create a scalable, RESTful API.

## **Features**
- CRUD operations for movies and reviews.
- JWT-based authentication.
- Filtering and searching for movies and reviews.
- Pagination for large datasets.

---

## **Setup Instructions**

### **Prerequisites**
Ensure the following are installed on your system:
- Python (version 3.9+ recommended)
- pip (Python package manager)
- Git

### **Steps to Set Up the Project**
1. **Clone the Repository**  
   ```bash
   git clone <repository-url>
   cd moviereview
   ```

2. **Set Up a Virtual Environment**  
   ```bash
   python -m venv venv
   ```
   Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**  
   Install all required libraries using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**  
   Set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Development Server**  
   Start the Django server:
   ```bash
   python manage.py runserver
   ```
   Access the API at [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## **API Endpoints**
| Method | Endpoint                | Description                   |
|--------|-------------------------|-------------------------------|
| GET    | `/api/test/`            | Test endpoint                 |
| POST   | `/api/movies/`          | Add a new movie               |
| GET    | `/api/movies/`          | Get all movies                |
| GET    | `/api/movies/{id}/`     | Get a single movie by ID      |
| PUT    | `/api/movies/{id}/`     | Update a movie by ID          |
| DELETE | `/api/movies/{id}/`     | Delete a movie by ID          |

---

## **Dependencies**
This project uses the following Python libraries:
- Django
- Django REST Framework
- djangorestframework-simplejwt
- django-filter

For a complete list, see the `requirements.txt` file.

---

## **License**
This project is open-source and available under the MIT License.


## **Author**
Created by Sosina Ayele. For any inquiries, feel free to contact me at [sosiayu14@example.com].

