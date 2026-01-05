import pandas as pd
import random
import os

# Configuration
NUM_PROPERTIES = 10000
ROOMS_PER_PROPERTY = (5, 12)  # min, max
NOTES_PER_ROOM = (1, 3)
IMAGES_PER_ROOM = (1, 3)

# Data templates
CITIES = ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai', 'Pune', 'Kolkata', 'Ahmedabad', 'Jaipur', 'Noida']
ROOM_TYPES = ['Living Room', 'Bedroom', 'Kitchen', 'Bathroom', 'Dining Room', 'Study', 'Guest Room', 'Balcony']
DEFECT_TYPES = ['damp', 'crack', 'exposed wiring', 'poor finishing', 'structural risk', 'safe']

INSPECTION_TEMPLATES = {
    'damp': [
        'Visible damp patches near the ceiling and wall corners',
        'Water seepage detected on walls',
        'Moisture stains visible near window frames',
        'Damp spots on floor near plumbing',
        'Ceiling shows signs of water damage and dampness'
    ],
    'crack': [
        'Minor wall cracks observed near window frame',
        'Hairline cracks visible on ceiling',
        'Crack observed in supporting beam, possible structural concern',
        'Multiple small cracks on exterior wall',
        'Vertical crack noticed on load-bearing wall'
    ],
    'exposed wiring': [
        'Exposed electrical wiring under the sink area',
        'Loose wires hanging from ceiling fixture',
        'Open electrical panel with exposed connections',
        'Damaged wire insulation near switch board',
        'Unprotected electrical cables running along wall'
    ],
    'poor finishing': [
        'Uneven paint application on walls',
        'Poorly finished flooring with visible gaps',
        'Rough plastering on walls and ceiling',
        'Paint peeling off in multiple areas',
        'Incomplete trim work around doors and windows'
    ],
    'structural risk': [
        'Crack observed in supporting beam, possible structural concern',
        'Sagging ceiling indicates structural weakness',
        'Foundation cracks visible in basement',
        'Load-bearing wall shows signs of stress',
        'Compromised structural integrity in roof support'
    ],
    'safe': [
        'Room appears clean and safe',
        'No defects observed in this area',
        'All systems functioning properly',
        'Well maintained with no visible issues',
        'Inspection passed without concerns'
    ]
}

print("Generating properties...")
properties = []
for i in range(1, NUM_PROPERTIES + 1):
    properties.append({
        'PROPERTY_ID': i,
        'ADDRESS': f'{random.choice(["Green", "Sky", "Blue", "Silver", "Golden", "Pearl"])} {random.choice(["Heights", "Residency", "Tower", "Apartments", "Villa", "Estate"])} Sector {random.randint(1, 100)}',
        'CITY': random.choice(CITIES)
    })
df_properties = pd.DataFrame(properties)

print("Generating rooms...")
rooms = []
room_id = 1
for prop_id in range(1, NUM_PROPERTIES + 1):
    num_rooms = random.randint(*ROOMS_PER_PROPERTY)
    for _ in range(num_rooms):
        rooms.append({
            'ROOM_ID': room_id,
            'PROPERTY_ID': prop_id,
            'ROOM_TYPE': random.choice(ROOM_TYPES)
        })
        room_id += 1
df_rooms = pd.DataFrame(rooms)

print(f"Generating inspection notes for {len(rooms)} rooms...")
notes = []
note_id = 1
for room in rooms:
    num_notes = random.randint(*NOTES_PER_ROOM)
    for _ in range(num_notes):
        defect_type = random.choice(DEFECT_TYPES)
        notes.append({
            'NOTE_ID': note_id,
            'ROOM_ID': room['ROOM_ID'],
            'TEXT': f'"{random.choice(INSPECTION_TEMPLATES[defect_type])}"'
        })
        note_id += 1
df_notes = pd.DataFrame(notes)

print(f"Generating image metadata for {len(rooms)} rooms...")
images = []
image_id = 1
for room in rooms:
    num_images = random.randint(*IMAGES_PER_ROOM)
    for _ in range(num_images):
        defect = random.choice(DEFECT_TYPES)
        images.append({
            'IMAGE_ID': image_id,
            'ROOM_ID': room['ROOM_ID'],
            'LABEL': defect,
            'CONFIDENCE': round(random.uniform(0.75, 0.99), 2)
        })
        image_id += 1
df_images = pd.DataFrame(images)

# Save to CSV
base_dir = os.path.join(os.path.dirname(__file__), '..', 'data')

print(f"\nSaving data to CSV files...")
df_properties.to_csv(os.path.join(base_dir, 'property.csv'), index=False)
print(f"  - property.csv: {len(df_properties)} rows")

df_rooms.to_csv(os.path.join(base_dir, 'room.csv'), index=False)
print(f"  - room.csv: {len(df_rooms)} rows")

df_notes.to_csv(os.path.join(base_dir, 'inspection_note.csv'), index=False)
print(f"  - inspection_note.csv: {len(df_notes)} rows")

df_images.to_csv(os.path.join(base_dir, 'image_metadata.csv'), index=False)
print(f"  - image_metadata.csv: {len(df_images)} rows")

total_rows = len(df_properties) + len(df_rooms) + len(df_notes) + len(df_images)
print(f"\nTotal rows across all tables: {total_rows:,}")
print("Dataset generation completed!")
