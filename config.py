# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

class BaseConfig(object):

    # Can be set to 'MasterUser' or 'ServicePrincipal'
    AUTHENTICATION_MODE = 'ServicePrincipal'

    # Workspace Id in which the report is present
    WORKSPACE_ID = '1d70a630-99b5-452f-9aae-c644bcf0f9b2'
    
    # Report Id for which Embed token needs to be generated
    REPORT_ID = '826c9492-e75a-4596-999c-eca95df9872e'
    
    # Id of the Azure tenant in which AAD app and Power BI report is hosted. Required only for ServicePrincipal authentication mode.
    TENANT_ID = '645fd607-1371-41f1-a9e2-53e1734038dc'
    
    # Client Id (Application Id) of the AAD app
    CLIENT_ID = 'e5c8122f-8a99-4095-ae60-a79c494c8905'
    
    # Client Secret (App Secret) of the AAD app.  Required only for ServicePrincipal authentication mode.
    CLIENT_SECRET = 'nbP8Q~yxIdEy4l0frxbZdrrKt9OI0HxFdR9i8a1i'
    
    # Scope Base of AAD app. Use the below configuration to use all the permissions provided in the AAD app through Azure portal.
    SCOPE_BASE = ['https://analysis.windows.net/powerbi/api/.default']
    
    # URL used for initiating authorization request
    AUTHORITY_URL = 'https://login.microsoftonline.com/organizations'
    
    # Master user email address. Required only for MasterUser authentication mode.
    POWER_BI_USER = 'Adriaan@ElephantBI.onmicrosoft.com'
    
    # Master user email password. Required only for MasterUser authentication mode.
    POWER_BI_PASS = 'A3an4rie'