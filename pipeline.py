from rich.console import Console
import time

from agents.planner import PlannerAgent
from agents.retriever import RetrieverAgent
from agents.analyzer import AnalyzerAgent
from agents.writer import WriterAgent

console = Console()


class AgentPipeline:

    def __init__(self):
        self.planner = PlannerAgent()
        self.retriever = RetrieverAgent()
        self.analyzer = AnalyzerAgent()
        self.writer = WriterAgent()

    # Retry logic for graceful failure handling
    def run_with_retry(self, agent_function, *args, retries=3):

        for attempt in range(1, retries + 1):
            try:
                return agent_function(*args)

            except Exception as e:
                console.print(f"[red]❌ Attempt {attempt} failed:[/red] {e}")

                if attempt < retries:
                    console.print("[yellow]🔄 Retrying in 2 seconds...[/yellow]")
                    time.sleep(2)

        raise Exception("Maximum retry attempts reached.")

    def execute(self, user_request):

        console.print("\n[bold cyan]📥 User Task Received[/bold cyan]")
        time.sleep(1)

        # Planner Agent
        console.print("\n[bold yellow]🧠 Planner Agent[/bold yellow]")
        plan = self.run_with_retry(
            self.planner.create_plan,
            user_request
        )
        console.print("[green]✅ Plan Created[/green]")
        time.sleep(1)

        # Retriever Agent
        console.print("\n[bold blue]🔍 Retriever Agent[/bold blue]")
        research = self.run_with_retry(
            self.retriever.retrieve_information,
            plan
        )
        console.print("[green]✅ Research Completed[/green]")
        time.sleep(1)

        # Analyzer Agent
        console.print("\n[bold magenta]📊 Analyzer Agent[/bold magenta]")
        summary = self.run_with_retry(
            self.analyzer.analyze,
            research
        )
        console.print("[green]✅ Summary Generated[/green]")
        time.sleep(1)

        # Writer Agent
        console.print("\n[bold green]✍️ Writer Agent[/bold green]")
        linkedin_post = self.run_with_retry(
            self.writer.write_post,
            summary
        )
        console.print("[green]✅ LinkedIn Post Generated[/green]")

        console.print("\n[bold cyan]🎉 Task Completed Successfully[/bold cyan]")

        console.rule("[bold green]Execution Plan")
        console.print(plan)

        console.rule("[bold blue]Summary")
        console.print(summary)

        console.rule("[bold magenta]LinkedIn Post")
        console.print(linkedin_post)

        return {
            "plan": plan,
            "research": research,
            "summary": summary,
            "linkedin_post": linkedin_post
        }