# HOW TO USE
## 1. Create a postgres database
## 2. Create a .env file with the following sample
<br />

#### **ENV CONFIG SAMPLE**

DB_NAME=database-name \
DB_USER=database-username \
DB_PASS=database-password \
host=hostname \
port=port

#### **Database table names**
### **Creating the database tables during step 1. is optional**

ANIME_TABLE_NAME=anime \
MANGA_TABLE_NAME=manga

#### **Allowed HTTP Methods**

*ONLY PUT METHODS YOU WANT TO ALLOW*

ALLOWED = ['GET', 'POST', 'PUT', 'DELETE']


