from typing import List, Optional

import statesman


class ProcessLifecycle(statesman.StateMachine):
    class States(statesman.StateEnum):
        starting = "Starting..."
        running = "Running..."
        stopping = "Stopping..."
        stopped = "Terminated."

    # Track state about the process we are running
    command: Optional[str] = None
    pid: Optional[int] = None
    logs: List[str] = []

    # initial state entry point
    @statesman.event(None, States.starting)
    async def start(self, command: str) -> None:
        """ "Start a process."""
        self.command = command
        self.pid = 31337
        self.logs.clear()  # Flush logs between runs

    @statesman.event(source=States.starting, target=States.running)
    async def run(self, transition: statesman.Transition) -> None:
        """Mark the process as running."""
        self.logs.append(f'Process pid {self.pid} is now running (command="{self.command}")')

    @statesman.event(source=States.running, target=States.stopping)
    async def stop(self) -> None:
        """Stop a running process."""
        self.logs.append(f'Shutting down pid {self.pid} (command="{self.command}")')

    @statesman.event(source=States.stopping, target=States.stopped)
    async def terminate(self) -> None:
        """Terminate a running process."""
        self.logs.append(f'Terminated pid {self.pid} ("{self.command}")')
        self.command = None
        self.pid = None

    @statesman.enter_state(States.stopping)
    async def _print_status(self) -> None:
        print("Entering stopped status!")

    @statesman.after_event("run")
    async def _after_run(self) -> None:
        print("running...")

    async def after_transition(self, transition: statesman.Transition) -> None:
        if transition.event and transition.event.name == "stop":
            await self.terminate()


async def _examples():
    # Let's play.
    state_machine = ProcessLifecycle()
    await state_machine.start("ls -al")
    assert state_machine.command == "ls -al"
    assert state_machine.pid == 31337
    assert state_machine.state == ProcessLifecycle.States.starting

    await state_machine.run()
    assert state_machine.logs == ['Process pid 31337 is now running (command="ls -al")']

    await state_machine.stop()
    assert state_machine.logs == [
        'Process pid 31337 is now running (command="ls -al")',
        'Shutting down pid 31337 (command="ls -al")',
        'Terminated pid 31337 ("ls -al")',
    ]

    # Or start in a specific state
    state_machine = ProcessLifecycle(state=ProcessLifecycle.States.running)

    # Transition to a specific state
    await state_machine.enter_state(ProcessLifecycle.States.stopping)

    # Trigger an event
    await state_machine.trigger_event("stop", key="value")
