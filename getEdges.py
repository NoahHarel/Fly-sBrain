#   imports
from neuprint import Client
from neuprint import fetch_adjacencies, merge_neuron_properties, NeuronCriteria as NC
from neuprint import fetch_neurons

#   Client creation - option to receive user' own TOKEN
TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im5vYWhoYXJlbEBtYWlsLnRhdS5h' \
        'Yy5pbCIsImxldmVsIjoibm9hdXRoIiwiaW1hZ2UtdXJsIjoiaHR0cHM6Ly9saDYuZ29vZ2xldXNlc' \
        'mNvbnRlbnQuY29tLy13dGxuQlZqSkE2OC9BQUFBQUFBQUFBSS9BQUFBQUFBQUFBQS9BQUtXSkpObG' \
        'J4UVc5NXdRd19oZlhxcVM1ZFJ4MTNvXzR3L3Bob3RvLmpwZz9zej01MD9zej01MCIsImV4cCI6MTc' \
        '2NjU5NTAzMn0.4At5bDlTYiVWawEUmO2uoyBn2u7eu6-UJwJbuvFCz90'

c = Client(server='neuprint.janelia.org', dataset='hemibrain:v1.0.1', token = TOKEN)

#runs for hours
def get_all_connections():
    connections_crit = NC()
    neuron_df, conn_df = fetch_adjacencies(connections_crit, None)
    print('got adjacencies!!!!!!!!!!!!!!!!!!!!!!')
    conn_df.to_csv('all_connections.csv', index = False)
    print('got csv file!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

if __name__ == '__main__':
    # get_all_neurons_roi_counts()
    get_all_connections()

