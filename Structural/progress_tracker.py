# structural/progress_tracker.py

class ProgressTracker:
    """
    A class to track progress on a series of tasks. 

    Attributes:
        total_tasks (int): The total number of tasks to complete.
        completed_tasks (int): The number of tasks that have been completed.

    Methods:
        complete_task(): Marks a task as completed and updates progress.
        get_progress(): Returns the progress as a percentage.
        __str__(): Returns a string representation of the current progress status.
    """

    def __init__(self, total_tasks: int):
        """
        Initializes the ProgressTracker with a specified number of tasks.

        Args:
            total_tasks (int): The total number of tasks to complete.
        """
        if total_tasks < 0:
            raise ValueError("Total tasks must be a non-negative integer.")
        self.total_tasks = total_tasks
        self.completed_tasks = 0

    def complete_task(self) -> None:
        """
        Marks a task as completed and updates the completed task count.

        Raises:
            RuntimeError: If all tasks have already been completed.
        """
        if self.completed_tasks >= self.total_tasks:
            raise RuntimeError("All tasks have already been completed.")
        self.completed_tasks += 1

    def get_progress(self) -> float:
        """
        Calculates and returns the progress as a percentage.

        Returns:
            float: Progress percentage.
        """
        if self.total_tasks == 0:
            return 0.0
        return (self.completed_tasks / self.total_tasks) * 100

    def __str__(self) -> str:
        """
        Returns a string representation of the current progress status.

        Returns:
            str: Summary of progress.
        """
        return f"Completed {self.completed_tasks} of {self.total_tasks} tasks. Progress: {self.get_progress():.2f}%."


# Sample usage
if __name__ == "__main__":
    tracker = ProgressTracker(total_tasks=5)
    print(tracker)

    tracker.complete_task()
    print(tracker)

    tracker.complete_task()
    tracker.complete_task()
    print(tracker)

    tracker.complete_task()
    tracker.complete_task()

    try:
        tracker.complete_task()  # This should raise an exception
    except RuntimeError as e:
        print(e)