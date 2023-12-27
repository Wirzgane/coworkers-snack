
# Coworkers Snack
#### Video Demo:  https://youtu.be/LKHjxDZRR-k
#### Description:
This is a simple Flask web application that helps co-workers to vote for their favorite snack.
1. Project files
   - /app.py: Contains application business for connecting to database, create db tables, and end points for create, read, delete and vote.
   - /templates/index.html: Application markup for snack list, creation form and buttons for delete and vote.
   - /static/index.html.css: Style for most voted snack.
   - /docker-compose.yml: This Docker Compose file sets up a development environment with a Flask web application, a PostgreSQL database, and a PgAdmin interface for database administration.
   - /Dockerfile: This Dockerfile sets up a Python environment, installs dependencies, and configures the environment for running a Flask application.
1. Features
   - Snack Submissions: Users can submit their chosen snack as text for consideration.
   - Voting System: Users can vote for their favorite snack.
   - Display Created Posts: Display a list of snack submissions, sorted by the number of votes they receive.
   - User-Friendly Interface: Design a user-friendly and visually appealing interface for the app, making it easy for users to navigate and interact.
   - Error Handling and Validation: Implement error handling and validation to ensure data integrity and prevent issues like duplicate snack submissions.
   - Data Persistence: Use a database to store snack submissions, votes, and other relevant data.
1. Technologies Used
   - Flask
   - HTML
   - CSS
   - Docker
   - Docker Compose
   - PostgreSQL
   - pgAdmin
1. Installation
   - Clone this repository.
   - Install Docker on your system if it’s not already installed.
   - Navigate to the project directory in your terminal.
   - Run `docker-compose up --build` to start the server.
1. To use the Coworkers Snack App.
   - Open your web browser and navigate to http://localhost:5000.
1. To access pgAdmin.
   - Open your web browser and navigate to http://localhost:5050.
   - Enter the email address and password you set in the docker-compose.yml file under pgadmin service environment variables (PGADMIN_DEFAULT_EMAIL and PGADMIN_DEFAULT_PASSWORD, respectively).
   - Once logged in, click on “Add New Server” under “Quick Links”.
   - In the “General” tab, enter a name for your server (e.g., “Coworkers Snack Database”).
   - In the “Connection” tab, enter the following information:
        1. Host name/address: db
        1. Port: 5432
        1. Maintenance database: snack_db
        1. Username: snack_user
        1. Password: snack_password
        1. Click “Save” to save your changes. You should now be able to view your database in pgAdmin.
            - If you encounter any problem connecting pgAdmin to postgreSql [this video was helpful](https://www.youtube.com/watch?v=2BjrT14Heug&t=471s&ab_channel=AcerTech).

That’s it!
