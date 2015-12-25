#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

# RESOURCE_TYPES = ["instance", "volume", "bandwidth", "ha", "router", "rdb",
#                   "load_balancer", "snapshot", "self_image"]

# RESOURCE_STATUS = ["active", "paused"]

MIN_VALUE = "1"
MAX_VALUE = "100000000"

RPC_ATTRs = (
    ENGINE_TOPIC,
    ENGINE_HEALTH_MGR_TOPIC,
    NOTIFICATION_TOPICS,
    RPC_API_VERSION,
) = (
    'bilean-engine',
    'engine-health_mgr',
    'billing_notifications',
    '1.0',
)
    
USER_KEYS = (
    USER_ID,
    USER_BALANCE,
    USER_RATE,
    USER_CREDIT,
    USER_LAST_BILL,
    USER_STATUS,
    USER_STATUS_REASION,
    USER_CREATED_AT,
    USER_UPDATED_AT
) = (
    'id',
    'balance',
    'rate',
    'credit',
    'last_bill',
    'status',
    'status_reason',
    'created_at',
    'updated_at'
)

RES_KEYS = (
    RES_ID,
    RES_RESOURCE_TYPE,
    RES_SIZE,
    RES_RATE,
    RES_STATUS,
    RES_STATUS_REASON,
    RES_USER_ID,
    RES_RULE_ID,
    RES_RESOURCE_REF,
    RES_CREATED_AT,
    RES_UPDATED_AT,
    RES_DELETED_AT,
    RES_DELETED
) = (
    'id',
    'resource_type',
    'size',
    'rate',
    'status',
    'status_reason',
    'user_id',
    'rule_id',
    'resource_ref',
    'created_at',
    'updated_at',
    'deleted_at',
    'deleted'
)

RULE_KEYS = (
    RULE_ID,
    RULE_NAME,
    RULE_TYPE,
    RULE_SPEC,
    RULE_METADATA,
    RULE_UPDATED_AT,
    RULE_CREATED_AT,
    RULE_DELETED_AT,
) = (
    'id',
    'name',
    'type',
    'spec',
    'metadata',
    'updated_at',
    'created_at',
    'deleted_at',
)