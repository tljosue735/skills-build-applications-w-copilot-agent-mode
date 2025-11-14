from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create(name='Test User', email='test@example.com', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='Test Desc')
        self.activity = Activity.objects.create(user=self.user, type='Run', duration=10, date='2025-01-01')
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=10, rank=1)

    def test_user(self):
        self.assertEqual(self.user.name, 'Test User')

    def test_team(self):
        self.assertEqual(self.team.name, 'Test Team')

    def test_activity(self):
        self.assertEqual(self.activity.type, 'Run')

    def test_workout(self):
        self.assertEqual(self.workout.name, 'Test Workout')

    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.rank, 1)
