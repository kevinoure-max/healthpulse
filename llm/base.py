class LLMProvider:
    def generate_analysis(
        self, metric: str, country: str, stats: dict, question: str = None
    ) -> str:
        raise NotImplementedError("Subclasses must implement generate_analysis")
