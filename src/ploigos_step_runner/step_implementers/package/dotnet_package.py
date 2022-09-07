"""`StepImplementer` for the `package` step using Dotnet.

Notes
-----

Step Configuration
------------------
Step configuration expected as input to this step.
Could come from:

  * static configuration
  * runtime configuration
  * previous step results

Configuration Key            | Required? | Default | Description
-----------------------------|-----------|---------|-----------

Result Artifacts
----------------
Results artifacts output by this step.

Result Artifact Key | Description
--------------------|------------

"""
import sh

from ploigos_step_runner.step_implementers.shared.dotnet_generic import \
    DotnetGeneric

DEFAULT_CONFIG = {
}

REQUIRED_CONFIG_OR_PREVIOUS_STEP_RESULT_ARTIFACT_KEYS = [
]

class DotnetPackage(DotnetGeneric):
    """`StepImplementer` for the `package` step using Maven.
    """
    def __init__(  # pylint: disable=too-many-arguments
        self,
        workflow_result,
        parent_work_dir_path,
        config,
        environment=None
    ):
        super().__init__(
            workflow_result=workflow_result,
            parent_work_dir_path=parent_work_dir_path,
            config=config,
            environment=environment,
            maven_phases_and_goals=['package']
        )

    @staticmethod
    def step_implementer_config_defaults():
        """Getter for the StepImplementer's configuration defaults.

        Returns
        -------
        dict
            Default values to use for step configuration values.

        Notes
        -----
        These are the lowest precedence configuration values.
        """
        # return {**MavenGeneric.step_implementer_config_defaults(), **DEFAULT_CONFIG}

    @staticmethod
    def _required_config_or_result_keys():
        """Getter for step configuration or previous step result artifacts that are required before
        running this step.

        Returns
        -------
        array_list
            Array of configuration keys or previous step result artifacts
            that are required before running the step.
        """
        return REQUIRED_CONFIG_OR_PREVIOUS_STEP_RESULT_ARTIFACT_KEYS

    def _run_step(self): # pylint: disable=too-many-locals
        """Runs the step implemented by this StepImplementer.

        Returns
        -------
        StepResult
            Object containing the dictionary results of this step.
        """
        csproj_file = self.get_value('csproj-file')
        if csproj_file is None:
            sh.dotnet("build") # pylint: disable=no-member
        else:
            sh.dotnet("build", csproj_file) # pylint: disable=no-member