class OldAdaptation:
    def __init__(self, exercise):
        self.exercise = exercise

    def make_adapted(self):
        self.exercise.adaptation = self.to_new_adaptation()
        return self.exercise.make_adapted()

    def make_delta(self):
        self.exercise.adaptation = self.to_new_adaptation()
        return self.exercise.make_delta()
