locals {
  resource_group_name = var.rg_name
  location = "eastus"
}

resource "azurerm_resource_group" "resource_group" {
  name     = local.resource_group_name
  location = "southcentralus"
}

resource "azurerm_service_plan" "app_service_plan" {
  name                = "openai-function-asp"
  resource_group_name = azurerm_resource_group.resource_group.name
  location            = azurerm_resource_group.resource_group.location
  os_type             = "Linux"
  sku_name            = "B1"
}

resource "azurerm_storage_account" "storage_account" {
  name                     = "openaifunctionsa"
  resource_group_name      = azurerm_resource_group.resource_group.name
  location                 = azurerm_resource_group.resource_group.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_linux_function_app" "function_app" {
  name                = "openai-function-fa"
  resource_group_name = azurerm_resource_group.resource_group.name
  location            = azurerm_resource_group.resource_group.location

  storage_account_name       = azurerm_storage_account.storage_account.name
  storage_account_access_key = azurerm_storage_account.storage_account.primary_access_key
  service_plan_id            = azurerm_service_plan.app_service_plan.id

  site_config {}
}