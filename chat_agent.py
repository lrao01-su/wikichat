from llama_index.core.tools import QueryEngineTool, ToolMetadata
import chainlit as cl
from chainlit.input_widget import Select, TextInput
import openai
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from llama_index.core.callbacks import CallbackManager, LlamaDebugHandler
from index_wikipages import create_index
from utils import get_apikey

import logging

logger = logging.getLogger(__name__)

index = None
global agent
agent = None


@cl.on_chat_start
async def on_chat_start():
    global index, agent
    try:
        # Settings
        settings = await cl.ChatSettings(
            [
                Select(
                    id="MODEL",
                    label="OpenAI - Model",
                    values=["gpt-3.5-turbo", "gpt-4"],
                    initial_index=0,
                ),
                TextInput(id="WikiPageRequest", label="Request Wikipage"),
            ]
        ).send()

        # Initialize the agent with default settings
        MODEL = "gpt-3.5-turbo"
        logger.info("Creating index for 'Default Wikipedia Page'")
        index = create_index("Default Wikipedia Page")
        logger.info("Creating ReAct agent with model: %s", MODEL)
        agent = create_react_agent(MODEL)

        await cl.Message(
            author="Agent",
            content="I'm ready to help! You can change the model or request a specific Wikipedia page in the settings.",
        ).send()
    except Exception as e:
        logger.error("Error during chat start: %s", str(e))
        await cl.Message(
            author="System",
            content="An error occurred during initialization. Please try restarting the chat.",
        ).send()


def wikisearch_engine(index):
    query_engine = index.as_query_engine(
        response_mode="compact", verbose=True, similarity_top_k=10
    )
    return query_engine


def create_react_agent(MODEL):
    query_engine_tools = [
        QueryEngineTool(
            query_engine=wikisearch_engine(index),
            metadata=ToolMetadata(
                name="WikipediaSearch",  # Ensure the tool name matches the action input
                description="Useful for performing searches on the wikipedia knowledgebase",
            ),
        )
    ]

    openai.api_key = get_apikey()

    # Use legacy CallbackManager and LlamaDebugHandler
    callback_manager = CallbackManager([LlamaDebugHandler()])

    # Log the type of callback_manager to ensure it's correct
    logger.info("CallbackManager type: %s", type(callback_manager))

    # Create OpenAI instance with callback_manager
    llm = OpenAI(model=MODEL, callback_manager=callback_manager)

    # Log the type of llm to ensure it's correct
    logger.info("OpenAI instance type: %s", type(llm))

    # Create ReActAgent instance
    react_agent = ReActAgent.from_tools(
        tools=query_engine_tools,
        llm=llm,
        callback_manager=callback_manager,
        verbose=True,
    )

    # Log the type of react_agent to ensure it's correct
    logger.info("ReActAgent instance type: %s", type(react_agent))

    return react_agent


@cl.on_settings_update
async def setup_agent(settings):
    global agent, index
    query = settings["WikiPageRequest"]
    index = create_index(query)

    print("on_settings_update", settings)
    MODEL = settings["MODEL"]
    agent = create_react_agent(MODEL)
    await cl.Message(
        author="Agent", content=f"Wikipage(s) '{query}' successfully indexed"
    ).send()


@cl.on_message
async def main(message: cl.Message):
    global agent
    logger.info("Received message: %s", message.content)
    if agent is None:
        logger.warning("Agent is not initialized")
        try:
            logger.info("Attempting to reinitialize agent")
            MODEL = "gpt-3.5-turbo"  # Default model
            agent = create_react_agent(MODEL)
            logger.info("Agent reinitialized successfully")
        except Exception as e:
            logger.error("Failed to reinitialize agent: %s", str(e))
            await cl.Message(
                author="System",
                content="Failed to initialize the agent. Please restart the chat or check your settings.",
            ).send()
            return

    logger.info("Agent is initialized, attempting to get response")
    try:
        response = await cl.make_async(agent.chat)(message.content)
        logger.info("Received response from agent: %s", response)
        await cl.Message(author="Agent", content=response).send()
    except Exception as e:
        logger.error("Error getting response from agent: %s", str(e))
        await cl.Message(
            author="System",
            content="An error occurred while processing your request. Please try again.",
        ).send()
