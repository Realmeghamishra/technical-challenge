# We need to write code that will query the meta data of an instance within AWS or Azure or GCP
# and provide a json formatted output.
# The choice of language and implementation is up to you.

from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
import json

def get_azure_instance_metadata():
    instance_metadata = {}
    subscription_id = '3932e3d7-3652-42d1-8f03-9eb4735ad5aa'  # Replace 'your-subscription-id' with your Azure subscription ID
    vm_id = '/subscriptions/3932e3d7-3652-42d1-8f03-9eb4735ad5aa/resourceGroups/adds-rg/providers/Microsoft.Compute/virtualMachines/Ldap-VM'  # Replace 'your-vm-id' with the actual virtual machine ID

    credentials = DefaultAzureCredential()
    compute_client = ComputeManagementClient(credentials, subscription_id)

    vm = compute_client.virtual_machines.get(resource_group_name='adds-rg', vm_name='Ldap-VM')
    # Replace 'your-resource-group' and 'your-vm-name' with the appropriate resource group and VM name

    instance_metadata['vm_id'] = vm.id
    instance_metadata['vm_size'] = vm.hardware_profile.vm_size
    instance_metadata['location'] = vm.location

    return json.dumps(instance_metadata, indent=2)

print(get_azure_instance_metadata())


#Output
#{
#  "vm_id": "/subscriptions/3932e3d7-3652-42d1-8f03-9eb4735ad5aa/resourceGroups/adds-rg/providers/Microsoft.Compute/virtualMachines/Ldap-VM",      
#  "vm_size": "Standard_B2s",
#  "location": "centralindia"
#}
