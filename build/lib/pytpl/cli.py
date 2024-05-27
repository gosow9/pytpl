import os
import click
from jinja2 import Environment, FileSystemLoader

# Function to render templates
def render_template(template_name, context):
    # Calculate the path to the templates directory
    template_path = os.path.join(os.path.dirname(__file__), 'templates')
    env = Environment(loader=FileSystemLoader(template_path))
    template = env.get_template(template_name)
    return template.render(context)

# CLI definition
@click.command()
@click.argument('project_name')
def create_project(project_name):
    """Create a new Python project with the given PROJECT_NAME."""
    # Create project directory
    os.makedirs(project_name, exist_ok=True)
    
    # Render setup.py
    setup_content = render_template('setup.py.j2', {'project_name': project_name})
    with open(os.path.join(project_name, 'setup.py'), 'w') as f:
        f.write(setup_content)
    
    # Create project package directory
    os.makedirs(os.path.join(project_name, project_name), exist_ok=True)
    
    # Render main.py
    main_content = render_template('main.py.j2', {'project_name': project_name})
    with open(os.path.join(project_name, project_name, 'main.py'), 'w') as f:
        f.write(main_content)
    
    click.echo(f'Project {project_name} created successfully!')

if __name__ == '__main__':
    create_project()
