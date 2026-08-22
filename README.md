# 🔐 Thiranex Password Strength Analyzer


A Python-based Cybersecurity Password Assessment Tool that analyzes password strength using multiple security checks and provides a security score, entropy estimation, password reuse detection, and recommendations for creating stronger passwords.


## 📌 About This Project

**Password Strength Analyzer** is a Python-based cybersecurity application designed to evaluate the security strength of passwords.

It analyzes passwords based on:
* Password length
* Character diversity
* Uppercase and lowercase letters
* Numbers
* Special characters
* Repeated patterns
* Sequential patterns
* Common passwords
* Estimated password entropy

The application generates a **password security score** and classifies the password according to its strength level. It also provides security recommendations to help users create stronger and more secure passwords.

The project includes a **strong password generator** using Python's `secrets` module and a **password reuse detection system** using SQLite.

Passwords are **not stored directly** in the database. Instead, the application converts them into **SHA-256 hashes** before storing them, demonstrating the basic concept of secure credential storage.



## 🎯 Project Objective

The main objectives of this project are:
* Analyze password security
* Identify weak password patterns
* Calculate a password security score
* Estimate password entropy
* Detect commonly used passwords
* Detect repeated and sequential patterns
* Identify password reuse
* Demonstrate password hashing
* Generate strong random passwords
* Provide security recommendations
* Demonstrate practical cybersecurity concepts using Python

---

## 🛠️ Technologies Used

---

| Technology  | Purpose                           |
| ----------- | --------------------------------- |
| **Python**  | Core programming language         |
| **Tkinter** | Graphical User Interface          |
| **SQLite**  | Local password history database   |
| **hashlib** | SHA-256 password hashing          |
| **secrets** | Secure random password generation |
| **re**      | Pattern and character detection   |
| **math**    | Entropy calculation               |
| **string**  | Character set handling            |

---

## ✨ Features

### 🔍 Password Analysis

The application performs multiple password-security checks:

* ✅ Password length
* ✅ Lowercase letters
* ✅ Uppercase letters
* ✅ Numbers
* ✅ Special characters
* ✅ Common password detection
* ✅ Repeated character detection
* ✅ Sequential pattern detection
* ✅ Character diversity analysis
* ✅ Entropy estimation

---

### 🔑 Secure Password Generation

The project uses Python's built-in **`secrets` module** to generate cryptographically stronger random passwords.

Example:
Generated Password:
X7@pL9#vQ2!mR8$k


The generator creates passwords using multiple character categories such as:

* Uppercase letters
* Lowercase letters
* Numbers
* Special characters



### 📊 Security Score
The application calculates a password security score between:

**0 – 100**

|  Score | Strength       |
| -----: | -------------- |
|   0–24 | 🔴 Very Weak   |
|  25–44 | 🟠 Weak        |
|  45–64 | 🟡 Medium      |
|  65–84 | 🟢 Strong      |
| 85–100 | 🟢 Very Strong |

The score is based on multiple password security characteristics rather than password length alone.

---

### 🔐 Password Reuse Detection

The application checks whether a password has already been analyzed before.

If the same password was previously detected, the application displays a warning and recommends using a different password.

For the local password-history feature, the application stores a **SHA-256 hash** rather than the original password.

> **Note:** SHA-256 hashing demonstrates the concept of hashed credential storage, but production password storage should use a dedicated password-hashing algorithm such as Argon2, bcrypt, or scrypt with appropriate salting.

---

## 🔒 Security Concepts Demonstrated

---

This project demonstrates several fundamental cybersecurity concepts:

* Password Security
* Credential Protection
* Password Hashing
* Entropy
* Brute-Force Resistance Concepts
* Pattern-Based Password Analysis
* Secure Random Generation
* Password Reuse Awareness
* Local Database Security
* Security Recommendations

---

## 🔄 Project Workflow

---

```text
        User Enters Password
                ↓
        Password Analysis
                ↓
    ┌───────────┼───────────┐
    ↓           ↓           ↓
 Character    Pattern     Common
  Analysis    Analysis    Password Check
    ↓           ↓           ↓
    └───────────┼───────────┘
                ↓
        Entropy Estimation
                ↓
        Security Score
                ↓
       Strength Classification
                ↓
     Security Recommendations
                ↓
       Password History Check
```

---


🔐 Password Reuse Detection
The application checks whether a password has already been analyzed before.

If the password was previously used, the application displays a warning and recommends using a different password.



## ▶️ How to Use

### Step 1 — Enter Password
Enter a password into the password input field.

### Step 2 — Analyze Password
Click **Analyze Password**.
The application will evaluate the password based on its security characteristics.

### Step 3 — Review Results

View:
* Security score
* Password strength
* Entropy estimation
* Detected weaknesses
* Security recommendations
* Password reuse warning


### Step 4 — Generate Strong Password
Click **Generate Strong Password** to create a secure random password.


### Step 5 — Show / Hide Password
Use the **Eye icon** to show or hide the entered password.



## 🖥️ Application Interface

The application provides a simple **Tkinter-based graphical interface** designed to make password security analysis easy to understand.


The interface allows users to:
* Enter passwords
* Analyze password strength
* View security results
* Generate strong passwords
* Show/hide passwords
* Receive security recommendations

---

## 📈 Security Recommendations

---

Depending on the analysis results, the application can recommend actions such as:

* Increase password length
* Add uppercase characters
* Add lowercase characters
* Add numbers
* Add special characters
* Avoid common passwords
* Avoid repeated characters
* Avoid sequential patterns
* Avoid reusing previously analyzed passwords

---

## ⚠️ Limitations

---

This project is designed for **educational and cybersecurity learning purposes**.

The password score and entropy are estimates and should not be treated as a complete security guarantee.

The project does not perform:

* Real-world credential breach monitoring
* Online password database checking
* Enterprise password-policy enforcement
* Advanced password-cracking simulation
* Multi-factor authentication

---

## 🔐 Security & Ethical Use

---

This project is intended for **educational and defensive cybersecurity purposes**.

Do not use the application to collect, store, or analyze passwords belonging to other users without their permission.

Never use real sensitive passwords for testing if they are intended for an important account.



## 🎓 Internship Project


This project was developed as a **Cybersecurity Internship Project** to demonstrate practical understanding of:

**Password Analysis → Security Scoring → Entropy Estimation → Hashing → Secure Password Generation → Security Recommendations**



## ⭐ Project Purpose
The purpose of this project is to provide a simple, practical tool for understanding how password characteristics affect security and to demonstrate fundamental cybersecurity concepts using Python.


