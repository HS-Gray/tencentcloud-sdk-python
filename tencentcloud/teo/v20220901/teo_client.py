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
from tencentcloud.teo.v20220901 import models


class TeoClient(AbstractClient):
    _apiVersion = '2022-09-01'
    _endpoint = 'teo.tencentcloudapi.com'
    _service = 'teo'


    def BindZoneToPlan(self, request):
        """将未绑定套餐的站点绑定到已有套餐

        :param request: Request instance for BindZoneToPlan.
        :type request: :class:`tencentcloud.teo.v20220901.models.BindZoneToPlanRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.BindZoneToPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindZoneToPlan", params, headers=headers)
            response = json.loads(body)
            model = models.BindZoneToPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckCnameStatus(self, request):
        """校验域名 CNAME 状态

        :param request: Request instance for CheckCnameStatus.
        :type request: :class:`tencentcloud.teo.v20220901.models.CheckCnameStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CheckCnameStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckCnameStatus", params, headers=headers)
            response = json.loads(body)
            model = models.CheckCnameStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAccelerationDomain(self, request):
        """在创建完站点之后，您可以通过本接口创建加速域名。

        CNAME 模式接入时，若您未完成站点归属权校验，本接口将为您返回域名归属权验证信息，您可以单独对域名进行归属权验证，详情参考 [站点/域名归属权验证](https://cloud.tencent.com/document/product/1552/70789)。

        :param request: Request instance for CreateAccelerationDomain.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateAccelerationDomainRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateAccelerationDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAccelerationDomain", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAccelerationDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAliasDomain(self, request):
        """创建别称域名。

        :param request: Request instance for CreateAliasDomain.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateAliasDomainRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateAliasDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAliasDomain", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAliasDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApplicationProxy(self, request):
        """创建应用代理

        :param request: Request instance for CreateApplicationProxy.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateApplicationProxyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateApplicationProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApplicationProxy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApplicationProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApplicationProxyRule(self, request):
        """创建应用代理规则

        :param request: Request instance for CreateApplicationProxyRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateApplicationProxyRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateApplicationProxyRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApplicationProxyRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApplicationProxyRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOriginGroup(self, request):
        """创建源站组，以源站组的方式管理业务源站。此处配置的源站组可于**添加加速域名**和**四层代理**等功能中引用。

        :param request: Request instance for CreateOriginGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateOriginGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateOriginGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOriginGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOriginGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePlanForZone(self, request):
        """为未购买套餐的站点购买套餐

        :param request: Request instance for CreatePlanForZone.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreatePlanForZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreatePlanForZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePlanForZone", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePlanForZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePrefetchTask(self, request):
        """创建预热任务

        :param request: Request instance for CreatePrefetchTask.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreatePrefetchTaskRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreatePrefetchTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrefetchTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePrefetchTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePurgeTask(self, request):
        """当源站资源更新，但节点缓存 TTL 未过期时，用户仍会访问到旧的资源，此时可以通过该接口实现节点资源更新。触发更新的方法有以下两种：<li>直接删除：不做任何校验，直接删除节点缓存，用户请求时触发回源拉取；</li><li>标记过期：将节点资源置为过期，用户请求时触发回源校验，即发送带有 If-None-Match 和 If-Modified-Since 头部的 HTTP 条件请求。若源站响应 200，则节点会回源拉取新的资源并更新缓存；若源站响应 304，则节点不会更新缓存；</li>

        清除缓存任务详情请查看[清除缓存](https://cloud.tencent.com/document/product/1552/70759)。

        :param request: Request instance for CreatePurgeTask.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreatePurgeTaskRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreatePurgeTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePurgeTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePurgeTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRule(self, request):
        """规则引擎创建规则。

        :param request: Request instance for CreateRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSecurityIPGroup(self, request):
        """创建安全 IP 组

        :param request: Request instance for CreateSecurityIPGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateSecurityIPGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateSecurityIPGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSecurityIPGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSecurityIPGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSharedCNAME(self, request):
        """创建共享 CNAME

        :param request: Request instance for CreateSharedCNAME.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateSharedCNAMERequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateSharedCNAMEResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSharedCNAME", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSharedCNAMEResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateZone(self, request):
        """EdgeOne 为您提供 CNAME、NS 和无域名接入三种接入方式，您需要先通过此接口完成站点创建。CNAME 和 NS 接入站点的场景可参考 [从零开始快速接入 EdgeOne](https://cloud.tencent.com/document/product/1552/87601); 无域名接入的场景可参考 [快速启用四层代理服务](https://cloud.tencent.com/document/product/1552/96051)。

        > 建议您在账号下已存在套餐时调用本接口创建站点，请在入参时传入 PlanId ，直接将站点绑定至该套餐；不传入 PlanId 时，创建出来的站点会处于未激活状态，无法正常服务，您需要通过 [BindZoneToPlan](https://cloud.tencent.com/document/product/1552/83042) 完成套餐绑定之后，站点才可正常提供服务 。若您当前没有可绑定的套餐时，请前往控制台购买套餐完成站点创建。

        :param request: Request instance for CreateZone.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateZone", params, headers=headers)
            response = json.loads(body)
            model = models.CreateZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAccelerationDomains(self, request):
        """批量删除加速域名

        :param request: Request instance for DeleteAccelerationDomains.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteAccelerationDomainsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteAccelerationDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAccelerationDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAccelerationDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAliasDomain(self, request):
        """删除别称域名。

        :param request: Request instance for DeleteAliasDomain.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteAliasDomainRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteAliasDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAliasDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAliasDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteApplicationProxy(self, request):
        """删除应用代理

        :param request: Request instance for DeleteApplicationProxy.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteApplicationProxyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteApplicationProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApplicationProxy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteApplicationProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteApplicationProxyRule(self, request):
        """删除应用代理规则

        :param request: Request instance for DeleteApplicationProxyRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteApplicationProxyRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteApplicationProxyRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApplicationProxyRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteApplicationProxyRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteOriginGroup(self, request):
        """删除源站组，若源站组仍然被服务（例如：四层代理，域名服务，负载均衡，规则引起）引用，将不允许删除。

        :param request: Request instance for DeleteOriginGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteOriginGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteOriginGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOriginGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteOriginGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRules(self, request):
        """批量删除规则引擎规则。

        :param request: Request instance for DeleteRules.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSecurityIPGroup(self, request):
        """删除指定 IP 组，如果有规则引用了 IP 组情况，则不允许删除。

        :param request: Request instance for DeleteSecurityIPGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteSecurityIPGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteSecurityIPGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSecurityIPGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSecurityIPGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteZone(self, request):
        """删除站点。

        :param request: Request instance for DeleteZone.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteZone", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccelerationDomains(self, request):
        """您可以通过本接口查看站点下的域名信息，包括加速域名、源站以及域名状态等信息。您可以查看站点下全部域名的信息，也可以指定过滤条件查询对应的域名信息。

        :param request: Request instance for DescribeAccelerationDomains.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeAccelerationDomainsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeAccelerationDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccelerationDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccelerationDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAliasDomains(self, request):
        """查询别称域名信息列表。

        :param request: Request instance for DescribeAliasDomains.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeAliasDomainsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeAliasDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAliasDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAliasDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplicationProxies(self, request):
        """查询应用代理列表。

        :param request: Request instance for DescribeApplicationProxies.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeApplicationProxiesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeApplicationProxiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationProxies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationProxiesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAvailablePlans(self, request):
        """查询当前账户可用套餐信息列表

        :param request: Request instance for DescribeAvailablePlans.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeAvailablePlansRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeAvailablePlansResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAvailablePlans", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAvailablePlansResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeContentQuota(self, request):
        """查询内容管理接口配额

        :param request: Request instance for DescribeContentQuota.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeContentQuotaRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeContentQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeContentQuota", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeContentQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDDoSAttackData(self, request):
        """本接口（DescribeDDoSAttackData）用于查询DDoS攻击时序数据。

        :param request: Request instance for DescribeDDoSAttackData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDoSAttackData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDDoSAttackDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDDoSAttackEvent(self, request):
        """本接口（DescribeDDoSAttackEvent）用于查询DDoS攻击事件列表。

        :param request: Request instance for DescribeDDoSAttackEvent.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackEventRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDoSAttackEvent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDDoSAttackEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDDoSAttackTopData(self, request):
        """本接口（DescribeDDoSAttackTopData）用于查询DDoS攻击Top数据。

        :param request: Request instance for DescribeDDoSAttackTopData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackTopDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackTopDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDoSAttackTopData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDDoSAttackTopDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDefaultCertificates(self, request):
        """查询默认证书列表

        :param request: Request instance for DescribeDefaultCertificates.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDefaultCertificatesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDefaultCertificatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDefaultCertificates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDefaultCertificatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostsSetting(self, request):
        """用于查询域名配置信息

        :param request: Request instance for DescribeHostsSetting.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeHostsSettingRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeHostsSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostsSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostsSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIdentifications(self, request):
        """查询站点的验证信息。

        :param request: Request instance for DescribeIdentifications.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeIdentificationsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeIdentificationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIdentifications", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIdentificationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOriginGroup(self, request):
        """获取源站组列表

        :param request: Request instance for DescribeOriginGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeOriginGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeOriginGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOriginGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOriginGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOriginProtection(self, request):
        """查询源站防护信息

        :param request: Request instance for DescribeOriginProtection.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeOriginProtectionRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeOriginProtectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOriginProtection", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOriginProtectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOverviewL7Data(self, request):
        """本接口（DescribeOverviewL7Data）用于查询七层监控类时序流量数据。

        :param request: Request instance for DescribeOverviewL7Data.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeOverviewL7DataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeOverviewL7DataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOverviewL7Data", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOverviewL7DataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePrefetchTasks(self, request):
        """查询预热任务状态

        :param request: Request instance for DescribePrefetchTasks.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribePrefetchTasksRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribePrefetchTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrefetchTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrefetchTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePurgeTasks(self, request):
        """查询清除缓存历史记录

        :param request: Request instance for DescribePurgeTasks.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribePurgeTasksRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribePurgeTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePurgeTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePurgeTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRules(self, request):
        """查询规则引擎规则。

        :param request: Request instance for DescribeRules.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRulesSetting(self, request):
        """返回规则引擎可应用匹配请求的设置列表及其详细建议配置信息

        :param request: Request instance for DescribeRulesSetting.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeRulesSettingRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeRulesSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRulesSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRulesSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityTemplateBindings(self, request):
        """查询指定策略模板的绑定关系列表。

        :param request: Request instance for DescribeSecurityTemplateBindings.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityTemplateBindingsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityTemplateBindingsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityTemplateBindings", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityTemplateBindingsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTimingL4Data(self, request):
        """本接口（DescribeTimingL4Data）用于查询四层时序流量数据列表。

        :param request: Request instance for DescribeTimingL4Data.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL4DataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL4DataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTimingL4Data", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTimingL4DataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTimingL7AnalysisData(self, request):
        """本接口（DescribeTimingL7AnalysisData）查询七层数据分析类时序数据。

        :param request: Request instance for DescribeTimingL7AnalysisData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL7AnalysisDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL7AnalysisDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTimingL7AnalysisData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTimingL7AnalysisDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTimingL7CacheData(self, request):
        """本接口（DescribeTimingL7CacheData）用于查询七层缓存分析时序类流量数据。

        :param request: Request instance for DescribeTimingL7CacheData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL7CacheDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL7CacheDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTimingL7CacheData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTimingL7CacheDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopL7AnalysisData(self, request):
        """本接口（DescribeTopL7AnalysisData）用于查询七层流量前topN的数据。

        :param request: Request instance for DescribeTopL7AnalysisData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeTopL7AnalysisDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeTopL7AnalysisDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopL7AnalysisData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopL7AnalysisDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopL7CacheData(self, request):
        """本接口（DescribeTopL7CacheData）用于查询七层缓存分析topN流量数据。

        :param request: Request instance for DescribeTopL7CacheData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeTopL7CacheDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeTopL7CacheDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopL7CacheData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopL7CacheDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZoneSetting(self, request):
        """用于查询站点的所有配置信息。

        :param request: Request instance for DescribeZoneSetting.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeZoneSettingRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeZoneSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZoneSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeZoneSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZones(self, request):
        """该接口用于查询您有权限的站点信息。可根据不同查询条件筛选站点。

        :param request: Request instance for DescribeZones.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeZonesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeZonesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZones", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeZonesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DownloadL4Logs(self, request):
        """本接口（DownloadL4Logs）用于下载四层离线日志。

        :param request: Request instance for DownloadL4Logs.
        :type request: :class:`tencentcloud.teo.v20220901.models.DownloadL4LogsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DownloadL4LogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownloadL4Logs", params, headers=headers)
            response = json.loads(body)
            model = models.DownloadL4LogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DownloadL7Logs(self, request):
        """本接口（DownloadL7Logs）下载七层离线日志。

        :param request: Request instance for DownloadL7Logs.
        :type request: :class:`tencentcloud.teo.v20220901.models.DownloadL7LogsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DownloadL7LogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownloadL7Logs", params, headers=headers)
            response = json.loads(body)
            model = models.DownloadL7LogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IdentifyZone(self, request):
        """用于验证站点所有权。

        :param request: Request instance for IdentifyZone.
        :type request: :class:`tencentcloud.teo.v20220901.models.IdentifyZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.IdentifyZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IdentifyZone", params, headers=headers)
            response = json.loads(body)
            model = models.IdentifyZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccelerationDomain(self, request):
        """修改加速域名信息

        :param request: Request instance for ModifyAccelerationDomain.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyAccelerationDomainRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyAccelerationDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccelerationDomain", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccelerationDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccelerationDomainStatuses(self, request):
        """批量修改加速域名状态

        :param request: Request instance for ModifyAccelerationDomainStatuses.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyAccelerationDomainStatusesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyAccelerationDomainStatusesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccelerationDomainStatuses", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccelerationDomainStatusesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAliasDomain(self, request):
        """修改别称域名。

        :param request: Request instance for ModifyAliasDomain.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyAliasDomainRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyAliasDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAliasDomain", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAliasDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAliasDomainStatus(self, request):
        """修改别称域名状态。

        :param request: Request instance for ModifyAliasDomainStatus.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyAliasDomainStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyAliasDomainStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAliasDomainStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAliasDomainStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApplicationProxy(self, request):
        """修改应用代理

        :param request: Request instance for ModifyApplicationProxy.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationProxy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApplicationProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApplicationProxyRule(self, request):
        """修改应用代理规则

        :param request: Request instance for ModifyApplicationProxyRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationProxyRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApplicationProxyRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApplicationProxyRuleStatus(self, request):
        """修改应用代理规则的状态

        :param request: Request instance for ModifyApplicationProxyRuleStatus.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyRuleStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationProxyRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApplicationProxyRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApplicationProxyStatus(self, request):
        """修改应用代理的状态

        :param request: Request instance for ModifyApplicationProxyStatus.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationProxyStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApplicationProxyStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyHostsCertificate(self, request):
        """完成域名创建之后，您可以为域名配置自有证书，也可以使用 EdgeOne 为您提供的 [免费证书](https://cloud.tencent.com/document/product/1552/90437)。
        如果您需要配置自有证书，请先将证书上传至 [SSL证书控制台](https://console.cloud.tencent.com/certoverview)，然后在本接口中传入对应的证书 ID。详情参考 [部署自有证书至 EdgeOne 域名
        ](https://cloud.tencent.com/document/product/1552/88874)。

        :param request: Request instance for ModifyHostsCertificate.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyHostsCertificateRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyHostsCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyHostsCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyHostsCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyOriginGroup(self, request):
        """修改源站组配置，新提交的源站记录将会覆盖原有源站组中的源站记录。

        :param request: Request instance for ModifyOriginGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyOriginGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyOriginGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyOriginGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyOriginGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRule(self, request):
        """修改规则引擎规则。

        :param request: Request instance for ModifyRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecurityIPGroup(self, request):
        """修改安全 IP 组。

        :param request: Request instance for ModifySecurityIPGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifySecurityIPGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifySecurityIPGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityIPGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecurityIPGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecurityPolicy(self, request):
        """修改Web&Bot安全配置。

        :param request: Request instance for ModifySecurityPolicy.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifySecurityPolicyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifySecurityPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecurityPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyZone(self, request):
        """修改站点信息。

        :param request: Request instance for ModifyZone.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyZone", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyZoneSetting(self, request):
        """用于修改站点配置

        :param request: Request instance for ModifyZoneSetting.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyZoneSettingRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyZoneSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyZoneSetting", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyZoneSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyZoneStatus(self, request):
        """用于开启，关闭站点。

        :param request: Request instance for ModifyZoneStatus.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyZoneStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyZoneStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyZoneStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyZoneStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def VerifyOwnership(self, request):
        """在 CNAME 接入模式下，您需要对站点或者域名的归属权进行验证，可以通过本接口触发验证。若站点通过归属权验证后，后续添加域名无需再验证。详情参考 [站点/域名归属权验证](https://cloud.tencent.com/document/product/1552/70789)。

        在 NS 接入模式下，您也可以通过本接口来查询 NS 服务器是否切换成功，详情参考 [修改 DNS 服务器](https://cloud.tencent.com/document/product/1552/90452)。

        :param request: Request instance for VerifyOwnership.
        :type request: :class:`tencentcloud.teo.v20220901.models.VerifyOwnershipRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.VerifyOwnershipResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VerifyOwnership", params, headers=headers)
            response = json.loads(body)
            model = models.VerifyOwnershipResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))