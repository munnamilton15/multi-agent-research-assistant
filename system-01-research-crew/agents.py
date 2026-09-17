import os
from dotenv import load_dotenv
from crewai import Agent, LLM
from crewai.tools import tool
from ddgs import DDGS

load_dotenv()

# --------------------------------------------------
# Gemini LLM
# --------------------------------------------------

gemini_llm = LLM(
    model="gemini/gemini-3.5-flash-lite",
    api_key=os.getenv("GEMINI_API_KEY"),
)


# --------------------------------------------------
# Web Search Tool
# --------------------------------------------------

@tool("web_search")
def web_search(query: str) -> str:
    """Search the web for credible information about a research topic."""

    results = []

    try:
        search_results = DDGS().text(
            query,
            max_results=8
        )

        for result in search_results:
            results.append(
                f"Title: {result.get('title')}\n"
                f"URL: {result.get('href')}\n"
                f"Snippet: {result.get('body')}\n"
            )

    except Exception as error:
        return f"WEB SEARCH ERROR: {error}"

    if not results:
        return "WEB SEARCH ERROR: No search results were returned."

    return "\n\n".join(results)


# --------------------------------------------------
# Agent 1 — Researcher
# --------------------------------------------------

searcher = Agent(
    role="Senior Research Librarian",

    goal=(
        "Find credible, recent and relevant sources about the research topic. "
        "Prioritize official documentation, research papers, universities, "
        "government sources and first-party sources."
    ),

    backstory=(
        "You are an experienced research librarian specializing in "
        "technology research. You carefully search the web, identify "
        "reliable sources and organize evidence for other researchers."
    ),

    tools=[web_search],

    llm=gemini_llm,

    allow_delegation=False,
    verbose=True,
)


# --------------------------------------------------
# Agent 2 — Analyst
# --------------------------------------------------

analyst = Agent(
    role="Critical Research Analyst",

    goal=(
        "Analyze the research collected by the Research Librarian and "
        "identify the strongest evidence-backed claims. Clearly distinguish "
        "strong evidence from uncertain or limited evidence."
    ),

    backstory=(
        "You are a critical technology research analyst. You evaluate "
        "evidence carefully and avoid unsupported claims or invented facts."
    ),

    llm=gemini_llm,

    allow_delegation=False,
    verbose=True,
)


# --------------------------------------------------
# Agent 3 — Fact Checker
# --------------------------------------------------

fact_checker = Agent(
    role="Research Fact Checker",

    goal=(
        "Verify the important claims in the research analysis against "
        "the provided sources. Identify unsupported claims, questionable "
        "statements, missing evidence and source-quality problems."
    ),

    backstory=(
        "You are a meticulous fact checker. Your job is to prevent "
        "hallucinations and ensure that the final report is based on "
        "traceable evidence."
    ),

    tools=[web_search],

    llm=gemini_llm,

    allow_delegation=False,
    verbose=True,
)


# --------------------------------------------------
# Agent 4 — Writer
# --------------------------------------------------

writer = Agent(
    role="Technical Report Writer",

    goal=(
        "Create a professional technical research report using only "
        "the verified research and analysis provided by the previous agents."
    ),

    backstory=(
        "You are a technical writer who specializes in producing clear, "
        "structured and evidence-based technology reports."
    ),

    llm=gemini_llm,

    allow_delegation=False,
    verbose=True,
)
