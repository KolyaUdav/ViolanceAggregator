import os


IMG_DIR = 'images/'
STATIC_DIR = '/'

TOTAL_PERCENTS_VIOLANCED = 'общий_процент_насилия'
TOTAL_PERCENTS_NOT_VIOLANCED = 'общий_процент_отсутствия_насилия'

AGE_TOTAL_PERCENTS_VIOLANCED = 'насилие_в_диапазоне_возраста'
AGE_TOTAL_PERCENTS_NOT_VIOLANCED = 'отсутствие_насилия_в_диапазоне_возраста'

AGE_COLUMN_NAME = 'возраст'

COLUMN_NAMES = [
    'пренебрежение_нуждами',
    'физическое_насилие_дома',
    'физическое_насилие_в_школе',
    'психологическое_насилие_дома',
    'психологическое_насилие_в_школе',
    'сексуальное_насилие_дома',
    'сексуальное_насилие_в_школе'
]

MIN_AGE = 10
MAX_AGE = 17
