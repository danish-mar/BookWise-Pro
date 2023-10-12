Based on your requirements, here's a modified schema for a library management system with three main tables: Books, Members (divided into Student and Teacher members), and Transactions. I've also added foreign key relationships to establish associations between these tables:

1. **Books Table**:
   - `id` (auto-increment, primary key)
   - `title` (title of the book)
   - `authorName` (author's name)
   - `publisher` (name of the publisher)
   - `isbn` (International Standard Book Number, unique)
   - `price` (price of the book)
   - `category` (category/genre of the book)
   - `publishYear` (year of publication)
   - `source` (source of the book, e.g., purchase or donation)
   - `date` (auto-generated date added to the library)

```sql
CREATE TABLE Books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    authorName VARCHAR(255) NOT NULL,
    publisher VARCHAR(255),
    isbn VARCHAR(13) UNIQUE NOT NULL,
    price DECIMAL(10, 2),
    category VARCHAR(50),
    publishYear INT,
    source VARCHAR(50),
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

2. **Members Tables (Student and Teacher)**:

   a. **Student Members**:
   - `id` (auto-increment, primary key)
   - `enrollNo` (enrollment number, unique)
   - `name` (name of the student)
   - `dept` (department of the student)
   - `semester` (current semester of the student)
   - `address` (address of the student)

```sql
CREATE TABLE StudentMembers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    enrollNo VARCHAR(15) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    dept VARCHAR(50),
    semester INT,
    address TEXT
);
```

   b. **Teacher Members**:
   - `id` (auto-increment, primary key)
   - `name` (name of the teacher)
   - `dept` (department of the teacher)

```sql
CREATE TABLE TeacherMembers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    dept VARCHAR(50)
);
```

3. **Transactions Table**:
   - `id` (auto-increment, primary key)
   - `dateOfIssue` (date when the book was issued)
   - `accNo` (accession number for the issued book)
   - `author` (foreign key related to `Books.authorName`)
   - `title` (foreign key related to `Books.title`)
   - `dueDate` (due date for returning the book)

```sql
CREATE TABLE Transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dateOfIssue DATE,
    accNo INT,  -- Accession Number
    author VARCHAR(255),  -- Foreign key related to Books.authorName
    title VARCHAR(255),   -- Foreign key related to Books.title
    dueDate DATE
);
```

These tables are structured to help you manage books, members (both students and teachers), and transactions related to book checkouts. You can customize and expand the schema based on your specific needs, such as adding more details to the members or including additional tables for fines, book copies, and more.