from project import Project

def main():
    print("Welcome to Pythonic Project Management")
    # Placeholder for menu implementation
def load_projects(file_name):
    projects = []
    try:
        with open(file_name, 'r') as file:
            file.readline()  # Skip header
            for line in file:
                name, completion, priority, start_date = line.strip().split('\t')
                projects.append(Project(name, completion, priority, start_date))
    except FileNotFoundError:
        print(f"File {file_name} not found.")
    return projects

def save_projects(file_name, projects):
    with open(file_name, 'w') as file:
        file.write("Name\tCompletion\tPriority\tStart Date\n")
        for project in projects:
            file.write(f"{project.name}\t{project.completion}\t{project.priority}\t{project.start_date.strftime('%d/%m/%Y')}\n")
def display_projects(projects):
    print("Displaying all projects:")
    for project in projects:
        print(project)
def filter_projects_by_date(projects, date_filter):
    filtered_projects = [project for project in projects if project.start_date > date_filter]
    print("Filtered Projects:")
    for project in filtered_projects:
        print(project)
def add_new_project(projects):
    name = input("Enter the project name: ")
    completion = int(input("Enter the completion percentage: "))
    priority = int(input("Enter the priority: "))
    start_date = input("Enter the start date (d/m/yyyy): ")
    projects.append(Project(name, completion, priority, start_date))
    print("New project added successfully.")

if __name__ == "__main__":
    main()
