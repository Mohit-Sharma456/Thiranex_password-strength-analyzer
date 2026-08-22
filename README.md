# Thiranex_password-strength-analyzer

🔐 Password Strength Analyzer
A Python-based Cybersecurity Password Assessment Tool that analyzes password strength using multiple security checks and provides a security score, entropy estimation, password reuse detection, and recommendations for creating stronger passwords.


📌 About This Project
Password Strength Analyzer is a Python-based cybersecurity application designed to evaluate the security strength of passwords. It analyzes passwords based on length, character diversity, uppercase/lowercase letters, numbers, special characters, repeated patterns, sequential patterns, common passwords, and estimated entropy.

The application generates a password security score and classifies the password according to its strength level. It also provides security recommendations to help users create stronger and more secure passwords.

The project includes a strong password generator using Python's secrets module and a password reuse detection system using SQLite. Passwords are not stored directly in the database. Instead, the application converts them into SHA-256 hashes before storing them, demonstrating the basic concept of secure credential storage.


🎯 Project Objective
The main objectives of this project are:

To analyze password security.
To identify weak password patterns.
To calculate a password security score.
To estimate password entropy.
To detect commonly used passwords.
To detect repeated and sequential patterns.
To identify password reuse.
To demonstrate password hashing.
To generate strong random passwords.
To provide users with security recommendations.
To demonstrate practical cybersecurity concepts using Python.
🛠️ Technologies Used


Technology Purpose
Python Core programming language
Tkinter Graphical User Interface
SQLite Local password history
hashlib SHA-256 hashing
secrets Secure random password generation
re Pattern and character detection
math Entropy calculation
string Character sets

✨ Features 🔍 Password Analysis

The application performs multiple password-security checks:

✅ Password length
✅ Lowercase letters
✅ Uppercase letters
✅ Numbers
✅ Special characters
✅ Common password detection
✅ Repeated character detection
✅ Sequential pattern detection
✅ Character diversity analysis
✅ Entropy estimation


🔑 Secure Password Generation
The project uses Python's built-in secrets module to generate random passwords.

Example: Generated Password: X7@pL9#vQ2!mR8$k

The generator ensures that the generated password contains characters from multiple categories.


📊 Security Score
The application calculates a score between:

0 – 100

The password is classified into:
Score Strength 0–24 🔴 Very Weak 25–44 🟠 Weak 45–64 🟡 Medium 65–84 🟢 Strong 85–100 🟢 Very Strong


🔐 Password Reuse Detection
The application checks whether a password has already been analyzed before.

If the password was previously used, the application displays a warning and recommends using a different password.


▶️ How to Use

Enter a password.
Click Analyze Password.
View the strength score, entropy, and security recommendations.
Use Generate Strong Password to create a secure password.
Use the Eye icon to show/hide the password.
