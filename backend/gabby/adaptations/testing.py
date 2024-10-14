import unittest


class AdaptationTestCase(unittest.TestCase):
    maxDiff = None

    # @todo Remove default value, enforce testing the delta
    def do_test(self, exercise, expected_adapted, expected_delta=None):
        self.assertEqual(exercise.make_adapted(), expected_adapted)
        if expected_delta is not None:
            self.assertEqual(exercise.make_delta(), expected_delta)
