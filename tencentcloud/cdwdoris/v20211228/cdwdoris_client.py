# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.cdwdoris.v20211228 import models


class CdwdorisClient(AbstractClient):
    _apiVersion = '2021-12-28'
    _endpoint = 'cdwdoris.tencentcloudapi.com'
    _service = 'cdwdoris'


    def DescribeInstance(self, request):
        """根据实例ID查询某个实例的具体信息

        :param request: Request instance for DescribeInstance.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceNodes(self, request):
        """获取实例节点信息列表

        :param request: Request instance for DescribeInstanceNodes.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceNodesRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceNodes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstances(self, request):
        """获取实例列表

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))