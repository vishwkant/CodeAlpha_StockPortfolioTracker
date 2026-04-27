# 📈 Stock Portfolio Tracker — Python Project
Hey! This is a simple stock portfolio tracker I built using Python as part of my internship at CodeAlpha. It runs in the terminal and helps you calculate how much total money you have invested across different stocks — no internet, no APIs, just pure Python logic.

📌 What is this project?
Ever wondered how much your stock investments are worth in total? This program does exactly that. You tell it which stocks you own and how many shares, and it calculates the total investment value for you — instantly.

💡 How it works

The program has a built-in price list for popular stocks like AAPL, TSLA, GOOGL, INFY, and AMZN
You enter how many stocks you want to track
For each stock, you type the name and how many shares you own
The program multiplies price × quantity for each stock
It adds everything up and shows your total investment
The results also get saved to a portfolio.txt file automatically


# ▶️ How to Run It
Make sure Python is installed, then open your terminal and run:
bashpython stock_tracker.py
No extra libraries or installations needed!

🖥️ Sample Output
How many stocks do you own? 2
Stock 1 name (e.g. AAPL): AAPL
Quantity of AAPL: 5
Stock 2 name (e.g. AAPL): TSLA
Quantity of TSLA: 3

--- Your Portfolio ---
AAPL: 5 shares × $180 = $900
TSLA: 3 shares × $250 = $750

Total investment: $1650
Results saved to portfolio.txt

📦 Stocks Available in This Version
StockCompanyPrice UsedAAPLApple Inc$180TSLATesla$250INFYInfosys$20GOOGLGoogle$140AMZNAmazon$185

# 🧠 What I Learned

How Python dictionaries work as key-value lookup tables
How to collect and validate user input with input() and int()
How for loops with .items() work on dictionaries
How to do basic arithmetic and accumulate totals with +=
How to write and save data to a .txt file using open()


📁 Files in this Project
FileWhat it doesstock_tracker.pyThe main program — run thisportfolio.txtAuto-generated output file with your resultsREADME.mdThis file — explains the project

# 🙋 About Me
This project was built during my Python Programming Internship at CodeAlpha. I'm learning Python from the ground up, and this was a great way to understand how real-world tools like portfolio trackers actually work under the hood!

🔗 Internship Details

Company: CodeAlpha
Domain: Python Programming
Task: Task 2 — Stock Portfolio Tracker


Simple code, real results. That's the goal.
