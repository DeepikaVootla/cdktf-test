#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack, TerraformOutput
from imports.azurerm.provider import AzurermProvider
from imports.azurerm.resource_group import ResourceGroup


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        AzurermProvider(self, "azurerm", features={})

        rg = ResourceGroup(self, "rg",
                           name="cdktf-rg",
                           location="East US")

        TerraformOutput(self, "resource_group_name", value=rg.name)

app = App()
MyStack(app, "cdktf-azure-demo")

app.synth()
