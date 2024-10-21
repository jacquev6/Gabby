import unittest


class AdaptationTestCase(unittest.TestCase):
    maxDiff = None

    # @todo Remove default value, enforce testing the delta
    def do_test(self, exercise, expected_adapted, expected_delta=None):
        actual_adapted = exercise.make_adapted()
        if actual_adapted != expected_adapted:
            print("actual_adapted:", actual_adapted)
        self.assertEqual(actual_adapted, expected_adapted)
        if expected_delta is not None:
            actual_delta = exercise.make_delta()
            if actual_delta != expected_delta:
                print("actual_delta:", actual_delta)
            self.assertEqual(actual_delta, expected_delta)
