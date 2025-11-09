"""
Project Management Program
Loads and saves a data file using a list of Project objects.
Actual time: 4hrs
Estimated time: 3 hrs
"""
import datetime
from operator import attrgetter

from project import Project

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


# TODO: DRY for whole program


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
            try:
                projects = load_project(chosen_filename)
                print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")
            except FileNotFoundError:
                print("File does not exist :(")
            except ValueError:
                print("File not correctly formatted :(\n"
                      "Correct formatting: Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage")
        elif choice == "S":
            # Prompt the user for a filename to save projects to and save them.
            chosen_filename = input("Enter filename: ")
            save_projects(chosen_filename, projects)
        elif choice == "D":
            # Display two groups: incomplete projects; completed projects, both sorted by priority.
            incomplete_projects = [project for project in projects if not project.is_complete()]
            incomplete_projects.sort(key=attrgetter("priority"))
            print("Incompleted projects:")
            display_projects(incomplete_projects, "  ", False)

            complete_projects = [project for project in projects if project.is_complete()]
            complete_projects.sort(key=attrgetter("priority"))
            print("Completed projects:")
            display_projects(complete_projects, "  ", False)
        elif choice == "F":
            # Ask the user for a date and display only projects that start after that date, sorted by date.
            filter_date_string = input("Show projects that start after date (dd/mm/yy):")
            try:
                filter_date = datetime.datetime.strptime(filter_date_string, "%d/%m/%Y").date()
                filtered_projects = filter_projects(projects, filter_date)
                filtered_projects.sort(key=attrgetter("date"))
                display_projects(filtered_projects, "", False)
            except ValueError:
                print("Invalid date :(")
        elif choice == "A":
            # Ask the user for the inputs and add a new project to memory.
            print("Let's add a new project")
            new_project = get_valid_project()
            if new_project != "BAD":
                projects.append(new_project)
        elif choice == "U":
            # Choose a project, then modify the completion % and/or priority.
            display_projects(projects, " ", True)
            try:
                project_index = int(input("Project choice: "))
                print(projects[project_index])
                new_completion = input("New Percentage: ")
                new_priority = input("New Priority: ")
                update_project(projects, project_index, new_completion, new_priority)
            except IndexError:
                print("This index does not exist :(")
            except ValueError:
                print("Invalid input")
        else:
            print("Invalid input :(")
        print(MENU)
        choice = input(">>> ").upper()
    # When the user quits, give them the choice of saving to the default file.
    save_choice = input(f"Would you like to save to {DEFAULT_FILENAME}?")
    if save_choice == "yes":
        save_projects(DEFAULT_FILENAME, projects)
    print("Thank you for using custom-built project management software.")


def load_project(filename):
    """Load projects from filename as list of Project objects."""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()  # Remove header row
        for line in in_file:
            parts = line.strip().split("\t")
            date_string = parts[DATE_INDEX]
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            project = Project(parts[NAME_INDEX], date, parts[PRIORITY_INDEX], float(parts[COST_INDEX]),
                              int(parts[COMPLETION_INDEX]))
            projects.append(project)
    return projects


def save_projects(filename, projects):
    """Save projects to filename."""
    with open(filename, "w") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)  # file header
        for project in projects:
            print(
                f"{project.name}\t{project.date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost}\t{project.completion}",
                file=out_file)


def display_projects(projects, indent, is_indexed):
    """Display two groups: incomplete projects; completed projects."""
    for i, project in enumerate(projects):
        if is_indexed:
            print(f"{i}{indent}{project}")
        else:
            print(f"{indent}{project}")


def filter_projects(projects, filter_date):
    """Filter projects by date for projects that start after filter_date."""
    filtered_projects = [project for project in projects if project.date >= filter_date]
    return filtered_projects


def get_valid_project():
    """Get new project from user."""
    try:
        name = input("Name: ")
        date_string = input("Start date: ")
        date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        priority = int(input("Priority: "))
        cost = float(input("Cost estimate: $"))
        completion = int(input("Percent complete: "))
        project = Project(name, date, priority, cost, completion)
        return project
    except ValueError:
        print("Invalid input :( ")
        return "BAD"  # TODO: fix logic and neaten this


def get_number(attribute):
    """Get a valid number for attribute"""
    try:
        attribute = int(input(f"{attribute.upper()}: "))
    except ValueError:
        print(f"Invalid {attribute}, must be a number :(")


def update_project(projects, project_index, completion, priority):
    """Modify the completion % and/or priority of project - if either is "" then retain existing values."""
    project = projects[project_index]
    if completion != "" or " ":
        project.completion = int(completion)
    if priority != "":
        project.priority = int(priority)


main()
