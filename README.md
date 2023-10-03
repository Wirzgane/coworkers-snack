 # Coworkers Snack
This is a simple Flask web application that allows co-workers to vote for their favorite snack every week. The snack with the most votes at the end of the week is chosen, and the boss gets it at the beginning of the new week.

 ## Features
 - User Authentication: Users can create accounts, log in, and log out. User accounts are required for snack submissions and voting.
 - Snack Submissions: Users can submit their chosen snack as text for consideration. Each user is allowed one snack submission per week.
 - Voting System: Users can vote for their favorite snack once per week. Each user can only vote for one snack per week. Implement a system to prevent fraudulent or multiple votes from the same user.
 - Display Created Posts: Display a list of snack submissions, sorted by the number of votes they receive. Reset the data (truncate) at the end of each week.
 - User Restrictions: Implement restrictions to ensure fair play, such as preventing users from submitting multiple snacks in a week or voting for their own snack.
 - User-Friendly Interface: Design a user-friendly and visually appealing interface for the app, making it easy for users to navigate and interact.
 - Error Handling and Validation: Implement error handling and validation to ensure data integrity and prevent issues like duplicate snack submissions or votes.
 - Data Persistence: Use a database to store user accounts, snack submissions, votes, and other relevant data.
 ## Technologies Used
 - Flask
 - SQLite
 - HTML
 - CSS
 - JavaScript
 - Docker
 - Docker Compose
 - PostgreSQL
 - pgAdmin
 ## Installation
 - Clone this repository.
 - Install Docker on your system if it’s not already installed.
 - Navigate to the project directory in your terminal.
 - Run `docker-compose up --build` to start the server.
 ## Usage
 ### To use the Coworkers Snack App.
  - Open your web browser and navigate to http://localhost:5000.
 ### To access pgAdmin.
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

That’s it!
