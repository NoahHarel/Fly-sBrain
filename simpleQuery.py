#import numpy as np
#import pandas as pd
#import hvplot.pandas

from neuprint import Client, fetch_custom, fetch_neurons
from neuprint import fetch_roi_hierarchy


TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im5vYWhoYXJlbEBtYWlsLnRhdS5hYy5pbCIsImxldmVsIjoibm9hdXRoIiwiaW1hZ2UtdXJsIjoiaHR0cHM6Ly9saDYuZ29vZ2xldXNlcmNvbnRlbnQuY29tLy13dGxuQlZqSkE2OC9BQUFBQUFBQUFBSS9BQUFBQUFBQUFBQS9BQUtXSkpObGJ4UVc5NXdRd19oZlhxcVM1ZFJ4MTNvXzR3L3Bob3RvLmpwZz9zej01MD9zej01MCIsImV4cCI6MTc2NjU5NTAzMn0.4At5bDlTYiVWawEUmO2uoyBn2u7eu6-UJwJbuvFCz90'

c = Client('neuprint.janelia.org', 'hemibrain:v1.0.1')

print(fetch_roi_hierarchy(False, mark_primary=True, format='text'))
