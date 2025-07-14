# KPA-API

# KPA Management API

This is a simple RESTful API built using Python and Flask to manage **KPA (Key Performance Areas)** for employees.

## What is KPA?

KPA stands for **Key Performance Area** – specific goals or performance indicators that help evaluate an employee's contribution in a company.

---

## Features

- Add a new KPA  
- Get all KPAs  
- Get a KPA by ID  
- Update a KPA  
- Delete a KPA  

---

## Tech Stack

- Language: **Python 3**
- Framework: **Flask**

---

##  How to Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/neemabhandari18/KPA-API
   cd kpa-api



## Author

**Neema Bhandari**  
📚 BCA Student | 💻 Python Intern  
🔗 GitHub: [@neemabhandari18](https://github.com/neemabhandari18)


   --------------------------------------------------
                   INSTALL POSTMAN 
   --------------------------------------------------



   ## 🧪 API Testing Tool Required

To test this Flask API, we recommend using **Postman** – a free and powerful API testing tool.

### How to Install Postman

1. Go to the official website:  
   [https://www.postman.com/downloads](https://www.postman.com/downloads)

2. Download and install the version suitable for your operating system (Windows/macOS/Linux).

3. Open the app and click on **"Continue without account"** to start using Postman immediately.

---

###  How to Use Postman for Testing

- `POST` → Add a new KPA:  
  URL: `http://127.0.0.1:5000/kpa`

  Body → raw → JSON:
  ```json
  {
    "name": "Attendance",
    "description": "Tracks daily presence"
  }




