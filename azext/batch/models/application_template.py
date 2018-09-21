# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class ApplicationTemplate(Model):
    """An Azure Batch Application Template.

    :param job_manager_task: Details of a Job Manager task to be launched when
     the job is started. If the job does not specify a Job Manager task, the
     user must explicitly add tasks to the job. If the job does specify a Job
     Manager task, the Batch service creates the Job Manager task when the job
     is created, and will try to schedule the Job Manager task before
     scheduling other tasks in the job. The Job Manager task's typical purpose
     is to control and/or monitor job execution, for example by deciding what
     additional tasks to run, determining when the work is complete, etc.
     (However, a Job Manager task is not restricted to these activities - it is
     a fully-fledged task in the system and perform whatever actions are
     required for the job.) For example, a Job Manager task might download a
     file specified as a parameter, analyze the contents of that file and
     submit additional tasks based on those contents.
    :type job_manager_task: :class:`JobManagerTask
     <azure.batch.models.JobManagerTask>`
    :param job_preparation_task: The Job Preparation task. If a job has a Job
     Preparation task, the Batch service will run the Job Preparation task on a
     compute node before starting any tasks of that job on that compute node.
    :type job_preparation_task: :class:`JobPreparationTask
     <azure.batch.models.JobPreparationTask>`
    :param job_release_task: The Job Release task. A Job Release task cannot
     be specified without also specifying a Job Preparation task for the job.
     The Batch service runs the Job Release task on the compute nodes that have
     run the Job Preparation task. The primary purpose of the Job Release task
     is to undo changes to compute nodes made by the Job Preparation task.
     Example activities include deleting local files, or shutting down services
     that were started as part of job preparation.
    :type job_release_task: :class:`JobReleaseTask
     <azure.batch.models.JobReleaseTask>`
    :param common_environment_settings: The list of common environment
     variable settings. These environment variables are set for all tasks in
     the job (including the Job Manager, Job Preparation and Job Release
     tasks). Individual tasks can override an environment setting specified
     here by specifying the same setting name with a different value.
    :type common_environment_settings: list of :class:`EnvironmentSetting
     <azure.batch.models.EnvironmentSetting>`
    :param on_all_tasks_complete: The action the Batch service should take
     when all tasks in the job are in the completed state. Note that if a job
     contains no tasks, then all tasks are considered complete. This option is
     therefore most commonly used with a Job Manager task; if you want to use
     automatic job termination without a Job Manager, you should initially set
     onAllTasksComplete to noAction and update the job properties to set
     onAllTasksComplete to terminateJob once you have finished adding tasks.
     Permitted values are: noAction - do nothing. The job remains active unless
     terminated or disabled by some other means. terminateJob - terminate the
     job. The job's terminateReason is set to 'AllTasksComplete'. The default
     is noAction. Possible values include: 'noAction', 'terminateJob'
    :type on_all_tasks_complete: str or :class:`OnAllTasksComplete
     <azure.batch.models.OnAllTasksComplete>`
    :param on_task_failure: The action the Batch service should take when any
     task in the job fails. A task is considered to have failed if has a
     failureInfo. A failureInfo is set if the task completes with a non-zero
     exit code after exhausting its retry count, or if there was an error
     starting the task, for example due to a resource file download error.
     noAction - do nothing. performExitOptionsJobAction - take the action
     associated with the task exit condition in the task's exitConditions
     collection. (This may still result in no action being taken, if that is
     what the task specifies.) The default is noAction. Possible values
     include: 'noAction', 'performExitOptionsJobAction'
    :type on_task_failure: str or :class:`OnTaskFailure
     <azure.batch.models.OnTaskFailure>`
    :param metadata: A list of name-value pairs associated with the job as
     metadata. The Batch service does not assign any meaning to metadata; it is
     solely for the use of user code.
    :type metadata: list of :class:`MetadataItem
     <azure.batch.models.MetadataItem>`
    :param uses_task_dependencies: Whether tasks in the job can define
     dependencies on each other. The default is false.
    :type uses_task_dependencies: bool
    :param task_factory: A task factory reference to automatically generate a set of
     tasks to be added to the job.
    :type task_factory: :class:`TaskFactoryBase
     <azext.batch.models.TaskFactoryBase>`
    """

    _attribute_map = {
        'job_manager_task': {'key': 'jobManagerTask', 'type': 'JobManagerTask'},
        'job_preparation_task': {'key': 'jobPreparationTask', 'type': 'JobPreparationTask'},
        'job_release_task': {'key': 'jobReleaseTask', 'type': 'JobReleaseTask'},
        'common_environment_settings': {'key': 'commonEnvironmentSettings', 'type': '[EnvironmentSetting]'},
        'on_all_tasks_complete': {'key': 'onAllTasksComplete', 'type': 'OnAllTasksComplete'},
        'on_task_failure': {'key': 'onTaskFailure', 'type': 'OnTaskFailure'},
        'metadata': {'key': 'metadata', 'type': '[MetadataItem]'},
        'uses_task_dependencies': {'key': 'usesTaskDependencies', 'type': 'bool'},
        'task_factory': {'key': 'taskFactory', 'type': 'TaskFactoryBase'},
    }

    def __init__(self, **kwargs):
        super(ApplicationTemplate, self).__init__(**kwargs)
        self.job_manager_task = kwargs.get('job_manager_task', None)
        self.job_preparation_task = kwargs.get('job_preparation_task', None)
        self.job_release_task = kwargs.get('job_release_task', None)
        self.common_environment_settings = kwargs.get('common_environment_settings', None)
        self.on_all_tasks_complete = kwargs.get('on_all_tasks_complete', None)
        self.on_task_failure = kwargs.get('on_task_failure', None)
        self.metadata = kwargs.get('metadata', None)
        self.uses_task_dependencies = kwargs.get('uses_task_dependencies', None)
        self.task_factory = kwargs.get('task_factory', None)
