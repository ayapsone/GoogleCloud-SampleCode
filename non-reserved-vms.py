# Print instances not using reservation

# This script uses the google.cloud.compute_v1.Client class to create a client for the Compute Engine API.
# It then lists all of the instances in the specified zone, and iterates over them to check if each one has a reservation.
# If an instance does not have a reservation, it prints the instance's name.

import google.cloud

# Create a client for the Compute Engine API.
compute_client = google.cloud.compute_v1.Client()

# List all of the instances in the specified zone.
instance_list = compute_client.projects().locations().instances()

# Iterate over the instances and check if each one has a reservation.
for instance in instance_list:
    if not instance.reservation:
        print(f"{instance.name} is not using a reservation.")
