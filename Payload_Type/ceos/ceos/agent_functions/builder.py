import logging
import pathlib
from mythic_container.PayloadBuilder import *
from mythic_container.MythicCommandBase import *
from mythic_container.MythicRPC import *
import json


class BasicPythonAgent(PayloadType):
    name = "Ceos"
    file_extension = "exe"
    author = "@Ferrevdv"
    supported_os = [SupportedOS.Windows]
    wrapper = False
    wrapped_payloads = []
    note = """This  uses JavaScript for Automation (JXA) for execution on macOS boxes."""
    supports_dynamic_loading = False
    c2_profiles = ["http"]
    mythic_encrypts = False
    translation_container = "CeosTranslator"
    build_parameters = [
        BuildParameter(
                name="output",
                parameter_type=BuildParameterType.ChooseOne,
                description="Choose output format",
                choices=["exe"],
                default_value="exe"
        )
    ]

    agent_path = pathlib.Path(".") / "ceos"
    agent_icon_path = agent_path / "agent_functions" / "basic_python_agent.svg"
    agent_code_path = agent_path / "agent_code"

    build_steps = [
        BuildStep(step_name="Gathering Files", step_description="Making sure all commands have backing files on disk"),
        BuildStep(step_name="Configuring", step_description="Stamping in configuration values")
    ]

    async def build(self) -> BuildResponse:
        # this function gets called to create an instance of your payload
        resp = BuildResponse(status=BuildStatus.Success)
        # create the payload
        build_msg = ""

        return resp
