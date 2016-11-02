# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from oslo_config import cfg

from senlin.common import consts
from senlin.objects import base
from senlin.objects import fields

CONF = cfg.CONF
CONF.import_opt('default_action_timeout', 'senlin.common.config')


@base.SenlinObjectRegistry.register
class ClusterListRequest(base.SenlinObject):

    fields = {
        'name': fields.ListOfStringsField(nullable=True),
        'status': fields.ListOfEnumField(
            valid_values=list(consts.CLUSTER_STATUSES), nullable=True),
        'limit': fields.NonNegativeIntegerField(nullable=True),
        'marker': fields.UUIDField(nullable=True),
        'sort': fields.SortField(
            valid_keys=list(consts.CLUSTER_SORT_KEYS), nullable=True),
        'project_safe': fields.FlexibleBooleanField(default=True),
    }


@base.SenlinObjectRegistry.register
class ClusterCreateRequestBody(base.SenlinObject):

    fields = {
        'name': fields.NameField(),
        'profile_id': fields.StringField(),
        'min_size': fields.CapacityField(
            nullable=True, minimum=0,
            default=consts.CLUSTER_DEFAULT_MIN_SIZE),
        'max_size': fields.CapacityField(
            nullable=True, minimum=-1,
            default=consts.CLUSTER_DEFAULT_MAX_SIZE),
        'desired_capacity': fields.CapacityField(
            nullable=True, minimum=0,
            default=consts.CLUSTER_DEFAULT_MIN_SIZE),
        'metadata': fields.JsonField(nullable=True, default={}),
        'timeout': fields.NonNegativeIntegerField(
            nullable=True, default=CONF.default_action_timeout),
    }


@base.SenlinObjectRegistry.register
class ClusterCreateRequest(base.SenlinObject):

    fields = {
        'cluster': fields.ObjectField('ClusterCreateRequestBody')
    }


@base.SenlinObjectRegistry.register
class ClusterGetRequest(base.SenlinObject):

    fields = {
        'identity': fields.StringField()
    }


@base.SenlinObjectRegistry.register
class ClusterUpdateRequest(base.SenlinObject):

    fields = {
        'identity': fields.StringField(),
        'name': fields.NameField(nullable=True),
        'profile_id': fields.StringField(nullable=True),
        'metadata': fields.JsonField(nullable=True),
        'timeout': fields.IntegerField(nullable=True),
    }


@base.SenlinObjectRegistry.register
class ClusterAddNodesRequest(base.SenlinObject):

    fields = {
        'identity': fields.StringField(),
        'nodes': fields.IdentityListField(min_items=1)
    }


@base.SenlinObjectRegistry.register
class ClusterDelNodesRequest(base.SenlinObject):

    fields = {
        'identity': fields.StringField(),
        'nodes': fields.IdentityListField(min_items=1)
    }


@base.SenlinObjectRegistry.register
class ClusterResizeRequest(base.SenlinObject):

    fields = {
        'identity': fields.StringField(),
        'adjustment_type': fields.AdjustmentTypeField(nullable=True),
        'number': fields.FloatField(nullable=True),
        'min_size': fields.CapacityField(nullable=True, minimum=0),
        'max_size': fields.CapacityField(nullable=True, minimum=-1),
        'min_step': fields.NonNegativeIntegerField(nullable=True),
        'strict': fields.BooleanField(nullable=True, default=True)
    }


@base.SenlinObjectRegistry.register
class ClusterScaleInRequest(base.SenlinObject):

    fields = {
        'identity': fields.StringField(),
        'count': fields.NonNegativeIntegerField(nullable=True)
    }


@base.SenlinObjectRegistry.register
class ClusterScaleOutRequest(base.SenlinObject):

    fields = {
        'identity': fields.StringField(),
        'count': fields.NonNegativeIntegerField(nullable=True)
    }


@base.SenlinObjectRegistry.register
class ClusterAttachPolicyRequest(base.SenlinObject):

    fields = {
        'identity': fields.StringField(),
        'policy_id': fields.StringField(),
        'enabled': fields.BooleanField(default=True),
    }
