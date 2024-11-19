from typing import Generator

from . import fasta_like_file_service

class FastqFileService(fasta_like_file_service.FastaLikeFileService):

    separator = "@"

    @classmethod
    def parse_string(cls, string: str)->dict:

        lines    = string.split("\n")
        header   = lines[0]
        i        = [i for i, line in enumerate(lines[1:]) if line[0]=="+"][0]
        sequence = "".join(lines[:i])
        info     = lines[i]
        quality  = "".join(lines[i+1:])

        return {"header": header,
                "sequence": sequence,
                "info": info,
                "quality": quality,
                "length": len(sequence),
                "file_type": "fastq"}

    @classmethod
    def parse_dict(cls, read: dict)->str:
        
        return "\n".join([read["header"],read["sequence"],read["info"],read["quality"]])+"\n"
    
    @classmethod
    def read(cls, file_path:str)->Generator:
        
        with open(file_path, "r") as f:

            while True:

                try:
                    header          = f.readline()
                    sequence_lines  = []
                    quality_lines   = []
                    while True:
                        line = f.readline()
                        if not line[0] == "+":
                            sequence_lines.append(line)
                        else:
                            info = line
                            break
                    for i in range(len(sequence_lines)):
                        quality_lines.append(f.readline())

                    yield  {"header": header,
                            "sequence": "".join(sequence_lines),
                            "info": info,
                            "quality": "".join(quality_lines),
                            "length": len("".join(sequence_lines)),
                            "file_type": "fastq"}
                        
                except:
                    return