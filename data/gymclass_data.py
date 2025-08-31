from models.gym_class import GymClassModel
from datetime import datetime, timedelta

gym_classes_list = [
    GymClassModel(
        title="Morning Yoga",
        description="Start your day with a relaxing yoga class.",
        category_id=1,  # assuming 'Yoga' category = id 1
        start_time=datetime(2025, 9, 1, 8, 0),
        end_time=datetime(2025, 9, 1, 9, 0)
    ),
  
    GymClassModel(
    title="Full Body Strength",
    description="A comprehensive workout targeting all major muscle groups.",
    category_id=4,  # 'Strength Training' = 4
    start_time=datetime(2025, 9, 2, 18, 0),
    end_time=datetime(2025, 9, 2, 19, 0)
    ),
    GymClassModel(
    title="Upper Body Blast",
    description="Focuses on building strength in the chest, back, shoulders, and arms.",
    category_id=4,   # 'Strength Training' = 4
    start_time=datetime(2025, 9, 4, 17, 30),
    end_time=datetime(2025, 9, 4, 18, 30)
),
    GymClassModel(
    title="Cardio Burnout",
    description="High-speed cardio routines to improve stamina and burn calories fast.",
    category_id=3,  # 'Cardio' = 3
    start_time=datetime(2025, 9, 2, 9, 0),
    end_time=datetime(2025, 9, 2, 9, 45)
),

]
