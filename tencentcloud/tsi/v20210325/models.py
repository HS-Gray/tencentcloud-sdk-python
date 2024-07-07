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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class DisplayInfo(AbstractModel):
    """同传结果数据

    """

    def __init__(self):
        r"""
        :param _SeId: 句子 ID
        :type SeId: str
        :param _SeVer: 句子版本号
        :type SeVer: int
        :param _SourceText: 识别结果
        :type SourceText: str
        :param _TargetText:  翻译结果
        :type TargetText: str
        :param _StartTime: 句子开始时间
        :type StartTime: int
        :param _EndTime: 句子结束时间
        :type EndTime: int
        :param _IsEnd:  当前句子是否已结束
        :type IsEnd: bool
        """
        self._SeId = None
        self._SeVer = None
        self._SourceText = None
        self._TargetText = None
        self._StartTime = None
        self._EndTime = None
        self._IsEnd = None

    @property
    def SeId(self):
        return self._SeId

    @SeId.setter
    def SeId(self, SeId):
        self._SeId = SeId

    @property
    def SeVer(self):
        return self._SeVer

    @SeVer.setter
    def SeVer(self, SeVer):
        self._SeVer = SeVer

    @property
    def SourceText(self):
        return self._SourceText

    @SourceText.setter
    def SourceText(self, SourceText):
        self._SourceText = SourceText

    @property
    def TargetText(self):
        return self._TargetText

    @TargetText.setter
    def TargetText(self, TargetText):
        self._TargetText = TargetText

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def IsEnd(self):
        return self._IsEnd

    @IsEnd.setter
    def IsEnd(self, IsEnd):
        self._IsEnd = IsEnd


    def _deserialize(self, params):
        self._SeId = params.get("SeId")
        self._SeVer = params.get("SeVer")
        self._SourceText = params.get("SourceText")
        self._TargetText = params.get("TargetText")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._IsEnd = params.get("IsEnd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TongChuanDisplayRequest(AbstractModel):
    """TongChuanDisplay请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionUuid: 一段完整的语音对应一个SessionUuid
        :type SessionUuid: str
        :param _IsNew: 句子排序方式，1-由新到旧
        :type IsNew: int
        :param _SeMax: 最多返回几句，目前只支持 5 条数据
        :type SeMax: int
        """
        self._SessionUuid = None
        self._IsNew = None
        self._SeMax = None

    @property
    def SessionUuid(self):
        return self._SessionUuid

    @SessionUuid.setter
    def SessionUuid(self, SessionUuid):
        self._SessionUuid = SessionUuid

    @property
    def IsNew(self):
        return self._IsNew

    @IsNew.setter
    def IsNew(self, IsNew):
        self._IsNew = IsNew

    @property
    def SeMax(self):
        return self._SeMax

    @SeMax.setter
    def SeMax(self, SeMax):
        self._SeMax = SeMax


    def _deserialize(self, params):
        self._SessionUuid = params.get("SessionUuid")
        self._IsNew = params.get("IsNew")
        self._SeMax = params.get("SeMax")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TongChuanDisplayResponse(AbstractModel):
    """TongChuanDisplay返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 同传结果数组
        :type List: list of DisplayInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._RequestId = None

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DisplayInfo()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class TongChuanRecognizeRequest(AbstractModel):
    """TongChuanRecognize请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionUuid: 一段完整的语音对应一个SessionUuid
        :type SessionUuid: str
        :param _Source: 音频中的语言类型，支持语言列表<li> zh : 中文 </li> <li> en : 英文 </li>
        :type Source: str
        :param _Target: 翻译目标语言类型，支持的语言列表<li> zh : 中文 </li> <li> en : 英文 </li>
        :type Target: str
        :param _AudioFormat: 语音编码类型，1-pcm
        :type AudioFormat: int
        :param _Seq: 语音分片的序号，从0开始
        :type Seq: int
        :param _Utc: 语音开始的时间戳
        :type Utc: int
        :param _IsEnd: 是否最后一片语音分片，0-否，1-是
        :type IsEnd: int
        :param _TranslateTime: 翻译时机，0-不翻译 2-句子实时翻译
        :type TranslateTime: int
        :param _Data: 语音分片内容进行 Base64 编码后的字符串。音频内容需包含有效并可识别的文本信息。
        :type Data: str
        """
        self._SessionUuid = None
        self._Source = None
        self._Target = None
        self._AudioFormat = None
        self._Seq = None
        self._Utc = None
        self._IsEnd = None
        self._TranslateTime = None
        self._Data = None

    @property
    def SessionUuid(self):
        return self._SessionUuid

    @SessionUuid.setter
    def SessionUuid(self, SessionUuid):
        self._SessionUuid = SessionUuid

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Target(self):
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def AudioFormat(self):
        return self._AudioFormat

    @AudioFormat.setter
    def AudioFormat(self, AudioFormat):
        self._AudioFormat = AudioFormat

    @property
    def Seq(self):
        return self._Seq

    @Seq.setter
    def Seq(self, Seq):
        self._Seq = Seq

    @property
    def Utc(self):
        return self._Utc

    @Utc.setter
    def Utc(self, Utc):
        self._Utc = Utc

    @property
    def IsEnd(self):
        return self._IsEnd

    @IsEnd.setter
    def IsEnd(self, IsEnd):
        self._IsEnd = IsEnd

    @property
    def TranslateTime(self):
        return self._TranslateTime

    @TranslateTime.setter
    def TranslateTime(self, TranslateTime):
        self._TranslateTime = TranslateTime

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._SessionUuid = params.get("SessionUuid")
        self._Source = params.get("Source")
        self._Target = params.get("Target")
        self._AudioFormat = params.get("AudioFormat")
        self._Seq = params.get("Seq")
        self._Utc = params.get("Utc")
        self._IsEnd = params.get("IsEnd")
        self._TranslateTime = params.get("TranslateTime")
        self._Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TongChuanRecognizeResponse(AbstractModel):
    """TongChuanRecognize返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class TongChuanSyncRequest(AbstractModel):
    """TongChuanSync请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionUuid: 一段完整的语音对应一个SessionUuid
        :type SessionUuid: str
        :param _Source: 音频中的语言类型，支持语言列表<li> zh : 中文 </li> <li> en : 英文 </li>
        :type Source: str
        :param _Target: 翻译目标语言类型，支持的语言列表<li> zh : 中文 </li> <li> en : 英文 </li>
        :type Target: str
        :param _AudioFormat: 语音编码类型，1-pcm
        :type AudioFormat: int
        :param _Seq: 语音分片的序号，从0开始
        :type Seq: int
        :param _Utc: 语音开始的时间戳
        :type Utc: int
        :param _IsEnd: 是否最后一片语音分片，0-否，1-是
        :type IsEnd: int
        :param _TranslateTime: 翻译时机，0-不翻译 2-句子实时翻译
        :type TranslateTime: int
        :param _Data: 语音分片内容进行 Base64 编码后的字符串。音频内容需包含有效并可识别的文本信息。
        :type Data: str
        """
        self._SessionUuid = None
        self._Source = None
        self._Target = None
        self._AudioFormat = None
        self._Seq = None
        self._Utc = None
        self._IsEnd = None
        self._TranslateTime = None
        self._Data = None

    @property
    def SessionUuid(self):
        return self._SessionUuid

    @SessionUuid.setter
    def SessionUuid(self, SessionUuid):
        self._SessionUuid = SessionUuid

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Target(self):
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def AudioFormat(self):
        return self._AudioFormat

    @AudioFormat.setter
    def AudioFormat(self, AudioFormat):
        self._AudioFormat = AudioFormat

    @property
    def Seq(self):
        return self._Seq

    @Seq.setter
    def Seq(self, Seq):
        self._Seq = Seq

    @property
    def Utc(self):
        return self._Utc

    @Utc.setter
    def Utc(self, Utc):
        self._Utc = Utc

    @property
    def IsEnd(self):
        return self._IsEnd

    @IsEnd.setter
    def IsEnd(self, IsEnd):
        self._IsEnd = IsEnd

    @property
    def TranslateTime(self):
        return self._TranslateTime

    @TranslateTime.setter
    def TranslateTime(self, TranslateTime):
        self._TranslateTime = TranslateTime

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._SessionUuid = params.get("SessionUuid")
        self._Source = params.get("Source")
        self._Target = params.get("Target")
        self._AudioFormat = params.get("AudioFormat")
        self._Seq = params.get("Seq")
        self._Utc = params.get("Utc")
        self._IsEnd = params.get("IsEnd")
        self._TranslateTime = params.get("TranslateTime")
        self._Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TongChuanSyncResponse(AbstractModel):
    """TongChuanSync返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 同传结果数组
        :type List: list of DisplayInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._RequestId = None

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DisplayInfo()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")