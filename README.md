# 🍽️ Restaurant Management System (RMS)

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
├── assets/                # Static assets like icons, images, logos
├── controllers/           # Handles business logic; connects models with views
├── database/              # DB scripts and schema initialization
├── docs/                  # Project documentation, architecture diagrams
├── gui/                   # GUI components if using Flet
├── logs/                  # Log files for debugging and monitoring
├── models/                # Database models/entities
├── reports/               # PDF reports, receipts, or print templates
├── scripts/               # Automation scripts (e.g., backups, seeds)
├── tests/                 # Unit and integration tests
├── ui/                    # UI layout and theming
├── utils/                 # Helper functions and utilities
├── .env                   # Environment variables (e.g., DB_PATH, API_KEYS)
├── CHANGELOG.md           # Tracks changes and version history
├── LICENSE                # License file (Apache 2.0)
├── requirements.txt       # Python dependencies
├── README.md              # Project overview, setup, and usage
└── run.py                 # Application entry point
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
