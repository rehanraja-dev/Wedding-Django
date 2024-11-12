Django wedding managing Website

This project is a fully functional wedding website built with Django, featuring a full authentication system (registration, login, and logout), along with essential functionalities like product listings, wishlists, shopping carts, and order management. The site includes a user-friendly admin panel to manage products, categories, orders, and customer information.

Features
User Authentication: Registration, login, logout, and password management for secure access.
Product Catalog: Dynamic product [vendor and venue] listing and categorization.
Wishlist: Save favorite products [ venue and vendor ] to a wishlist for future reference.
Shopping Cart: Add, update, or remove items from the cart before checkout.
Order Management: Place orders [vendors] with address management, review order details, and view order history.
Admin Panel: Manage products, categories, users, and orders from Django’s built-in admin interface.
Technologies Used
Backend: Django (Python)
Frontend: HTML, CSS, JavaScript
Database: SQLite (default) or other Django-supported databases
Authentication: Django's built-in authentication system

1. Setup Instructions - Clone the repository:

bash - Copy code

git clone https://github.com/amanraja-dev/Wedding-Django.git

cd Wedding-Django

2. Create a virtual environment also activate virtual env:

bash - Copy code

python -m venv env

env\Scripts\activate // Window command

3. Install dependencies: 

bash - Copy code

pip install -r requirements.txt

4. Start the development server:

bash - Copy code

python manage.py runserver

5. Create a superuser for admin panel access:

bash - Copy code

python manage.py createsuperuser

6. Access the website and admin panel:

Website: Visit  http://127.0.0.1:8000/
Website admin pannel: Visit  http://127.0.0.1:8000/admin


Project folder structure:

Project contain 7 folder and 3 files.

Folder work and containing files are:

1. Cake - This folder is an App in Djnaog used to make seperate models related cake details.
2. Manager - THis folder is an App in Django used to make seperate models related manager details.
3. Media - This folder containe some other folders which is used to store media file like images of product images like , venue , vendors , manager , cake.
4. Static - Contains CSS, JavaScript, and images for frontend styling.
5. Tables - Contains all basic models of the project.
6. Templates - Includes HTML templates for different pages, including product listings, cart, checkout, and user profile.
7. Wedding - Main folder which contian setting.py , views.py and urls.py and others.

8. db.sqlite3 - This is lightweight file based database.
9. manage.py - 
10. requirements.txt - Contian all required dependecies with version.

Contributing
Contributions are welcome! Fork the repository and create a pull request to add features or make improvements.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

IMPORTANT FOR CONTRIBUTION 

Instruct Contributors to Use Feature Branches: Make it clear in your README.md or a CONTRIBUTING.md file that contributors should:

Fork the repository or clone it and create a new branch for their changes (e.g., feature/xyz).
Push their branch to the remote repository (not to main).
Open a pull request (PR) against the main branch for review and merging.

