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


def gui_to_criteria():
    # defaults for now, will be the function to tie GUI and backend together
    # body_id_in = [387023620, 387364605, 416642425]
    # instance_in = "OA-VPM3"
    # type_in = 'PENPEN_b(PEN2)'

    input_rois_in = ['AL(R)']
    output_rois_in = ['AL(L)']

    criteria_in = NC(inputRois=input_rois_in, outputRois=output_rois_in)

    return criteria_in


def find_neurons(criteria):
    neuron_df, roi_counts_df = fetch_neurons(criteria)
    return neuron_df[['bodyId', 'instance', 'type', 'pre', 'post', 'status', 'cropped', 'size']]

def fetch_adj_and_merge(criteria):
    default_criteria_for_test = NC(inputRois='AB(L)')
    neuron_df, conn_df = fetch_adjacencies(criteria, default_criteria_for_test)
    conn_df = merge_neuron_properties(neuron_df, conn_df, ['type', 'instance'])
    return conn_df

def simple_query():
    criteria_find = gui_to_criteria()
    print('...\n')
    df1 = find_neurons(criteria_find)
    print('...\n')
    print('The total count of pre-synaptic and post-synaptic points within each neuron'
          ' are given in the pre and post columns \n')
    #   print(df1)
    print('...\n')
    df1.to_csv('fetch_neurons.csv', index=False)
    print('fetch_neurons.csv file is now ready \n')
    print('...\n')
    df2 = fetch_adj_and_merge(criteria_find)
    print('Fetching all direct connections between two sets of neurons\n')
    #   print(df2)
    print('...\n')
    df2.to_csv('adjacency_table.csv', index=False)
    print('adjacency_table.csv file is now ready\n')

def get_all_neurons_roi_counts():
    crit = NC()
    neuron_df, roi_counts_df = fetch_neurons(crit)
    neuron_df = neuron_df[['bodyId', 'instance', 'type', 'pre', 'post', 'status', 'cropped', 'size']]
    neuron_df.to_csv('all_neurons.csv', index = False)
    roi_counts_df.to_csv('all_roi_counts', index = False)

# def get_all_connections():


if __name__ == '__main__':
    get_all_neurons_roi_counts()

