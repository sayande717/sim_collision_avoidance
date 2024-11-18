import tkinter as tk

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Simple Display")

    # Create a label with a message
    label = tk.Label(root, text="Hello, World!", font=("Helvetica", 24))
    label.pack(pady=20)

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    main()