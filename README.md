
#  KPA-API (Key Performance Area Management System)

This is a simple RESTful API built using **Python** and **Flask** that allows managers to manage **Key Performance Areas (KPAs)** for employees. KPAs are used to evaluate employee performance across different measurable goals.

---

##  What is a KPA?

**KPA** stands for **Key Performance Area**. These are clearly defined objectives or responsibilities assigned to employees — such as attendance, punctuality, sales, productivity — to measure their work performance.

---

##  Features

-  Add a new KPA
-  View all KPAs
-  View a KPA by ID
-  Update a KPA
-  Delete a KPA

---

##  Tech Stack

- **Language**: Python 3  
- **Framework**: Flask  
- **Testing Tool**: Postman

---

##  How to Run This Project

### 1. Clone the Repository

```bash
git clone https://github.com/neemabhandari18/KPA-API.git
cd KPA-API
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

> If you don’t have a `requirements.txt`, you can install Flask directly:  
```bash
pip install flask
```

### 3. Run the Flask App

```bash
python app.py
```

Your API will start on:  
 `http://127.0.0.1:5000`

---

## Testing the API with Postman

To use this API without coding, we recommend using **Postman** — a tool designed for testing APIs.

### Install Postman:

1. Go to: [https://www.postman.com/downloads](https://www.postman.com/downloads)  
2. Download and install the version for your system  
3. Click "Continue without account" to get started

---

##  How to Use This API (for KPA Managers)

You can perform these actions in Postman after the app is running:

|     Action       | Method |             URL               | Body Required|
|------------------|--------|-------------------------------|--------------|
| Add new KPA      | POST   | `http://127.0.0.1:5000/kpa`   |  Yes         |
| View all KPAs    | GET    | `http://127.0.0.1:5000/kpa`   |  No          |
| View one KPA     | GET    | `http://127.0.0.1:5000/kpa/1` |  No          |
| Update a KPA     | PUT    | `http://127.0.0.1:5000/kpa/1` |  Yes         |
| Delete a KPA     | DELETE | `http://127.0.0.1:5000/kpa/1` |  No          |

---

## JSON Body Samples (for Postman)

###    Add a New KPA (POST)

```json
{
  "name": "trackers",
  "description": "Tracks on-time arrival to office"
}
```

###   Update an Existing KPA (PUT)

```json
{
  "name": "Updated KPA Name",
  "description": "Updated description for the KPA"
}
```

---

##  requirements.txt

```
Flask==3.1.1
```

Install using:

```bash
pip install -r requirements.txt
```

---

## 👩‍💻 Author

**Neema Bhandari**  
🎓 BCA Student | 💻 Python Intern  
🔗 GitHub: [@neemabhandari18](https://github.com/neemabhandari18)

---

## 📄 License

This project is for educational and internship use only.
