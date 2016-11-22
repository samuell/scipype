# Copyright (c) 2016 Samuel Lampa <samuel.lampa@gmail.com>
import re
from collections import deque

class Workflow(object):
    processes = {}

    def add_process(self, process_name, process):
        self.processes[process_name] = process

    def run(self):
        while True:
            for process_name, process in self.processes.iteritems():
                print '-'*80
                print 'Now processing: %s' % process_name
                print '-'*80
                process.process_next()

class Channel(object):
    items = deque()

    def send(self, target):
        self.items.append(target)

    def recv(self):
        return self.items.popleft()


class Process(object):
    command_pattern = ''

    def __init__(self, command_pattern):
        self.command_pattern = command_pattern

        ms = re.findall('\{([:a-z0-9]+)\}', command_pattern)
        for m in ms:
            bits = m.split(':')
            field_type = bits[0] # [i]nput, [o]utput or [p]arameter
            field_name = bits[1]

            if field_type == 'i':
                setattr(self, 'inp_%s' % field_name, Channel())
            elif field_type == 'o':
                setattr(self, 'outp_%s' % field_name, Channel())

    def process_next(self):
        print 'Receiveing inputs ...'
        for field_name, channel in self.__dict__.iteritems():
            if field_name[0:4] == 'inp_':
                try:
                    target = channel.recv()
                except IndexError as e:
                    pass

        print 'Formatting commands (Not yet implemented) ...'
        # TODO: Implement ...

        print 'Executing commands (Not yet implemented) ...'
        # TODO: Implement ...

        print 'Sending outputs (Not yet implemented) ...'
        # TODO: Implement ...


class Target(object):
    pass


class FileTarget(Target):
    pass
