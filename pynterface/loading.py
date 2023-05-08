from threading import Thread
from time import sleep

class Loader():
    
    def __init__(self, message: str, cycle: list[str], delay: int, hide_cursor: bool = False) -> None:

        """
        Creates a new Loader with a message which appears on the same line as the cycler.
        """

        assert sum([not isinstance(part, str) for part in cycle]) == 0, "Cycle must consist of strings only."
        assert isinstance(message, str), "Message must be a string."

        self.max_len = max([len(item) for item in cycle])

        # stores customization values
        self.cycle = cycle
        self.message = message
        self.delay = delay / 1000
        self.hide_cursor = hide_cursor

        # temporary null value 
        self.runner = None
        
        # for cycling
        self.mod = len(cycle)
        self.index = 0

        # for states
        self.over = False
        self.paused = False
        
        if self.hide_cursor:
            print("\033[?25l", end="")

    @property
    def state(self):
        """
        Adjusts the index and returns it.
        """
        self.index += 1
        self.index %= self.mod
        return self.index

    def run(self):
        """
        Thread that runs the loader.
        """
        try:
            while not self.over:
                if self.paused:
                    continue
                item = self.cycle[self.state]
                self.__display(item)
                sleep(self.delay)
        finally:
            if self.hide_cursor:
                print("\033[?25h", end="")

    def __display(self, item):
        """
        Clears and displays the message.
        """
        self.__clear()
        print("\r" + self.message + item, end="")

    def __enter__(self):
        self.runner = Thread(target=self.run)
        self.runner.start()
        return self

    def __exit__(self, _, __, ___):

        # ends and clears
        self.over = True
        self.__clear()

        # print newline
        print(end="\r") 

        # end thread
        self.runner.join()

    def print_above(self, message):
        """
        Prints the entered string above the spinner.
        """

        # pause and print message
        self.paused = True
        self.__clear()
        print("\r" + message)
        self.paused = False

        # reset the display
        self.__display(self.cycle[self.state])
        sleep(self.delay)

    def __clear(self):
        """
        Clears the message.
        """
        print("\r" + " " * (len(self.message) + self.max_len + 1), end="")

class Spinner(Loader):
    def __init__(self, message: str, delay: int = 100) -> None:
        """
        A Spinner preset based on the Loader class.
        You must enter a message, and the delay is defaulted to 100 milliseconds, but is optionally changeable.
        """
        super().__init__(message=message, cycle=["/", "-", "\\", "|"], delay=delay, hide_cursor=True)

if __name__ == "__main__":
    with Spinner(message="Loading ") as loader:
        sum = 0
        for i in range(1, 100_000_000):
            if i % 30_000_000 == 0:
                loader.print_above("message")
            sum += 1

    print("done")