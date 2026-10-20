import json
from pathlib import Path
from datetime import date

FILE = Path("applications.json")


def load_applications():
    if FILE.exists():
        return json.loads(FILE.read_text())
    return []


def save_applications(applications):
    FILE.write_text(json.dumps(applications, indent=4))


def add_application():
    company = input("Company name: ").strip()
    role = input("Job title: ").strip()

    if not company or not role:
        print("Company and job title are required.")
        return

    application = {
        "company": company,
        "role": role,
        "date_applied": str(date.today()),
        "status": "Applied"
    }

    applications = load_applications()
    applications.append(application)
    save_applications(applications)

    print("Application saved successfully!")


def list_applications():
    applications = load_applications()

    if not applications:
        print("No applications recorded yet.")
        return

    for number, application in enumerate(applications, start=1):
        print(
            f"{number}. {application['role']} at "
            f"{application['company']} | "
            f"{application['status']} | "
            f"{application['date_applied']}"
        )


def main():
    while True:
        print("\nJOB APPLICATION TRACKER")
        print("1. Add application")
        print("2. View applications")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_application()
        elif choice == "2":
            list_applications()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
