"""
Project Management Program
Loads and saves a data file using a list of Project objects.
Actual time:
Estimated time: 3 hrs
"""

# NOTES
# You should notice that there are two different scenarios for both loading and saving.
# Consider SRP and how you can write a single function for loading that you use in both scenarios: the default filename and the user-selected filename.
# Use the datetime module for the project start date.
# Use at least one utility/helper method in your class.
# Think of our examples like is_vintage for Guitar and what you might use for a Project.
# Error checking. Do no error checking to start with.

# Remember how in our walkthrough above, we saw that it is not the class's job to convert the file's "Yes" string into the Boolean True for the class? That's the job of the client code.
# Here, when you create a Project object, you will want to convert the date string to a datetime object, but it's not the class's job - it's the client code's job.

WELCOME_MESSAGE = "Welcome to Pythonic Project Management"
MENU = "- (L)oad projects"
"- (S)ave projects"
"- (D)isplay projects"
"- (F)ilter projects by date"
"- (A)dd new project"
"- (U)pdate project"
"- (Q)uit"
FILENAME = "projects.txt"


def main():
    print(WELCOME_MESSAGE)
    projects = load_project()
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    print(MENU)
    choice = input()
    while choice != "Q":
        if choice == "L":
            load_project()
            # TODO: Load projects: prompt the user for a filename to load projects from and load them
            # import datetime
            #
            # date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
            # date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            # print(f"That day is/was {date.strftime('%A')}")
            # print(date.strftime("%d/%m/%Y"))
        elif choice == "S":
            save_projects()
            # TODO: Save projects Prompt the user for a filename to save projects to and save them
        elif choice == "D":
            display_projects()
            sort_projects()
            # TODO: Display projects: Display two groups: incomplete projects; completed projects, both sorted by priority
        elif choice == "F":
            filter_projects()
            sort_projects()
            # TODO: Filter projects by date: Ask the user for a date and display only projects that start after that date, sorted by date
        elif choice == "A":
            add_projects()
            # TODO: Add new project: Ask the user for the inputs and add a new project to memory
        elif choice == "U":
            update_projects()
            # TODO: Update project: Choose a project, then modify the completion % and/or priority - the user can leave either input blank to retain existing values
        print(MENU)
        choice = input()
    # TODO: When the user quits, give them the choice of saving to the default file.


def load_project(filename):
    """Load projects from filename as list of Project objects"""
    return "1"  # dummy value change later


def save_projects(filename):
    """Save projects to filename"""


def display_projects():
    """Display two groups: incomplete projects; completed projects"""


def filter_projects(date):
    """Display only projects that start after date"""


def add_projects():
    """Add a new project to memory."""


def update_projects(project):
    """Modify the completion % and/or priority of project - the user can leave either input blank to retain existing values."""


def sort_projects(sort_method):
    """Sort projects by sort_method."""


main()
