from argparse import ArgumentParser

class MyArgumentParser(ArgumentParser):

    prog        =   "ToyReads"

    description =   """
                    ----------
                    Commandline tool for the generation of toy sequence read files.
                    
                    Filters for sequence reads that were mapped to the same reference
                    sequence by minimap2 in single-threaded mode.
                    """
    
    help = {
            "reads_in":  "Path to file with sequence reads (.fasta or .fastq, not compressed)",
            "reads_out": "Path to output file",
            "paf":       "Mapping file (.paf from single threaded minimap2)",
            "filter":    "Name of the reference sequence to filter for.",
        }
    
    def __init__(self) -> None:

        super().__init__(prog=self.prog, description=self.description)
        
        self.add_argument("reads_in",  type=str, help=self.help["reads_in"])
        self.add_argument("reads_out", type=str, help=self.help["reads_out"])
        self.add_argument("paf",       type=str, help=self.help["paf"])
        self.add_argument("filter",    type=str, help=self.help["filter"])