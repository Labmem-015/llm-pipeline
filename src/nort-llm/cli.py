import random
import requests
import typer

app = typer.Typer()

HARDCODED_USER = "default_user"
BASE_URL = "http://localhost:8000"
session_id = random.randint(1, 100000)
think_mode = True

@app.command("send")
def send_prompt(
    prompt: str = typer.Argument(..., help="The prompt text to send"),
    think: bool = typer.Option(False, "--think", help="Enable thinking mode"),
):
    """Send a prompt to the server."""
    url = f"{BASE_URL}/chat/{session_id}"
    payload = {
        "username": HARDCODED_USER,
        "prompt": prompt,
        "think": think,
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        typer.echo(f"Sent prompt to session {session_id}")
        typer.echo(f"Response: {response.json()}")
    except requests.exceptions.RequestException as e:
        typer.echo(f"Error sending request: {e}", err=True)

@app.command("run")
def interactive_prompt():
    """Start an interactive CLI similar to a REPL."""
    typer.echo("Interactive Prompt Mode")
    typer.echo("Type '/exit' or '/quit' to /exit")
    while True:
        try:
            prompt = typer.prompt(">", prompt_suffix="")
            if prompt.lower() in ["/exit", "/quit", "/q"]:
                break
            if prompt.lower() in ["/think", "/t"]:
                global think_mode
                think_mode = not think_mode
                typer.echo(f"\nThink mode: {think_mode}")
                continue
            send_prompt(prompt=prompt, think=think_mode)
        except KeyboardInterrupt:
            typer.echo("\nExiting...")
            break

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """Main entry point if no args are specified"""
    # Если подкоманда не передана, вызываем command1
    if ctx.invoked_subcommand is None:
        interactive_prompt()


if __name__ == "__main__":
    app()
