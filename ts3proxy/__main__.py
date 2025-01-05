from .ts3proxy import main
from pathlib import Path
import logging

logging.basicConfig(
    level=20,
    format='[%(asctime)s] %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

services = []

for cfg_path in Path('./config').glob('*.yml'):
    logging.info('reading file {cfg_path}'.format(cfg_path=cfg_path))
    services.extend(main(cfg_path))

try:
    # now all services are started
    # wait for threads to stop or for keyboard interrupt
    for service in services:
        service.thread.join()
except KeyboardInterrupt:
    logging.info('received KeyboardInterrupt, stopping threads')
    for service in services:
        service.stop_thread()
    logging.info('closed sockets, waiting for threads to stop')
    for service in services:
        service.thread.join()
    logging.info('threads stopped')