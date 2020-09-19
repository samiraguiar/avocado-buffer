import logging
from avocado import Test
from avocado.utils import process
from aexpect.client import run_fg

class Run(Test):
    def test_buffered(self):
        logging.debug('[logme] Test #1 | process with buffer (no live logging)')
        exit_status = process.run('python sample.py').exit_status
        self.assertEqual(exit_status, 0)

    def test_unbuffered_python(self):
        logging.debug('[logme] Test #2 | process without buffer via python -u (live logging ok)')
        exit_status = process.run('python -u sample.py').exit_status
        self.assertEqual(exit_status, 0)

    def test_unbuffered_script(self):
        logging.debug('[logme] Test #3 | process without buffer via script (live logging ok)')
        exit_status = process.run('script -q -c "python sample.py" /dev/null').exit_status
        self.assertEqual(exit_status, 0)

    def test_unbuffered_aexpect(self):
        def output_func(output):
            logging.debug(output)

        logging.debug('[logme] Test #4 | process without buffer via aexpect (live logging ok)')
        exit_status, _ = run_fg('python sample.py', output_func=output_func, timeout=60)
        self.assertEqual(exit_status, 0)
