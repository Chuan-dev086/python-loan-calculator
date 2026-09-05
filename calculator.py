import tkinter as tk
from tkinter import messagebox


def calculate():
    try:
        # get the users input data
        principal = float(entry_principal.get())
        annual_rate = float(entry_rate.get())
        years = int(entry_years.get())

        # get the users input data
        loan_type = repayment_type.get()

        # calculation
        monthly_rate = annual_rate / 100 / 12
        months = years * 12

        if loan_type == "Equal Loan Payment":
            # Equal Monthly Installment (EMI)
            monthly_payment = (
                principal
                * (monthly_rate * (1 + monthly_rate) ** months)
                / ((1 + monthly_rate) ** months - 1)
            )
            total_payment = monthly_payment * months
            total_interest = total_payment - principal

            # showing results
            result_text = f"【Equal Loan Payment】\n"
            result_text += f"Monthly Payment:RM {monthly_payment:.2f}\n"
            result_text += f"Total Payment:RM {total_payment:.2f}\n"
            result_text += f"Total Interest:RM {total_interest:.2f}"

        else:  # Equal Monthly Payment
            # Equal Monthly Principal (Every Month)
            monthly_principal = principal / months

            # First Month Interest
            first_month_interest = principal * monthly_rate
            # First Month Payment (Principal + Interest)
            first_month_payment = monthly_principal + first_month_interest

            # Last Month Interest
            last_month_interest = monthly_principal * monthly_rate
            # Last Month Payment
            last_month_payment = monthly_principal + last_month_interest

            # Total Interest = (First Month's Interest + Last Month's Interest) × Number of Months ÷ 2
            total_interest = (first_month_interest + last_month_interest) * months / 2
            total_payment = principal + total_interest

            # Monthly Decrease Amount
            monthly_decrease = monthly_principal * monthly_rate

            result_text = f"【Equal Principal Amount】\n"
            result_text += f"First Month Payment:RM {first_month_payment:.2f}\n"
            result_text += f"Monthly Decrease:RM {monthly_decrease:.2f}\n"
            result_text += f"Total Payment:RM {total_payment:.2f}\n"
            result_text += f"Total Interest:RM {total_interest:.2f}"

        label_result.config(text=result_text)

    except ValueError:
        messagebox.showerror("Oops", "Please Enter a valid number")
    except Exception as e:
        messagebox.showerror("Error", f"Have Error Occured:{e}")


# creating windows
window = tk.Tk()
window.title(" House Loan Calculator")
window.geometry("400x500")

# title
title = tk.Label(window, text="House Loan Calculator", font=("Arial", 16, "bold"))
title.pack(pady=15)

# select payment method
tk.Label(window, text="Payment Method:", font=("Arial", 11)).pack()
repayment_type = tk.StringVar(value="Equal Principal Payment")
dropdown = tk.OptionMenu(
    window, repayment_type, "Equal Pricipal Payment", "Equal Loan Payment"
)
dropdown.pack(pady=5)


# principal (loan amount)
tk.Label(window, text="Loan Amount(RM):", font=("Arial", 11)).pack()
entry_principal = tk.Entry(window, font=("Arial", 11))
entry_principal.pack(pady=5)

# APR (Annual Percentage Rate)
tk.Label(window, text="Annual Interest Rate(%):", font=("Arial,11")).pack()
entry_rate = tk.Entry(window, font=("Arial", 11))
entry_rate.pack(pady=5)

# Loan terms
tk.Label(
    window,
    text="Loan Term (Years):",
    font=(
        "Arial",
        11,
    ),
).pack()
entry_years = tk.Entry(window, font=("Arial", 11))
entry_years.pack(pady=5)

# Calculate Button
btn_calculate = tk.Button(
    window,
    text="Calculate",
    command=calculate,
    font=("Arial", 12),
    bg="#4CAF50",
    fg="white",
    width=15,
    height=2,
)
btn_calculate.pack(pady=15)

# Show Result Calculated
tk.Label(window, text="Result Calculated:", font=("Arial", 12, "bold")).pack()
label_result = tk.Label(window, text="", font=("Arial", 11), fg="blue", justify="left")
label_result.pack(pady=10)

# running windows
window.mainloop()
