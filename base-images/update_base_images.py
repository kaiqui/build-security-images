import os
import click
import subprocess
from rich.console import Console
from rich.progress import track

console = Console()

def get_tag():
    """_summary_

    Returns:
        str: return docker tag
    """
    result = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True, check=True)
    version = result.stdout.strip()
    return version

def build_and_push_docker_image(dockerfile_path, image_name, version, registry, project, username, password):
    """_summary_

    Args:
        dockerfile_path (_type_): _description_
        image_name (_type_): _description_
        version (_type_): _description_
        registry (_type_): _description_
        project (_type_): _description_
        username (_type_): _description_
        password (_type_): _description_
    """
    full_image_name = f"{image_name}:{version}"
    image_name = f"{registry}/{project}/{full_image_name}"
    
    # Build the Docker image
    console.print(f"[yellow]Building Docker image {full_image_name}...[/yellow]")
    build_command = f"docker build -t {full_image_name} -f {dockerfile_path} ."
    subprocess.run(build_command, shell=True, check=True)
    
    # Tag the Docker image
    tag_command = f"docker tag {full_image_name} {image_name}"
    subprocess.run(tag_command, shell=True, check=True)
    
    # Push the Docker image to the Harbor registry
    console.print(f"[yellow]Pushing Docker image {full_image_name} to {registry}/{project}...[/yellow]")
    login_command = f"docker login {registry} -u {username} -p {password}"
    subprocess.run(login_command, shell=True, check=True)
    push_command = f"docker push {image_name}"
    subprocess.run(push_command, shell=True, check=True)
    console.print(f"[green]Docker image {full_image_name} pushed successfully![/green]")

@click.command()
@click.option('--dockerfile-dir', default='dockerfiles', help='Directory containing Dockerfiles')
@click.option('--registry', prompt=True, help='Harbor registry URL')
@click.option('--project', prompt=True, help='Harbor project name')
@click.option('--username', prompt=True, help='Harbor username')
@click.option('--password', prompt=True, hide_input=True, help='Harbor password')
def build_and_push_images(dockerfile_dir, registry, project, username, password):
    if not os.path.exists(dockerfile_dir):
        console.print(f"[bold red]Directory '{dockerfile_dir}' does not exist![/bold red]")
        return
    
    try:
        version = get_tag()
        console.print(f"[bold blue]Using Git version: {version}[/bold blue]")
    except subprocess.CalledProcessError:
        console.print(f"[bold red]Failed to get Git version. Make sure you're in a Git repository with tags.[/bold red]")
        return
    
    dockerfiles = [f for f in os.listdir(dockerfile_dir) if f.startswith('Dockerfile')]
    console.print(f"[bold blue]Found {len(dockerfiles)} Dockerfiles in '{dockerfile_dir}' directory[/bold blue]")

    for dockerfile in track(dockerfiles, description="Processing Dockerfiles..."):
        dockerfile_path = os.path.join(dockerfile_dir, dockerfile)
        image_name = dockerfile.replace('Dockerfile_', 'myapp_image_')
        
        # Build, tag, and push the Docker image
        build_and_push_docker_image(dockerfile_path, image_name, version, registry, project, username, password)

    console.print("[bold green]All images built and pushed successfully![/bold green]")

if __name__ == '__main__':
    build_and_push_images()
