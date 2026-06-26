from pipeline import AgentPipeline


def main():

    print("=" * 60)
    print("🤖 Agentic AI Multi-Step Task System")
    print("=" * 60)

    user_request = input("\nEnter your task:\n> ")

    pipeline = AgentPipeline()

    pipeline.execute(user_request)


if __name__ == "__main__":
    main()