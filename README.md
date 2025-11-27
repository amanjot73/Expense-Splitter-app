# **FairSplit – Expense Splitter CLI App**

FairSplit is a **Command-Line based Expense Settlement Tool** that helps groups split expenses fairly. It calculates who owes whom and minimizes the number of payments required. The application also visualizes settlements using **Graph Theory**.

---

## ✨ Features

* **Fair & Automated Settlement Calculation**
* **Minimum number of payments**
* **Graph visualization** of who pays whom
* Works for any group size
* Simple & interactive CLI interface

---

## 🧠 How It Works

* Calculates **net balance** for every person
* Matches creditors vs. debtors efficiently
* Uses **Greedy Optimization** for settlement
* Draws **directed graph** using NetworkX + Matplotlib

---

## 🛠️ Tech Stack

| Component           | Technology Used              |
| ------------------- | ---------------------------- |
| Logic               | Python                       |
| Data Handling       | Pandas                       |
| Graph Visualization | NetworkX, Matplotlib         |
| UI Type             | Command Line Interface (CLI) |

---

## 📦 Installation

### Required Software

* Python **3.x**

### Required Python Libraries

Install dependencies using:

```bash
pip install numpy pandas matplotlib networkx
```

or

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
git clone https://github.com/amanjot73/Expense-Splitter-app.git
cd Expense-Splitter-app
python app.py
```

---

## 📝 Example Input

```
Enter number of people: 3
Enter name of person 1: Aman
Enter amount paid by Aman: 1200
Enter name of person 2: Sahil
Enter amount paid by Sahil: 300
Enter name of person 3: Amit
Enter amount paid by Amit: 0
```

### Output Includes:

✔ Total spend
✔ Per person share
✔ Who should pay whom
✔ Graph showing payment flow

---

## 📊 Graph Example

A directed graph is generated like:

➡ **Amit → Aman : ₹400**
➡ **Sahil → Aman : ₹400**

Each arrow shows: **Debtor → Creditor → Amount**

---

## 📂 Project Structure

```
Expense-Splitter-app/
│── app.py              # Main CLI application
│── README.md           # Documentation
│── requirements.txt    # Required dependencies

```

---

## 🚀 Future Enhancements

* GUI version using Streamlit
* Export settlement summary as PDF
* Support multiple bills & recurring groups
* Improved visualization styling

---

## ✍️ Author

**Amanjot Singh**
GitHub: [@amanjot73](https://github.com/amanjot73)

---