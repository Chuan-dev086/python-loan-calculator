import tkinter as tk
from tkinter import messagebox


def calculate():
    try:
        # get the users input data
        principal = float(entry_principal.get())
        annual_rate = float(entry_rate.get())
        years = int(entry_years.get())

        # calculation
        monthly_rate = annual_rate / 100 / 12
        months = years * 12

        # Equal Monthly Installment (EMI)
        monthly_payment = (
            principal
            * (monthly_rate * (1 + monthly_rate) ** months)
            / ((1 + monthly_rate) ** months - 1)
        )
        total_payment = monthly_payment * months
        total_interest = total_payment - principal

        # showing results
        result_text = f"[Equal Principal Payments]\n"
        result_text = f"Monthly Payment: RM {monthly_payment:.2f}"
        result_text = f"Total Payment: RM {total_payment:.2f}"
        result_text = f"Total Interest:RM {total_interest:.2f}"

        label_result.config(text=result_text)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number !!")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong")


# creating windows
window = tk.Tk()
window.title(" House Loan Calculator")
window.geometry("400x500")

# title
title = tk.Label(window, text="House Loan Calculator", font=("Arial",16,"bold"))
title.pack(pady=15)

# principal (loan amount)
tk.Label(window,text="Loan Amount(RM):",font=("Arial",11)).pack()
entry_principal = tk.Entry(window, font=("Arial",11))
entry_principal.pack(pady=5)

# APR (Annual Percentage Rate) 
tk.Label(window, text="Annual Interest Rate(%):",font=("Arial,11")).pack()
entry_rate = tk.Entry(window,font=("Arial",11))
entry_rate.pack(pady=5)

# Loan terms 
tk.Label(window, text="Loan Term (Years):", font=("Arial",11,)).pack()
entry_years = tk.Entry(window, font=("Arial",11))
entry_years.pack(pady=5)

# Calculate Button
btn_calculate = tk.Button(window, text="Calculate", command=calculate,
                          font=("Arial",12), bg="#4CAF50",fg="white",
                          width=15,height=2)
btn_calculate.pack(pady=15)

# Show Result Calculated
tk.Label(window, text="Result Calculated:", font=("Arial",12,"bold")).pack()
label_result = tk.Label(window, text="", font=("Arial", 11), fg="blue",justify="left")
label_result.pack(pady=10)

# running windows
window.mainloop()