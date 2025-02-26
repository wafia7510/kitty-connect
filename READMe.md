
# **🐾 Kitty Connect** – *Find Your Purr-fect Companion!*

### **📍 Project Overview**
Kitty Connect is a **Django-powered** full-stack web application that simplifies **cat adoption** by providing a seamless platform where users can **browse, favorite, apply for adoption, and track adoption requests** while **admins manage cats and adoption approvals**. The project follows an **MVC (Model-View-Controller) pattern**, incorporating authentication, role-based access, and business logic to ensure smooth operations.

---

## **🚀 Features**
### **For Users**
✅ Browse available cats for adoption  
✅ View cat details (image, age, breed, description)  
✅ Apply for adoption with a message  
✅ Track adoption request status  
✅ Favorite/Wishlist feature to save cats for later  
✅ View past adoption history  
✅ Secure user authentication (Register/Login/Logout)  

### **For Admins**
✅ Add, edit, and delete cat listings  
✅ Manage adoption requests (approve/reject)  
✅ Remove an adopted cat from availability  
✅ Prevent users from reapplying for rejected cats for **6 months**  
✅ Auto-redirect admins to **admin dashboard** upon login  

---

## **💻 Tech Stack**
✅ **Frontend:** HTML, CSS, Bootstrap  
✅ **Backend:** Python + Django  
✅ **Database:** SQLite (upgradable to PostgreSQL/MySQL)  
✅ **Authentication:** Django’s built-in authentication  
✅ **Deployment:** Will be cloud-hosted (TBD)  
✅ **Version Control:** Git & GitHub  

---

## **📂 Project Structure**
```
KittyConnect/
│── accounts/                # User authentication & dashboard
│── cats/                    # Cat model & listing functionalities
│── adoption/                # Adoption request handling
│── static/                  # CSS, images, JavaScript files
│── templates/               # HTML templates for the website
│── manage.py                # Django management script
│── db.sqlite3               # Database (default: SQLite)
│── README.md                # Project documentation
│── requirements.txt         # Project dependencies
```

---

## **⚙️ Installation & Setup**
To run this project locally, follow these steps:

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/KittyConnect.git
cd KittyConnect
```

### **2️⃣ Create & Activate a Virtual Environment**
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Apply Database Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

### **5️⃣ Create a Superuser (for Admin Access)**
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin account.

### **6️⃣ Run the Server**
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

---

## **🛠️ Admin Panel Access**
To access the Django Admin Panel:
1. **Login as a superuser** (`http://127.0.0.1:8000/admin`)
2. **Manage cat listings & adoption requests**

---

## **📜 Database & Models**
The application uses Django's **ORM (Object Relational Mapper)** to handle data storage.  

### **🔹 Cat Model**
- `name`: Name of the cat  
- `breed`: Breed of the cat  
- `age`: Age of the cat  
- `description`: Brief description  
- `image`: Cat's image  
- `available`: Boolean flag (available for adoption or not)  

### **🔹 AdoptionRequest Model**
- `user`: Reference to the user applying  
- `cat`: Reference to the cat being adopted  
- `message`: User's reason for adoption  
- `status`: Pending, Approved, or Rejected  
- `request_date`: Date of application  

---

## **🔍 Assessment Compliance Checklist**
Below is an **evaluation of missing & completed requirements** based on the Full-Stack Toolkit **Assessment Guide**.

| Requirement | Status | Notes |
|-------------|--------|---------|
| **1. MVC & Agile Methodology** | ✅ | Django follows MVC, Agile tool (Trello/GitHub Projects) needed for tracking |
| **2. Database Design & Models** | ✅ | Cat & AdoptionRequest models implemented |
| **3. Authentication & Authorization** | ✅ | Role-based login with restricted access (user/admin) |
| **4. Frontend Design (UX & Accessibility)** | ✅ | Bootstrap, CSS, and ARIA labels included |
| **5. CRUD Operations** | ✅ | Users & admins can create, read, update, and delete records |
| **6. Testing (Manual/Automated)** | ❌ | **Testing needs implementation (Unit Tests)** |
| **7. Version Control (Git & GitHub)** | ✅ | Used for development and commits are tracked |
| **8. Deployment (Cloud Hosting)** | ❌ | **Deployment to a cloud service (e.g., Heroku, Render) required** |
| **9. API Integration** | ❌ | **No API features yet (optional for extra points)** |
| **10. README & Documentation** | ✅ | README structured for future updates |
| **11. Security Features (Env Variables, Debug Mode Off, No Hardcoded Secrets)** | ❌ | **Environment variable handling missing** |
| **12. UX Documentation (Wireframes, Mockups, User Stories)** | ❌ | **Wireframes & Agile planning missing** |

### **🚨 Missing Features that Need to be Fixed**
- **Testing Implementation** (Unit Tests for Views, Forms, Models)  
- **Deployment** (Push to **Heroku, Render, or DigitalOcean**)  
- **Environment Variables Security** (Store API keys & secrets in `.env`)  
- **UX Documentation** (Create **wireframes, user journey & flow diagrams**)  
- **Advanced Features** (APIs, real-time notifications, or a chatbot)  

---

## **📸 Screenshots & Demo**
**(To be added once UI is finalized and deployed)**  
- Homepage  
- Cat Listings  
- Adoption Request Form  
- Admin Dashboard  

---

## **🔬 Testing**
**Manual Testing (Completed)**
✔️ Tested user authentication (Register/Login/Logout)  
✔️ Verified role-based access (Users/Admins)  
✔️ Checked all CRUD operations (Create, Update, Delete)  

**Automated Testing (To Be Implemented)**
❌ Django Unit Tests (Models, Views, Forms)  
❌ JavaScript Testing (If applicable)  

---

## **🛠 Future Improvements**
✔️ **User Profiles** (Allow users to edit their details)  
✔️ **Search & Filter** (Find cats by age, breed, or name)  
✔️ **Email Notifications** (Send emails on request approval/rejection)  
✔️ **Adoption Status Tracker** (Show progress in steps)  
✔️ **Better UI/UX** (Enhance design & accessibility)  

---

## **🌍 Deployment**
*(To Be Documented Once the Site is Deployed)*  
Steps for **Heroku, AWS, or Render** deployment will be updated here.

---

## **📜 License**
This project is open-source under the **MIT License**.

---

## **💬 Contact**
For questions, feel free to reach out:  
📧 **Email:** your@email.com  
🐱 **GitHub:** [yourusername](https://github.com/yourusername)  

---

