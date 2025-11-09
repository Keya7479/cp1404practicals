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
MENU = ("- (L)oad projects\n"
        "- (S)ave projects\n"
        "- (D)isplay projects\n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project\n"
        "- (U)pdate project\n"
        "- (Q)uit")
DEFAULT_FILENAME = "projects.txt"

# identification indexes for each project in projects
NAME_INDEX = 0
DATE_INDEX = 1
PRIORITY_INDEX = 2
COST_INDEX = 3
COMPLETION_INDEX = 4


def main():
    """Load, manipulate and save projects from chosen files using a list of Project objects."""
    print(WELCOME_MESSAGE)
    projects = load_project(DEFAULT_FILENAME)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            # Prompt the user for a filename to load projects from and load them.
            chosen_filename = input("Enter filename: ")
            projects = load_project(chosen_filename)
            print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")

        elif choice == "S":
            # Prompt the user for a filename to save projects to and save them.
            chosen_filename = input("Enter filename: ")
            save_projects(chosen_filename, projects)
        elif choice == "D":
            # Display two groups: incomplete projects; completed projects, both sorted by priority.
            incomplete_projects = filter_projects(projects, COMPLETION_INDEX,
                                                  range(0, 100))  # TODO: consider logic here
            sorted_incomplete_projects = sort_projects(incomplete_projects, PRIORITY_INDEX)
            print("Uncompleted projects:")
            display_projects(sorted_incomplete_projects)

            complete_projects = filter_projects(projects, COMPLETION_INDEX, 100)
            sorted_complete_projects = sort_projects(complete_projects, PRIORITY_INDEX)
            print("Completed projects:")
            display_projects(sorted_complete_projects)
        elif choice == "F":
            # Ask the user for a date and display only projects that start after that date, sorted by date.
            filter_date = input("Show projects that start after date (dd/mm/yy):")
            filtered_projects = filter_projects(projects, DATE_INDEX, filter_date)
            sorted_filtered_projects = sort_projects(filtered_projects, DATE_INDEX)
            display_projects(sorted_filtered_projects)
        elif choice == "A":
            # Ask the user for the inputs and add a new project to memory.
            print("Let's add a new project")
            name, date, priority, cost, completion = get_project()
            add_project(name, date, priority, cost, completion)
        elif choice == "U":
            # Choose a project, then modify the completion % and/or priority.
            display_projects(projects)
            project_index = input("Project choice: ")
            print(projects[project_index])
            new_percent = input("New Percentage: ")
            new_priority = input("New Priority: ")
            update_project(project_index, new_percent, new_priority)
        print(MENU)
        choice = input(">>> ").upper()
    # When the user quits, give them the choice of saving to the default file.
    save_choice = input(f"Would you like to save to {DEFAULT_FILENAME}?")
    if save_choice == "yes":
        save_projects(DEFAULT_FILENAME, projects)
    print("Thank you for using custom-built project management software.")


def load_project(filename):
    """Load projects from filename as list of Project objects."""
    # import datetime
    #
    # date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
    # date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    # print(f"That day is/was {date.strftime('%A')}")
    # print(date.strftime("%d/%m/%Y"))
    return "1"  # dummy value change later


def save_projects(filename, projects):
    """Save projects to filename."""


def display_projects(projects):
    """Display two groups: incomplete projects; completed projects."""


def filter_projects(projects, filter_method, filter_value):
    """Filter projects by filter_method according to filter_value."""
    # [project[COMPLETION_INDEX] in projects if project[COMPLETION_INDEX] != 100]
    return "1"  # dummy value change later


def get_project():
    """Get new project from user."""
    return "1", "2", "3", "4", "5"  # dummy value change later


def add_project(name, date, priority, cost, completion):
    """Add a new project to memory."""


def update_project(project_index, percent, priority):
    """Modify the completion % and/or priority of project - if either is "" then retain existing values."""


def sort_projects(items, sort_method):
    """Sort items by sort_method."""
    return "1"  # dummy value change later


main()
