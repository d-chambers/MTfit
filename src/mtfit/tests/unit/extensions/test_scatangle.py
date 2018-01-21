import unittest
import glob
import os

from MTfit.extensions.scatangle import parse_scatangle


class ScatangleTestCase(unittest.TestCase):

    def setUp(self):
        self.existing_scatangle_files = glob.glob('*.scatangle')

    def tearDown(self):
        for fname in glob.glob('*.scatangle'):
            if fname not in self.existing_scatangle_files:
                try:
                    os.remove(fname)
                except Exception:
                    print('Cannot remove {}'.format(fname))
        import gc
        try:
            os.remove('test.scatangle')
        except Exception:
            pass
        gc.collect()

    def station_angles(self):
        out = "504.7\n"
        out += "S0271   231.1   154.7\n"
        out += "S0649   42.9    109.7\n"
        out += "S0484   21.2    145.4\n"
        out += "S0263   256.4   122.7\n"
        out += "S0142   197.4   137.6\n"
        out += "S0244   229.7   148.1\n"
        out += "S0415   75.6    122.8\n"
        out += "S0065   187.5   126.1\n"
        out += "S0362   85.3    128.2\n"
        out += "S0450   307.5   137.7\n"
        out += "S0534   355.8   138.2\n"
        out += "S0641   14.7    120.2\n"
        out += "S0155   123.5   117\n"
        out += "S0162   231.8   127.5\n"
        out += "S0650   45.9    108.2\n"
        out += "S0195   193.8   147.3\n"
        out += "S0517   53.7    124.2\n"
        out += "S0004   218.4   109.8\n"
        out += "S0588   12.9    128.6\n"
        out += "S0377   325.5   165.3\n"
        out += "S0618   29.4    120.5\n"
        out += "S0347   278.9   149.5\n"
        out += "S0529   326.1   131.7\n"
        out += "S0083   223.7   118.2\n"
        out += "S0595   42.6    117.8\n"
        out += "S0236   253.6   118.6\n"
        out += '\n'
        out += "504.7\n"
        out += "S0271   230.9   154.8\n"
        out += "S0649   43      109.8\n"
        out += "S0484   21.3    145.4\n"
        out += "S0263   256.4   122.8\n"
        out += "S0142   197.3   137.6\n"
        out += "S0244   229.6   148.1\n"
        out += "S0415   75.7    122.8\n"
        out += "S0065   187.4   126.1\n"
        out += "S0362   85.3    128.2\n"
        out += "S0450   307.5   137.8\n"
        out += "S0534   355.7   138.3\n"
        out += "S0641   14.8    120.3\n"
        out += "S0155   123.5   117.1\n"
        out += "S0162   231.7   127.6\n"
        out += "S0650   45.9    108.3\n"
        out += "S0195   193.6   147.3\n"
        out += "S0517   53.7    124.2\n"
        out += "S0004   218.3   109.9\n"
        out += "S0588   13      128.7\n"
        out += "S0377   325.7   165.4\n"
        out += "S0618   29.5    120.5\n"
        out += "S0347   278.9   149.6\n"
        out += "S0529   326.1   131.8\n"
        out += "S0083   223.7   118.2\n"
        out += "S0595   42.7    117.9\n"
        out += "S0236   253.5   118.7\n"
        out += "\n"
        return out

    def test_parser_scatangle(self, parser=parse_scatangle, *args):
        open('test.scatangle', 'w').write(self.station_angles())
        A, B = parser('test.scatangle')
        self.assertEqual(B, [504.7, 504.7])
        self.assertEqual(len(A), 2)
        self.assertEqual(sorted(A[0].keys()), ['Azimuth', 'Name', 'TakeOffAngle'])
        A, B = parser('test.scatangle', bin_size=1)
        self.assertEqual(B, [1009.4])
        self.assertEqual(len(A), 1)
        self.assertEqual(sorted(A[0].keys()), ['Azimuth', 'Name', 'TakeOffAngle'])
        open('test.scatangle', 'w').write('\n'.join([self.station_angles() for i in range(40)]))
        AC, BC = parser('test.scatangle', bin_size=1)
        APy, BPy = parser('test.scatangle', bin_size=1, _use_c=False)
        self.assertEqual(len(APy), 1)
        self.assertEqual(len(AC), 1)
        self.assertEqual(BPy, BC)
        os.remove('test.scatangle')


def test_suite(verbosity=2):
    tests = []
    tests.append(unittest.TestLoader().loadTestsFromTestCase(ScatangleTestCase))
    return unittest.TestSuite(tests)


def run_tests(verbosity=1):
    """Run inversion module tests."""
    suite = test_suite(verbosity)
    unittest.TextTestRunner(verbosity=verbosity).run(suite)


if __name__ == "__main__":
    run_tests()
