# Python FastAPI Authorization Solution
In this app we have setup the JWT authentication for a simple boilerplate application. We have 2 simple models + a user model and respective controllers with serializers to use as a jump off point. We have also included alembic for database migration, with the initial migration already setup to migrate the user model.

Once this base project is setup, please review and follow the post install documentation:
> [Managing Migrations](https://github.com/Dujota/FastAPI-SQLAlchemy-Migrations-Guide)
> 
> [Setting up CORS for FastAPI](https://github.com/Dujota/FastAPI-CORS-Guide)
> 
> [Deploying to Heroku](https://github.com/Dujota/FastAPI-Heroku-Deployment-Guide)

## Getting Started

## Cloning the Auth boilerplate

Clone this repo down to your machine so you can start the setup stage for your new project: 

```bash
git clone https://github.com/Dujota/fast-api-jwt-auth-template-example.git
```

Once we have the repository on our machines, we can change the name of the directory to `'express-api-hoot-back-end'`:

```bash
mv fast-api-jwt-auth-template-example <YOUR_APP_NAME>
```

Next, `cd` into your renamed directory:

```bash
cd <YOUR_APP_NAME>
```

Finally, remove the existing `.git` information from this template:

```bash
rm -rf .git
```

> Removing the `.git` info is important as this is just a starter template provided gere. You do not need the existing git history for this project.

## GitHub setup

To add this project to GitHub, initialize a new Git repository:

```bash
git init
git add .
git commit -m "init commit"
```

Make a new repository on [GitHub](https://github.com/) named `<YOUR_PROJECT_NAME>`.

Link your local project to your remote GitHub repo:

```bash
git remote add origin https://github.com/<github-username>/<YOUR_PROJECT_NAME>.git
git push origin main
```

> 🚨 Do not copy the above command. It will not work. Your GitHub username will replace `<github-username>` (including the `<` and `>`) in the URL above.

Open the project's folder in your code editor:

```bash
code .
```

3. Install dependencies (this also creates the virtual environment if it doesn’t exist):

```sh
 pipenv install
```

4. Activate the virtual environment:

```sh
 pipenv shell
```

5. Set up your PostgreSQL database:

   - Ensure PostgreSQL is installed and running on your machine.
   - Create a database named `teas_db` if it does not already exist:

```bash
createdb YOUR_APP_DB
```

6. Open the application in Visual Studio Code:

```bash
code .
```

7. The database connection string is defined in the `config/environment.py` file which uses environment variables:
   > create a `.env` file in the root of your project and add the below variables

```python
DB_URI=db_URI = "postgresql://<username>@localhost:5432/<YOUR_APP_DB>"
JWT_SECRET=YOUR_SECRET_KEY
```

> _Modify your database connection string to use your username as the `<username>`._

8. Seed the database with initial data:

   - Run the `seed.py` file to reset the database by dropping existing tables and repopulating it with starter data:

```bash
pipenv run python seed.py
```

> You should see output indicating the database was successfully seeded. If there are any errors, check the `db_URI` in the `config/environment.py` file.

9. Start the development server:

```bash
pipenv run uvicorn main:app --reload
```

> You should now have the app running. Visit [`http://127.0.0.1:8000`](http://127.0.0.1:8000) in your browser to confirm it’s working.

10. Now you can test each endpoint using FastAPI’s built-in documentation.

> Navigate to FastAPI Documentation: Open [`http://localhost:8000/docs`](http://localhost:8000/docs) in your browser.

<br>

### Troubleshooting PostgreSQL

- The database connection string is defined in the `config/environment.py` file:

  ```python
  db_URI = "postgresql://<username>@localhost:5432/teas_db"
  ```

- Ensure your PostgreSQL instance is configured to allow connections with the provided credentials.
- **_Modify your database connection string to use your username as the `<username>`._**

#### Setting Up a User in PostgreSQL

To connect to a specific PostgreSQL user, use the following command:

```sh
psql -U <username>
```

#### Handling "Role Does Not Exist" Error

If you see this error:

```sh
Error: FATAL: role "<username>" does not exist
```

it means that the specified user does not exist in PostgreSQL.

#### Creating a New PostgreSQL User

To create the user, run the following command inside `psql`:

```sql
CREATE ROLE "<username>" WITH LOGIN PASSWORD 'your_secure_password';
```

> 🔹 **Replace** `<username>` with your desired username and **choose a secure password**.

This will allow you to connect using one of the following database connection strings:

#### Connection Strings:

If **no password is required**:

```python
db_URI = "postgresql://<username>@localhost:5432/YOUR_APP_DB"
```

If **a password is required**:

```python
db_URI = "postgresql://<username>:<your_secure_password>@localhost:5432/YOUR_APP_DB"
```

This ensures that PostgreSQL correctly authenticates and allows access to the `YOUR_APP_DB` database.
