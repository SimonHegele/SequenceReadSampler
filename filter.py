import logging

from sys import stdout

from my_argument_parser     import MyArgumentParser
from sequence_mapping_queue import SequenceMappingQueue
from file_services.utils    import get_read_writer

def setup_logging():

    stdout_handler = logging.StreamHandler(stream=stdout)

    logging.basicConfig(level    = logging.INFO,
                        format   = "%(asctime)s %(levelname)s %(message)s",
                        datefmt  = "%d-%m-%Y %H:%M:%S",
                        handlers=[stdout_handler]
                        )

def filter_reads(reads_in, reads_out, paf, filter):

    filtered_reads = []

    progress = 0

    for read, mappings in SequenceMappingQueue(reads_in, paf).queue():

        if progress%100_000==0:
            logging.info(f"Filtered {len(filtered_reads)} from {int(progress/1000)}k reads")
        
        progress += 1

        if any(mappings):

                for m in mappings:
                    if filter in m["target_name"]:
                        filtered_reads.append(read)
                        break

    
    logging.info(f"Filtered {len(filtered_reads)} from {int(progress/1000)}k reads")
    logging.info(f"Writing filtered reads to file")
                        
    get_read_writer(filtered_reads[0]).write(reads_out, filtered_reads)

    logging.info(f"Done")

def main():

    args = MyArgumentParser().parse_args()

    setup_logging()

    filter_reads(args.reads_in, args.reads_out, args.paf, args.filter)

if __name__ == '__main__':
    main()