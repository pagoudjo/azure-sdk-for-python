# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class ErrorContract(msrest.serialization.Model):
    """Contains details when the response code indicates an error.

    :param error: The error details.
    :type error: ~azure.synapse.accesscontrol.models.ErrorResponse
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorResponse'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorContract, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class ErrorDetail(msrest.serialization.Model):
    """ErrorDetail.

    All required parameters must be populated in order to send to Azure.

    :param code: Required.
    :type code: str
    :param message: Required.
    :type message: str
    :param target:
    :type target: str
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorDetail, self).__init__(**kwargs)
        self.code = kwargs['code']
        self.message = kwargs['message']
        self.target = kwargs.get('target', None)


class ErrorResponse(msrest.serialization.Model):
    """ErrorResponse.

    All required parameters must be populated in order to send to Azure.

    :param code: Required.
    :type code: str
    :param message: Required.
    :type message: str
    :param target:
    :type target: str
    :param details:
    :type details: list[~azure.synapse.accesscontrol.models.ErrorDetail]
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorDetail]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.code = kwargs['code']
        self.message = kwargs['message']
        self.target = kwargs.get('target', None)
        self.details = kwargs.get('details', None)


class RoleAssignmentDetails(msrest.serialization.Model):
    """Role Assignment response details.

    :param id: Role Assignment ID.
    :type id: str
    :param role_id: Role ID of the Synapse Built-In Role.
    :type role_id: str
    :param principal_id: Object ID of the AAD principal or security-group.
    :type principal_id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'role_id': {'key': 'roleId', 'type': 'str'},
        'principal_id': {'key': 'principalId', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(RoleAssignmentDetails, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.role_id = kwargs.get('role_id', None)
        self.principal_id = kwargs.get('principal_id', None)


class RoleAssignmentOption(msrest.serialization.Model):
    """Role Assignment request details.

    All required parameters must be populated in order to send to Azure.

    :param role_id: Required. Role ID of the Synapse Built-In Role.
    :type role_id: str
    :param principal_id: Required. Object ID of the AAD principal or security-group.
    :type principal_id: str
    """

    _validation = {
        'role_id': {'required': True},
        'principal_id': {'required': True},
    }

    _attribute_map = {
        'role_id': {'key': 'roleId', 'type': 'str'},
        'principal_id': {'key': 'principalId', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(RoleAssignmentOption, self).__init__(**kwargs)
        self.role_id = kwargs['role_id']
        self.principal_id = kwargs['principal_id']


class RolesListResponse(msrest.serialization.Model):
    """A list of Synapse roles available.

    All required parameters must be populated in order to send to Azure.

    :param value: Required. List of Synapse roles.
    :type value: list[~azure.synapse.accesscontrol.models.SynapseRole]
    :param next_link: The link to the next page of results, if any remaining results exist.
    :type next_link: str
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[SynapseRole]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(RolesListResponse, self).__init__(**kwargs)
        self.value = kwargs['value']
        self.next_link = kwargs.get('next_link', None)


class SynapseRole(msrest.serialization.Model):
    """Synapse role details.

    All required parameters must be populated in order to send to Azure.

    :param id: Role ID.
    :type id: str
    :param name: Name of the Synapse role.
    :type name: str
    :param is_built_in: Required. Is a built-in role or not.
    :type is_built_in: bool
    """

    _validation = {
        'is_built_in': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'is_built_in': {'key': 'isBuiltIn', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SynapseRole, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.is_built_in = kwargs['is_built_in']
