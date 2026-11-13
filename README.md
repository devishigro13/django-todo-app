# TASKFLOW
### Make space for what matters.

A simple, thoughtfully designed task management application built with Django.

TaskFlow brings your everyday tasks into one organised space. Create tasks, manage deadlines, track your progress and keep moving forward — one task at a time.

---

## THE IDEA

Productivity shouldn't feel like another task on your list.

TaskFlow is built around a simple idea: make organising your day easier, clearer and less overwhelming.

Whether it's a small reminder or an important deadline, TaskFlow helps you keep everything in one place.

## WHAT YOU CAN DO

| Feature | Description |
|---|---|
| Task Management | Create tasks with titles, descriptions and due dates. |
| Edit Tasks | Update task details whenever plans change. |
| Delete Tasks | Remove tasks you no longer need. |
| Progress Tracking | Keep track of pending and completed tasks. |
| Task Details | View individual task information. |
| User Authentication | Sign up and log in to the application. |
| Dashboard | Get an overview of your tasks. |

## THE TECH STACK

**Backend**
- Python
- Django

**Frontend**
- HTML5
- CSS3

**Database**
- SQLite for local development
- PostgreSQL (Neon) for deployment

**Tools**
- Git and GitHub
- Vercel

## PROJECT STRUCTURE

```text
todo_project/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── tasks/
│   ├── migrations/
│   ├── templates/
│   │   ├── tasks/
│   │   └── registration/
│   ├── static/
│   │   └── tasks/
│   │       └── style.css
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## GETTING STARTED

Follow these steps to run TaskFlow locally.

**1. Clone the repository**

```bash
git clone https://github.com/devishigro13/django-todo-app.git
```

**2. Navigate to the project**

```bash
cd django-todo-app
```

**3. Create a virtual environment**

```bash
python -m venv venv
```

**4. Activate it**

macOS / Linux:
```bash
source venv/bin/activate
```

Windows:
```bash
venv\Scripts\activate
```

**5. Install dependencies**

```bash
pip install -r requirements.txt
```

**6. Set up environment variables**

Create a `.env` file in the project root:

```env
DJANGO_SECRET_KEY=<enter-your-secret-key>
DEBUG=True
```

Keep your secret key private. Never push your `.env` file to GitHub.

**7. Apply database migrations**

```bash
python manage.py migrate
```

**8. Run the development server**

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to open the application.

## APPLICATION PREVIEW

Screenshots of TaskFlow will be added here.

| Home | My Tasks |
|---|---|
| <img width="1350" height="963" alt="image" src="https://github.com/user-attachments/assets/1d92f289-89ec-4ae6-825c-0e9ba33f56c4" /> |<img width="1347" height="943" alt="image" src="https://github.com/user-attachments/assets/a8c15f63-b9f1-45cb-8801-fdbc337b1408" />|

| Completed Tasks | Login |
|---|---|
| <img width="1351" height="972" alt="image" src="https://github.com/user-attachments/assets/cc822d5e-6b1d-4d08-b5e3-0205ab3758e1" />|<img width="1352" height="957" alt="image" src="https://github.com/user-attachments/assets/508e95f8-0110-4d33-a882-4e3c1dfcc957" />| 

## WHAT THIS PROJECT TAUGHT ME

Building TaskFlow gave me practical experience with:

- Django project and app structure
- Models, views and URL routing
- CRUD operations using Django ORM
- Template inheritance and reusable components
- Form handling and validation
- User authentication
- Static files and CSS
- Git and GitHub version control
- Deployment and hosted database configuration

## LIVE APPLICATION

**Live Website:** https://taskivo-eta.vercel.app/

**Source Code:** [GitHub Repository](https://github.com/devishigro13/django-todo-app)

---

### ~ A LITTLE NOTE :))

TaskFlow started as a way to understand Django by building something practical.
What began as a simple to-do list became an opportunity to explore the complete journey of a web application ~ from writing the first model to deploying a live product.

**Less clutter. Clearer priorities. Better flow.**
