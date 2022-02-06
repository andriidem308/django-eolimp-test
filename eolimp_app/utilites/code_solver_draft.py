import asyncio
import os
import re
import sys
import time
from io import StringIO


def get_testfile_id(f):
    return f.split('_')[-1]


def split_files(tests):
    files_dict = {}
    input_files = [file_in for file_in in tests if 'input_' in file_in]
    output_files = [file_out for file_out in tests if 'output_' in file_out]

    for file_in in input_files:
        file_in_id = get_testfile_id(file_in)
        for file_out in output_files:
            if get_testfile_id(file_out) == file_in_id:
                files_dict[file_in] = file_out

    return files_dict


def get_solution_code(solution_file):
    solution = open(solution_file, 'r')
    return solution.read()


tests = os.listdir('tests')
solution_file = 'solution.py'


class AsyncIterator:
    def __init__(self, seq):
        self.iter = iter(seq)

    def __aiter__(self):
        return self

    async def __anext__(self):
        try:
            return next(self.iter)
        except StopIteration:
            raise StopAsyncIteration


async def solver(solution_file, tests, max_exec_time):
    tests_map = split_files(tests)
    code_text = get_solution_code(solution_file)

    tests_results = []

    async for test_in, test_out in AsyncIterator(tests_map.items()):
        res, exec_time = await check_single_test(code_text, test_in, test_out)
        if exec_time > max_exec_time:
            tests_results.append(False)
        else:
            tests_results.append(res)

    score_percents = sum(tests_results)/len(tests_results)
    return score_percents


async def check_single_test(code, input_filename, output_filename):
    input_text = open(f'tests/{input_filename}').read()
    output_text = open(f'tests/{output_filename}').read()

    res_code = code[:]

    inputs = input_text.split('\n')
    found_inputs = re.findall(r'input\(.*?\)', res_code)
    for inp in inputs:
        res_code = res_code.replace(found_inputs.pop(0), f"'{inp}'", 1)

    start_time = time.time()
    code_out, code_err = exec_code(res_code)
    exec_time = (time.time() - start_time) * 1000     # ms

    return (code_out.strip() == output_text), exec_time


def exec_code(code):
    code_out, code_err = StringIO(), StringIO()
    sys.stdout, sys.stderr = code_out, code_err
    exec(code)
    sys.stdout, sys.stderr = sys.__stdout__, sys.__stderr__

    return code_out.getvalue(), code_err.getvalue()


loop = asyncio.get_event_loop()
result = loop.run_until_complete(solver(solution_file, tests, 1000))

print(result)