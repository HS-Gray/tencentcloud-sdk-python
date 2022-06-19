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


# CAM签名/鉴权错误。
AUTHFAILURE = 'AuthFailure'

# 操作失败。
FAILEDOPERATION = 'FailedOperation'

# 签署人未达到合法年龄。
FAILEDOPERATION_AGENOTACHIEVENORMALLEGAL = 'FailedOperation.AgeNotAchieveNormalLegal'

# 鉴权失败。
FAILEDOPERATION_AUTHFAIL = 'FailedOperation.AuthFail'

# 发起签署存在填写控件。
FAILEDOPERATION_QRCODECREATORSIGNCOMPONENTS = 'FailedOperation.QrCodeCreatorSignComponents'

# 模板签署人不存在。
FAILEDOPERATION_QRCODESIGNUSERS = 'FailedOperation.QrCodeSignUsers'

# 一码多人二维码模板有误。
FAILEDOPERATION_QRCODETEMPLATEID = 'FailedOperation.QrCodeTemplateId'

# 员工已实名。
FAILEDOPERATION_STAFFALREADYVERIFY = 'FailedOperation.StaffAlreadyVerify'

# 内部错误。
INTERNALERROR = 'InternalError'

# 其他API错误。
INTERNALERROR_API = 'InternalError.Api'

# 数据库错误。
INTERNALERROR_DB = 'InternalError.Db'

# 数据库连接出错。
INTERNALERROR_DBCONNECTION = 'InternalError.DbConnection'

# 数据库新增记录出错。
INTERNALERROR_DBINSERT = 'InternalError.DbInsert'

# 数据库读取失败。
INTERNALERROR_DBREAD = 'InternalError.DbRead'

# 数据库更新记录出错。
INTERNALERROR_DBUPDATE = 'InternalError.DbUpdate'

# 解密错误。
INTERNALERROR_DECRYPTION = 'InternalError.Decryption'

# 加密错误。
INTERNALERROR_ENCRYPTION = 'InternalError.Encryption'

# 生成唯一ID错误。
INTERNALERROR_GENERATEID = 'InternalError.GenerateId'

# 序列化错误。
INTERNALERROR_SERIALIZE = 'InternalError.Serialize'

# 系统错误。
INTERNALERROR_SYSTEM = 'InternalError.System'

# 第三方错误。
INTERNALERROR_THIRDPARTY = 'InternalError.ThirdParty'

# 参数错误。
INVALIDPARAMETER = 'InvalidParameter'

# 应用号不存在。
INVALIDPARAMETER_APPLICATION = 'InvalidParameter.Application'

# 重复添加签署人。
INVALIDPARAMETER_BIZAPPROVERALREADYEXISTS = 'InvalidParameter.BizApproverAlreadyExists'

# 数据不存在。
INVALIDPARAMETER_DATANOTFOUND = 'InvalidParameter.DataNotFound'

# 参数为空。
INVALIDPARAMETER_EMPTYPARAMS = 'InvalidParameter.EmptyParams'

# 参数错误。
INVALIDPARAMETER_PARAMERROR = 'InvalidParameter.ParamError'

# 参数取值错误。
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# 超过配额限制。
LIMITEXCEEDED = 'LimitExceeded'

# 缺少参数错误。
MISSINGPARAMETER = 'MissingParameter'

# 操作被拒绝。
OPERATIONDENIED = 'OperationDenied'

# 应用号已被禁止。
OPERATIONDENIED_BANNEDAPPLICATION = 'OperationDenied.BannedApplication'

# 禁止操作。
OPERATIONDENIED_FORBID = 'OperationDenied.Forbid'

# 没有API权限。
OPERATIONDENIED_NOAPIAUTH = 'OperationDenied.NoApiAuth'

# 未通过个人实名。
OPERATIONDENIED_NOIDENTITYVERIFY = 'OperationDenied.NoIdentityVerify'

# 流程配额不足。
OPERATIONDENIED_NOQUOTA = 'OperationDenied.NoQuota'

# 用户不在当前企业中。
OPERATIONDENIED_USERNOTINORGANIZATION = 'OperationDenied.UserNotInOrganization'

# 资源不存在。
RESOURCENOTFOUND = 'ResourceNotFound'

# 应用号不存在。
RESOURCENOTFOUND_APPLICATION = 'ResourceNotFound.Application'

# 未找到对应流程。
RESOURCENOTFOUND_FLOW = 'ResourceNotFound.Flow'

# 机构不存在。
RESOURCENOTFOUND_ORGANIZATION = 'ResourceNotFound.Organization'

# 模板不存在。
RESOURCENOTFOUND_TEMPLATE = 'ResourceNotFound.Template'

# 资源不可用。
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# 未授权操作。
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# 未知参数错误。
UNKNOWNPARAMETER = 'UnknownParameter'

# 操作不支持。
UNSUPPORTEDOPERATION = 'UnsupportedOperation'
