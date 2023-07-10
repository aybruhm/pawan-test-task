# Task Duration: 30 mins

Create a simple TODO list application using Django. The application should have the following features:

* User Authentication: Users should be able to register and log in.

* TODO List: Authenticated users should be able to create, view, edit, and delete TODO items. Each TODO item should have a title, description, and a completion status.
(You can create the interface using bootstrap. Nothing too fancy.)

* List View: Display the list of TODO items in a paginated view, showing only the title and completion status.

* Admin Panel: There should be an admin panel accessible only to superusers. Superusers should be able to manage TODO items through the admin panel.

Publish the code in public github repo and send me the link.

## Get Started

To get it running on your local machine, follow the steps below:

1. Run the commands below in your terminal:

```bash
git clone https://github.com/aybruhm/pawan-test-task.git
```

2. Change directory to pawan-test-task:

```bash
cd pawan-test-task
```

3. Create virtual environment, activate and install the requirements with the command below:

```bash
python3.x -m virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

4. Run the development server with

```bash
python manage.py runserver
```

5. Launch your browser and navigate to:

```bash
http://127.0.0.1:8000
```


## Admin Credentials

username: admin
password: admin
