# 🍽️ Restaurant Reservation & Food Delivary System

A desktop-based Restaurant Management System developed using Python, SQLite3, and Flet to streamline restaurant operations such as order processing, billing, inventory tracking, and staff management. This system is designed for single-user use and works offline, offering an efficient and user-friendly experience for restaurant administrators.

---



## 🚀 Features

* **Home Dashboard** – Overview of restaurant activity and quick navigation.
* **Order Management** – Take, update, and delete customer orders with ease.
* **Billing System** – Automatically generate and print invoices using ReportLab.
* **Menu Management** – Add, update, and remove items from the food and beverage menu.
* **Inventory Tracking** – Monitor stock levels of ingredients and supplies.
* **Staff Management** – Manage staff details, roles, and work schedules.
* **Table Allocation** – Track available and occupied tables in real-time.
* **Expense Monitoring** – Record and manage daily operational expenses.
* **Reports** – Generate detailed reports for sales, inventory, and staff attendance.



---

## 🛠️ Tech Stack

* **Python** – Core language for backend logic.
* **SQLite3** – Lightweight, embedded database for local data storage.
* **SQLAlchemy** – SQL toolkit and Object-Relational Mapping (ORM) library for database management.
* **Flet** – Modern UI framework for creating a responsive desktop interface.
* **ReportLab** – PDF generation library used for invoices and reporting.

---



## 🧑‍💻 Installation

### Clone the Repository

```
git clone https://github.com/your-username/restaurant-management-system.git
cd restaurant-management-system
```

### Create a Virtual Environment

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **Install Dependencies**

```
pip install -r requirements.txt
```

### Run the Application

```
python run.py
```


---

## 📂 Project Structure

```
rms/
├── assets/                # Static files like icons, images, and logos used in the UI
├── controllers/           # Business logic and event handling; connects models with views
├── database/              # Database connection setup, schema definitions, and init scripts
├── docs/                  # Project documentation, system architecture, and diagrams
├── views/                 # Visual layout components rendered using Flet
├── logs/                  # Application logs for error tracking and debugging
├── models/                # ORM models (e.g., SQLAlchemy classes) representing DB tables
├── reports/               # PDF templates and generated reports using ReportLab
├── scripts/               # Automation scripts (e.g., data backup, database seeding)
├── tests/                 # Unit and integration tests to ensure code reliability
├── ui/                    # UI definitions including theming, layout, and reusable widgets
├── utils/                 # Helper functions and shared utility methods
├── .env                   # Environment variables (e.g., DB paths, secrets); not committed
├── CHANGELOG.md           # Document tracking all notable changes and version history
├── CODE_OF_CONDUCT.md     # Guidelines for contributor behavior and community standards
├── CONTRIBUTING.md        # Instructions and best practices for contributing to the project
├── LICENSE                # Legal license of the project (e.g., Apache 2.0)
├── requirements.txt       # Python package dependencies for the project
├── README.md              # Main project overview, features, setup, and usage guide
└── run.py                 # Main entry point to run the application

```

---

## 📄 License

This project is licensed under the APACHE **License** — see the [LICENSE](LICENSE "Apache License") file for more details.

---



## 🤝 Contributing

We welcome contributions to improve the Restaurant Management System! To contribute, please follow the guidelines outlined in the [CONTRIBUTING.md](CONTRIBUTING.md "Contributing file") file.

To get started, you can:

1. Fork the repository
2. Clone your fork locally
3. Create a new branch for your changes
4. Make your improvements or fixes
5. Submit a pull request with a clear description of the changes

We appreciate your help in making this project better!

---



## 🙌 Acknowledgments

Special thanks to the open-source community and the Python ecosystem for providing the tools and libraries that made this project possible.
