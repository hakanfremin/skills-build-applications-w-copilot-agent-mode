from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from octofit_tracker.models import Team, Activity, Leaderboard, Workout

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password')
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password')
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password')
        captain = User.objects.create_user(username='captain', email='captain@marvel.com', password='password')

        # Create activities
        Activity.objects.create(user='ironman', activity_type='Running', duration=30)
        Activity.objects.create(user='batman', activity_type='Cycling', duration=45)
        Activity.objects.create(user='superman', activity_type='Swimming', duration=60)
        Activity.objects.create(user='captain', activity_type='Yoga', duration=20)

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=100)
        Leaderboard.objects.create(team='DC', points=90)

        # Create workouts
        Workout.objects.create(name='Pushups', difficulty='Easy')
        Workout.objects.create(name='Pullups', difficulty='Medium')
        Workout.objects.create(name='Squats', difficulty='Hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
