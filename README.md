# 🏥 Django Assignment: Building a Healthcare Backend

## 📌 Objective
The goal of this assignment is to create a backend system for a healthcare application using **Django**, **Django REST Framework (DRF)**, and **PostgreSQL**. The system should allow users to register, log in, and manage patient and doctor records securely.

---

## 🛠️ Tech Stack

- **Backend**: Django, Django REST Framework (DRF)  
- **Database**: PostgreSQL  
- **Authentication**: JWT (via `djangorestframework-simplejwt`)  
- **Tools**: Python, Postman (for API testing)

---

## ✅ Requirements

- Set up a Django project with DRF.
- Use PostgreSQL as the primary database.
- Implement JWT authentication with `djangorestframework-simplejwt`.
- Create RESTful API endpoints for managing:
  - Users (Registration/Login)
  - Patients
  - Doctors
  - Patient-Doctor mappings
- Use Django ORM for modeling.
- Handle validation and errors gracefully.
- Store sensitive configurations using environment variables.

---

## 📋 API Endpoints

### 1. **Authentication APIs**
- `POST /api/auth/register/` – Register a new user  
- `POST /api/auth/login/` – Log in and receive a JWT token

### 2. **Patient Management APIs**
- `POST /api/patients/` – Add a new patient (**Authenticated**)  
- `GET /api/patients/` – Get all patients of the authenticated user  
- `GET /api/patients/<id>/` – Get patient details  
- `PUT /api/patients/<id>/` – Update patient details  
- `DELETE /api/patients/<id>/` – Delete a patient  

### 3. **Doctor Management APIs**
- `POST /api/doctors/` – Add a new doctor (**Authenticated**)  
- `GET /api/doctors/` – Get all doctors  
- `GET /api/doctors/<id>/` – Get doctor details  
- `PUT /api/doctors/<id>/` – Update doctor details  
- `DELETE /api/doctors/<id>/` – Delete a doctor  

### 4. **Patient-Doctor Mapping APIs**
- `POST /api/mappings/` – Assign a doctor to a patient  
- `GET /api/mappings/` – Get all patient-doctor mappings  
- `GET /api/mappings/<patient_id>/` – Get doctors assigned to a patient  
- `DELETE /api/mappings/<id>/` – Remove a doctor from a patient  

---

## 🧪 Testing

- Use **Postman** or any API client to test endpoints.
- Include JWT tokens in the Authorization header (`Bearer <token>`) for protected routes.

---

## 🎯 Expected Outcome

- Secure JWT-based authentication
- Full CRUD operations for patients and doctors
- Mapping system to assign doctors to patients
- PostgreSQL-backed data persistence
- Clean and RESTful API structure

---

