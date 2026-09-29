# 🏥 Patient Billing System – Python OOP

A simple **Patient Billing System** built using **Python Object-Oriented Programming (OOP)** concepts.

This project allows users to store patient details, check patient age and bill amount, display patient information, and update the patient's bill amount.

## 📌 Project Overview

The project uses a Python class named `Paitents` to manage patient information.

The program stores:

* Patient ID
* Patient Name
* Patient Age
* Disease
* Bill Amount

The user can then perform different operations through a menu-driven program.

## 🛠️ Technologies Used

* **Python 3**
* Classes and Objects
* Constructor `__init__()`
* Encapsulation
* Private variables
* Methods
* Conditional statements
* `while` loop
* User input
* Arithmetic operators

## ✨ Features

### 1. Check Patient Age

Checks whether the patient's age is greater than zero.

```text
1.check age:

enter a check: 1
Paitent age: 25
```

### 2. Check Bill Amount

Checks whether the patient's bill amount is valid.

```text
2.enter the amount:

enter a check: 2
amount: 5000
```

### 3. Display Patient Details

Displays all patient information.

```text
3.display detials:

enter a check: 3

paitent id: 101
paitent name: Arun
paitent age: 25
paitent disease: Fever
remaining amount: 5000
```

### 4. Update Bill Amount

Allows the user to add a new bill amount to the existing amount.

```text
4.update bill amount:

enter a check: 4
enter a new bill amount2000
current amount: 7000
```

## 🧠 OOP Concepts Used

### Class

The `Paitents` class represents a patient.

```python
class Paitents:
```

### Constructor

The `__init__()` method initializes patient information.

```python
def __init__(self, paitentid, name, age, disease, amount):
```

### Encapsulation

Patient data is stored using private attributes:

```python
self.__id
self.__name
self.__age
self.__disease
self.__amount
```

The double underscore `__` makes these attributes private.

### Object

An object is created using:

```python
obj = Paitents(paitentid, name, age, disease, amount)
```

### Methods

The class contains different methods for different operations:

| Method       | Purpose                 |
| ------------ | ----------------------- |
| `agee()`     | Check patient age       |
| `amounts()`  | Check bill amount       |
| `displays()` | Display patient details |
| `update()`   | Update bill amount      |

## ▶️ How to Run

### 1. Install Python

Make sure Python 3 is installed.

Check the version:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/patient-billing-system.git
```

### 3. Open the Project

```bash
cd patient-billing-system
```

### 4. Run the Program

```bash
python patient.py
```

## 💻 Sample Input

```text
enter a id: 101
enter a paitent name: Arun
enter a age: 25
enter a disease: Fever
enter a amount: 5000
```

## 📋 Sample Menu

```text
1.check age:
2.enter the amount:
3.display detials:
4.update bill amount:

enter a check:
```

## 🔄 Program Flow

```text
Start
  ↓
Enter Patient Details
  ↓
Create Patient Object
  ↓
Display Menu
  ↓
Choose an Option
  ↓
┌──────────────────────┐
│ 1 → Check Age        │
│ 2 → Check Amount     │
│ 3 → Display Details  │
│ 4 → Update Bill      │
└──────────────────────┘
  ↓
Repeat Menu
```

## 🚀 Future Improvements

The project can be improved by adding:

* Patient record search
* Patient record deletion
* Multiple patient records
* Doctor information
* Appointment management
* Medicine charges
* Automatic total bill calculation
* Exception handling
* File/database storage
* Better input validation

## 📚 Learning Outcome

This project helps beginners understand:

* How to create a **class**
* How to create **objects**
* How constructors work
* How **private variables** work
* How methods are used
* How encapsulation works
* How to create a menu-driven Python application
* How OOP can be applied to a real-world problem



