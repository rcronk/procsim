import queue


class Generator():
    """
    These generate outputs that will flow to Processors.
    """
    def __init__(self, outputs):
        """
        Set up the generator.
        """
        self.outputs = outputs


class Processor():
    """
    These convert inputs into outputs.
    """
    def __init__(self, inputs, outputs):
        """
        Set up the processor.
        """
        self.inputs = inputs
        self.outputs = outputs


class LoadBalancer():
    """
    This directs inputs to a collection of Processors.
    """
    def __init__(self, inputs, processors):
        """
        Set up the LoadBalancer.
        """
        self.inputs = inputs
        self.processors = processors

# Could we define the process as a graph with nodes being generators or processors and edges being queues?