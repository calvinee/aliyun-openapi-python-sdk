# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkdbs.endpoint import endpoint_data

class CreateIncrementBackupSetDownloadRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dbs', '2019-03-06', 'CreateIncrementBackupSetDownload','cbs')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_BackupSetName(self):
		return self.get_query_params().get('BackupSetName')

	def set_BackupSetName(self,BackupSetName):
		self.add_query_param('BackupSetName',BackupSetName)

	def get_BackupSetId(self):
		return self.get_query_params().get('BackupSetId')

	def set_BackupSetId(self,BackupSetId):
		self.add_query_param('BackupSetId',BackupSetId)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_BackupSetDataFormat(self):
		return self.get_query_params().get('BackupSetDataFormat')

	def set_BackupSetDataFormat(self,BackupSetDataFormat):
		self.add_query_param('BackupSetDataFormat',BackupSetDataFormat)